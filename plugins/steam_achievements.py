"""
steam_achievements - Fetch Steam game achievements and create posts for each achievement

# Installation

```toml
hooks = [
  "markata.plugins.steam_achievements",
]
```

# Configuration

```toml
[markata.steam_achievements]
api_key = "your_steam_api_key"  # Steam Web API key
steam_id = "your_steam_id"      # Your Steam ID
posts_dir = "pages/steam"       # Directory to create achievement posts
template = "steam_achievement"  # Jinja2 template name
cache_duration = 3600           # Cache duration in seconds (default: 1 hour)
```

# Usage

Add Steam game information to your post frontmatter:

```yaml
steam:
  app_id: 730  # Counter-Strike: Global Offensive
```

The plugin will fetch achievements and create individual posts for each achievement
on the date they were received.

# Notes

Requires a Steam Web API key from https://steamcommunity.com/dev/apikey
Posts are created with timestamps matching the achievement unlock time.
Existing posts are not overwritten.
"""

from typing import TYPE_CHECKING, Dict, List, Optional, Any
import requests
import time
from pathlib import Path
import json
from datetime import datetime, timezone

from markata.hookspec import hook_impl, register_attr
import pydantic

if TYPE_CHECKING:
    from markata import Markata

MARKATA_PLUGIN_NAME = "SteamAchievements"
MARKATA_PLUGIN_PACKAGE_NAME = "steam_achievements"


class SteamAchievementsConfig(pydantic.BaseModel):
    api_key: Optional[str] = None
    steam_id: Optional[str] = None
    posts_dir: str = "pages/steam"
    template: str = "steam_achievement"
    cache_duration: int = 3600  # 1 hour default

    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True
        extra = "allow"
        str_strip_whitespace = True
        validate_default = True
        coerce_numbers_to_str = True


class Config(pydantic.BaseModel):
    steam_achievements: SteamAchievementsConfig = SteamAchievementsConfig()

    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True
        extra = "allow"


class SteamAchievement(pydantic.BaseModel):
    apiname: str
    achieved: int
    unlocktime: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    icongray: Optional[str] = None


class SteamGameData(pydantic.BaseModel):
    appid: int
    name: str
    achievements: List[SteamAchievement]
    total_achievements: int
    unlocked_achievements: int
    completion_percentage: float

    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True
        extra = "allow"


@hook_impl
@register_attr("config_models")
def config_model(markata: "Markata"):
    markata.config_models.append(Config)


def get_cache_path(markata: "Markata", app_id: int) -> Path:
    """Get the cache file path for Steam achievements data."""
    cache_dir = Path(markata.config.output_dir) / ".steam_cache"
    cache_dir.mkdir(exist_ok=True)
    return cache_dir / f"achievements_{app_id}.json"


def is_cache_valid(cache_path: Path, cache_duration: int) -> bool:
    """Check if cache file is still valid."""
    if not cache_path.exists():
        return False

    file_age = time.time() - cache_path.stat().st_mtime
    return file_age < cache_duration


def create_achievement_post(
    markata: "Markata",
    game_data: SteamGameData,
    achievement: SteamAchievement,
    posts_dir: Path,
) -> bool:
    """Create a markdown post for an individual achievement."""
    # Debug: Check why Portal achievements are being filtered out
    if game_data.appid == 400:
        print(
            f"DEBUG create_achievement_post: {achievement.apiname} - achieved: {achievement.achieved}, unlocktime: {achievement.unlocktime}, achieved_bool: {bool(achievement.achieved)}, unlocktime_bool: {bool(achievement.unlocktime)}"
        )
        print(
            f"DEBUG create_achievement_post: not achieved: {not achievement.achieved}, not unlocktime: {not achievement.unlocktime}"
        )

    if not achievement.achieved or not achievement.unlocktime:
        if game_data.appid == 400:
            print(
                f"DEBUG create_achievement_post: FILTERED OUT - {achievement.apiname}"
            )
        return False  # Only create posts for unlocked achievements

    if game_data.appid == 400:
        print(f"DEBUG create_achievement_post: PASSED FILTER - {achievement.apiname}")

    # Convert unlock timestamp to date
    unlock_date = datetime.fromtimestamp(achievement.unlocktime, tz=timezone.utc)
    date_str = unlock_date.strftime("%Y-%m-%d")

    if game_data.appid == 400:
        print(
            f"DEBUG create_achievement_post: unlock_date: {unlock_date}, date_str: {date_str}"
        )

    # Create filename
    safe_game_name = "".join(
        c for c in game_data.name if c.isalnum() or c in (" ", "-", "_")
    ).rstrip()
    safe_game_name = safe_game_name.replace(" ", "-").lower()
    safe_achievement_name = "".join(
        c for c in (achievement.name or "") if c.isalnum() or c in (" ", "-", "_")
    ).rstrip()
    safe_achievement_name = safe_achievement_name.replace(" ", "-").lower()

    filename = f"{date_str}-{safe_game_name}-{safe_achievement_name}.md"
    filepath = posts_dir / filename

    # Create frontmatter (recreate post even if it already exists)
    frontmatter = {
        "title": achievement.name or f"Achievement in {game_data.name}",
        "description": achievement.description or "",
        "date": date_str,
        "templateKey": "steam_achievement",
        "steam": {
            "game": game_data.name,
            "app_id": game_data.appid,
            "achievement": {
                "name": achievement.name,
                "description": achievement.description,
                "api_name": achievement.apiname,
                "unlock_time": achievement.unlocktime,
                "unlock_date": unlock_date.isoformat(),
                "icon": achievement.icon,
                "icongray": achievement.icongray,
            },
        },
        "tags": ["steam", "achievement", safe_game_name],
    }

    # Create badge image URLs
    badge_url = (
        achievement.icon
        if achievement.icon and achievement.achieved
        else (achievement.icongray or "")
    )
    badge_html = (
        f'<img src="{badge_url}" alt="{achievement.name}" style="width: 64px; height: 64px;">'
        if badge_url
        else ""
    )

    # Write post content with properly quoted frontmatter
    content = f"""---
title: {json.dumps(achievement.name or f"Achievement in {game_data.name}")}
description: {json.dumps(achievement.description or "")}
date: {date_str}
templateKey: steam_achievement
steam:
  game: {json.dumps(game_data.name)}
  app_id: {game_data.appid}
  achievement:
    name: {json.dumps(achievement.name or "")}
    description: {json.dumps(achievement.description or "")}
    api_name: {json.dumps(achievement.apiname)}
    unlock_time: {achievement.unlocktime}
    unlock_date: {json.dumps(unlock_date.isoformat())}
    icon: {json.dumps(achievement.icon or "")}
    icongray: {json.dumps(achievement.icongray or "")}
tags: {json.dumps(["steam", "achievement", safe_game_name])}
---

# {achievement.name or "Achievement Unlocked"}

{badge_html}

{achievement.description or ""}

Unlocked in **{game_data.name}** on {unlock_date.strftime("%B %d, %Y at %I:%M %p")}.

---

*Achievement data automatically imported from Steam.*
"""

    # Ensure posts directory exists
    posts_dir.mkdir(parents=True, exist_ok=True)

    # Write the file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created achievement post: {filepath}")
    return True


def get_steam_games(api_key: str, steam_id: str) -> List[Dict]:
    """Get all games from user's Steam library."""
    games_url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    games_params = {
        "key": api_key,
        "steamid": steam_id,
        "format": "json",
        "include_appinfo": True,
        "include_played_free_games": True,
    }

    try:
        response = requests.get(games_url, params=games_params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("response", {}).get("games", [])
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error fetching Steam games: {e}")
        return []


def fetch_steam_achievements(
    markata: "Markata", app_id: int, api_key: str, steam_id: str
) -> Optional[SteamGameData]:
    """Fetch achievements for a Steam game."""
    cache_path = get_cache_path(markata, app_id)
    config = markata.config.steam_achievements

    # Check cache first
    if is_cache_valid(cache_path, config.cache_duration):
        try:
            with open(cache_path, "r") as f:
                data = json.load(f)
            return SteamGameData(**data)
        except (json.JSONDecodeError, pydantic.ValidationError):
            pass  # Fall through to fetch fresh data

    # Fetch from Steam API
    try:
        # Get game schema
        schema_url = (
            f"https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/"
        )
        schema_params = {"key": api_key, "appid": app_id, "l": "english"}

        schema_response = requests.get(schema_url, params=schema_params, timeout=10)
        schema_response.raise_for_status()
        schema_data = schema_response.json()

        if "game" not in schema_data or "availableGameStats" not in schema_data["game"]:
            print(f"No achievement data found for app {app_id}")
            return None

        achievements_schema = schema_data["game"]["availableGameStats"].get(
            "achievements", []
        )

        # Get user achievements
        user_url = (
            f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/"
        )
        user_params = {
            "key": api_key,
            "appid": app_id,
            "steamid": steam_id,
            "l": "english",
        }

        user_response = requests.get(user_url, params=user_params, timeout=10)
        user_response.raise_for_status()
        user_data = user_response.json()

        user_achievements = user_data.get("playerstats", {}).get("achievements", [])

        achievements = []
        for user_ach in user_achievements:
            schema_ach = next(
                (
                    a
                    for a in achievements_schema
                    if a.get("name") == user_ach.get("apiname")
                ),
                {},
            )

            achieved_raw = user_ach.get("achieved")
            try:
                achievement_obj = SteamAchievement(
                    apiname=user_ach.get("apiname", ""),
                    achieved=int(achieved_raw) if achieved_raw is not None else 0,
                    unlocktime=user_ach.get("unlocktime"),
                    name=schema_ach.get("displayName", ""),
                    description=schema_ach.get("description", ""),
                    icon=schema_ach.get("icon", ""),
                    icongray=schema_ach.get("icongray", ""),
                )
                achievements.append(achievement_obj)
            except Exception as e:
                print(f"Error creating achievement object: {e}")
                # Fallback to minimal achievement object
                achievements.append(
                    SteamAchievement(
                        apiname=user_ach.get("apiname", ""),
                        achieved=int(achieved_raw) if achieved_raw is not None else 0,
                        unlocktime=user_ach.get("unlocktime"),
                        name=schema_ach.get("displayName", ""),
                        description=schema_ach.get("description", ""),
                    )
                )

        achievements = []
        for user_ach in user_achievements:
            schema_ach = next(
                (
                    a
                    for a in achievements_schema
                    if a.get("name") == user_ach.get("apiname")
                ),
                {},
            )

            # Debug: Log raw API data
            achieved_raw = user_ach.get("achieved")
            if app_id == 400:
                print(
                    f"DEBUG: Processing achievement - apiname: {user_ach.get('apiname')}, achieved raw value: {achieved_raw}, type: {type(achieved_raw)}"
                )

            try:
                # Debug: Validate the data before Pydantic model creation
                achieved_int = int(achieved_raw) if achieved_raw is not None else 0
                if app_id == 400:
                    print(
                        f"DEBUG: Before Pydantic - apiname: {user_ach.get('apiname')}, achieved_raw: {achieved_raw}, achieved_int: {achieved_int}"
                    )

                achievement_obj = SteamAchievement(
                    apiname=user_ach.get("apiname", ""),
                    achieved=achieved_int,
                    unlocktime=user_ach.get("unlocktime"),
                    name=schema_ach.get("displayName", ""),
                    description=schema_ach.get("description", ""),
                    icon=schema_ach.get("icon", ""),
                    icongray=schema_ach.get("icongray", ""),
                )
                if app_id == 400:
                    print(
                        f"DEBUG: Created SteamAchievement - apiname: {achievement_obj.apiname}, achieved: {achievement_obj.achieved}, type: {type(achievement_obj.achieved)}, model_dump: {achievement_obj.model_dump()}"
                    )
                achievements.append(achievement_obj)
            except Exception as e:
                print(f"ERROR creating achievement object: {e}")
                print(
                    f"ERROR details - apiname: {user_ach.get('apiname')}, achieved_raw: {achieved_raw}, type: {type(achieved_raw)}"
                )
                # Fallback to minimal achievement object
                try:
                    fallback_obj = SteamAchievement(
                        apiname=user_ach.get("apiname", ""),
                        achieved=int(achieved_raw) if achieved_raw is not None else 0,
                        unlocktime=user_ach.get("unlocktime"),
                        name=schema_ach.get("displayName", ""),
                        description=schema_ach.get("description", ""),
                    )
                    if app_id == 400:
                        print(
                            f"DEBUG: Fallback SteamAchievement created - achieved: {fallback_obj.achieved}"
                        )
                    achievements.append(fallback_obj)
                except Exception as fallback_e:
                    print(f"ERROR: Even fallback failed: {fallback_e}")
                    # Create absolutely minimal object
                    achievements.append(
                        SteamAchievement(
                            apiname=user_ach.get("apiname", "unknown"),
                            achieved=0,
                        )
                    )

        # Create game data
        total_achievements = len(achievements)
        unlocked_achievements = sum(1 for a in achievements if a.achieved)
        completion_percentage = (
            (unlocked_achievements / total_achievements * 100)
            if total_achievements > 0
            else 0
        )

        # Debug: Test different counting methods
        if app_id == 400:
            count_method1 = sum(1 for a in achievements if a.achieved)
            count_method2 = sum(1 for a in achievements if bool(a.achieved))
            count_method3 = sum(
                1
                for a in achievements
                if a.achieved is not None and int(a.achieved) > 0
            )
            count_method4 = sum(
                int(a.achieved) for a in achievements if a.achieved is not None
            )
            print(
                f"DEBUG: Counting methods - method1: {count_method1}, method2: {count_method2}, method3: {count_method3}, method4: {count_method4}"
            )

        unlocked_achievements = sum(1 for a in achievements if a.achieved)
        completion_percentage = (
            (unlocked_achievements / total_achievements * 100)
            if total_achievements > 0
            else 0
        )

        if app_id == 400:
            print(
                f"DEBUG: Portal summary - total: {total_achievements}, unlocked: {unlocked_achievements}, completion: {completion_percentage}%"
            )

        game_data = SteamGameData(
            appid=app_id,
            name=schema_data["game"].get("gameName", f"Game {app_id}"),
            achievements=achievements,
            total_achievements=total_achievements,
            unlocked_achievements=unlocked_achievements,
            completion_percentage=round(completion_percentage, 2),
        )

        # Cache the data
        with open(cache_path, "w") as f:
            json.dump(game_data.model_dump(), f, indent=2)

        return game_data

    except requests.RequestException as e:
        print(f"Error fetching Steam data for app {app_id}: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing Steam data for app {app_id}: {e}")
        return None


@hook_impl
def cli(app, markata):
    """CLI hook to create achievement posts before build."""

    @app.command()
    def steam_achievements():
        """Create Steam achievement posts from unlocked achievements."""
        steam_config = markata.config.get(
            "steam_achievements", SteamAchievementsConfig()
        )

        # Expand environment variables and load from .env if needed
        import os
        from pathlib import Path

        # Try to load .env file if it exists
        env_path = Path(".env")
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    if line.strip() and not line.startswith("#"):
                        key, value = line.strip().split("=", 1)
                        os.environ[key] = value

        api_key = (
            os.path.expandvars(steam_config.api_key) if steam_config.api_key else None
        )
        steam_id = (
            os.path.expandvars(steam_config.steam_id) if steam_config.steam_id else None
        )

        if (
            not api_key
            or not steam_id
            or api_key.startswith("${")
            or steam_id.startswith("${")
        ):
            print("❌ Steam API key or Steam ID not configured")
            print("Set environment variables and add to markata.toml:")
            print("[markata.steam_achievements]")
            print("api_key = '${STEAM_API_KEY}'")
            print("steam_id = '${STEAM_ID}'")
            return

        posts_dir = Path(steam_config.posts_dir)

        print("🎮 Fetching your Steam games and achievements...")

        # Get all games from user's Steam library
        games_url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
        games_params = {
            "key": api_key,
            "steamid": steam_id,
            "format": "json",
            "include_appinfo": True,
            "include_played_free_games": True,
        }

        try:
            games_response = requests.get(games_url, params=games_params, timeout=30)
            games_response.raise_for_status()
            games_data = games_response.json()

            if "response" not in games_data or "games" not in games_data["response"]:
                print("❌ No games found in Steam library")
                return

            games = games_data["response"]["games"]
            print(f"📚 Found {len(games)} games in your Steam library")

            total_posts_created = 0
            games_processed = 0

            for game in games:
                app_id = game.get("appid")
                game_name = game.get("name", f"Game {app_id}")

                if not app_id:
                    continue

                print(f"🎯 Processing: {game_name} (ID: {app_id})")
                steam_data = fetch_steam_achievements(
                    markata, app_id, api_key, steam_id
                )

                if steam_data and steam_data.achievements:
                    unlocked_count = 0
                    new_posts_count = 0
                    for achievement in steam_data.achievements:
                        if achievement.achieved:
                            unlocked_count += 1
                            created = create_achievement_post(
                                markata, steam_data, achievement, posts_dir
                            )
                            if created:
                                new_posts_count += 1
                                total_posts_created += 1

                    games_processed += 1

                    if new_posts_count > 0:
                        print(
                            f"  ✅ Created {new_posts_count} new achievement posts for {steam_data.name} ({unlocked_count} total unlocked)"
                        )
                    elif unlocked_count > 0:
                        print(
                            f"  ℹ️  {unlocked_count} achievements already have posts for {steam_data.name}"
                        )
                    else:
                        print(f"  ℹ️  No unlocked achievements for {steam_data.name}")
                else:
                    print(f"  ⚠️  No achievement data for {game_name}")

            print(
                f"\n🎉 Created {total_posts_created} achievement posts from {games_processed} games"
            )
            print(f"📁 Posts saved to: {posts_dir}")
            print("🔧 Run 'git add pages/steam' to commit new posts")

        except Exception as e:
            print(f"❌ Error fetching Steam games: {e}")
            print("Steam API might be temporarily unavailable. Try again later.")
            return


# @hook_impl
# def pre_render(markata: "Markata"):
#     """Load achievement data into posts during build (posts already created by CLI hook)."""
#     config = markata.config.steam_achievements
#
#     if not config.api_key or not config.steam_id:
#         return
#
#     for post in markata.filter("not skip"):
#         steam_config = post.get("steam")
#         if isinstance(steam_config, dict):
#             app_id = steam_config.get("app_id")
#             if isinstance(app_id, int) and app_id > 0:
#                 steam_data = fetch_steam_achievements(
#                     markata, app_id, config.api_key, config.steam_id
#                 )
#                 if steam_data:
#                     post.steam_achievements = steam_data


if __name__ == "__main__":
    f = __file__
