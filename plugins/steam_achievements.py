"""
steam_achievements - Fetch Steam game achievements and create posts for each achievement and game

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

The plugin will:
- Create individual posts for each achievement when unlocked
- Create game posts with all achievements and cross-linking
- Link achievements back to their game pages

# CLI Commands

- `markata steam_achievements` - Create achievement posts from unlocked achievements
- `markata steam_games` - Create game posts with all achievements and cross-linking

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
    last_played: Optional[int] = None
    playtime_forever: Optional[int] = None
    playtime_2weeks: Optional[int] = None
    description: Optional[str] = None
    developers: Optional[List[str]] = None
    publishers: Optional[List[str]] = None

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


def create_game_post(
    markata: "Markata",
    game_data: SteamGameData,
    posts_dir: Path,
) -> bool:
    """Create a comprehensive markdown post for a Steam game with all achievements."""
    # Create safe filename for game
    safe_game_name = "".join(
        c for c in game_data.name if c.isalnum() or c in (" ", "-", "_")
    ).rstrip()
    safe_game_name = safe_game_name.replace(" ", "-").lower()

    # Create filename and path
    filename = f"{safe_game_name}.md"
    filepath = posts_dir / filename

    # Generate game page URL
    game_url = f"/{safe_game_name}/"

    # Separate unlocked and locked achievements
    unlocked = [a for a in game_data.achievements if a.achieved]
    locked = [a for a in game_data.achievements if not a.achieved]

    # Fetch game images from Steam store API
    header_image_url = (
        f"https://cdn.akamai.steamstatic.com/steam/apps/{game_data.appid}/header.jpg"
    )
    library_image_url = f"https://cdn.akamai.steamstatic.com/steam/apps/{game_data.appid}/library_600x900.jpg"

    # Format playtime
    playtime_hours = (
        round(game_data.playtime_forever / 60, 1) if game_data.playtime_forever else 0
    )
    last_played_date = (
        datetime.fromtimestamp(game_data.last_played, tz=timezone.utc).strftime(
            "%Y-%m-%d"
        )
        if game_data.last_played
        else None
    )

    # Write post content with properly quoted frontmatter
    post_date = last_played_date or datetime.now().strftime("%Y-%m-%d")
    content = f"""---
title: "{json.dumps(game_data.name).replace('"', "")}"
description: "Steam achievements and progress for {
        json.dumps(game_data.name).replace('"', "")
    } - {game_data.completion_percentage}% complete with {
        game_data.unlocked_achievements
    }/{game_data.total_achievements} achievements unlocked."
date: "{post_date}"
templateKey: steam_game
steam:
  game: "{json.dumps(game_data.name).replace('"', "")}"
  app_id: {game_data.appid}
  total_achievements: {game_data.total_achievements}
  unlocked_achievements: {game_data.unlocked_achievements}
  completion_percentage: {game_data.completion_percentage}
  playtime_hours: {playtime_hours}
  last_played: "{last_played_date}"
  description: "{json.dumps(game_data.description or "").replace('"', "")}"
  developers: {json.dumps(game_data.developers or [])}
  publishers: {json.dumps(game_data.publishers or [])}
tags: {json.dumps(["steam", "game", safe_game_name])}
url: "{game_url}"
slug: "steam/{safe_game_name}"
---

<style>
.game-header {{
  display: flex;
  align-items: flex-start;
  gap: 30px;
  margin: 30px 0;
  padding: 20px;
  background: #1a1a1a;
  border-radius: 12px;
  border: 1px solid #333;
}}

.game-header img {{
  width: 200px;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border: 1px solid #333;
  flex-shrink: 0;
}}

.game-info {{
  flex: 1;
}}

.game-info h1 {{
  margin: 0 0 15px 0;
  color: #fff;
  font-size: 2em;
}}

.game-info p {{
  margin: 0 0 15px 0;
  color: #ccc;
  line-height: 1.5;
}}

.game-info .developers {{
  font-size: 0.9em;
  color: #999;
}}

.game-links {{
  margin-top: 20px;
}}

.game-links a {{
  display: inline-block;
  margin-right: 15px;
  padding: 8px 12px;
  background: #2a2a2a;
  color: #fff;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9em;
  transition: background-color 0.2s ease;
}}

.game-links a:hover {{
  background: #3a3a3a;
  color: #4caf50;
}}

.steam-game-progress {{
  background: #1a1a1a;
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
  border: 1px solid #333;
}}

.stats-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin: 20px 0;
}}

.stat-card {{
  background: #2a2a2a;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  border: 1px solid #444;
}}

.stat-card h3 {{
  margin: 0 0 15px 0;
  color: #4caf50;
  font-size: 1.1em;
}}

.stat-value {{
  font-size: 2em;
  font-weight: bold;
  color: #fff;
  margin: 10px 0;
}}

.stat-card p {{
  margin: 10px 0 0 0;
  color: #ccc;
  font-size: 0.9em;
}}

.progress-bar {{
  width: 100%;
  height: 24px;
  background: #2a2a2a;
  border-radius: 12px;
  overflow: hidden;
  margin: 10px 0;
  position: relative;
}}

.progress-fill {{
  height: 100%;
  background: linear-gradient(90deg, #4caf50, #8bc34a);
  border-radius: 12px;
  transition: width 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 12px;
}}

.achievements-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(60px, 1fr));
  gap: 8px;
  margin: 20px 0;
}}

.achievement-item {{
  position: relative;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s ease;
}}

.achievement-item:hover {{
  transform: scale(1.1);
  z-index: 10;
}}

.achievement-icon-wrapper {{
  display: inline-block;
  padding: 2px;
}}

.achievement-icon {{
  width: 40px;
  height: 40px;
  border-radius: 6px;
  border: 2px solid #444;
  transition: border-color 0.2s ease;
}}

.achievement-item.unlocked .achievement-icon {{
  border-color: #4caf50;
  box-shadow: 0 0 10px rgba(76, 175, 80, 0.3);
}}

.achievement-item.locked .achievement-icon {{
  filter: grayscale(100%);
  opacity: 0.6;
}}

.achievement-tooltip {{
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.95);
  color: white;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 12px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
  z-index: 100;
  margin-bottom: 5px;
  max-width: 200px;
  white-space: normal;
  text-align: center;
}}

.achievement-item:hover .achievement-tooltip {{
  opacity: 1;
}}

.achievement-section {{
  background: #1a1a1a;
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
  border: 1px solid #333;
}}

.achievement-section h2 {{
  margin-top: 0;
  color: #fff;
}}
</style>

<div class="game-header">
  <img src="{library_image_url}" alt="{game_data.name} box art" loading="lazy" 
       onerror="this.src='{header_image_url}'">
  <div class="game-info">
    <h1>{game_data.name}</h1>
    {f"<p><em>{game_data.description}</em></p>" if game_data.description else ""}
    {
        f'<p class="developers">Developed by {", ".join(game_data.developers[:2])}{"..." if len(game_data.developers) > 2 else ""}</p>'
        if game_data.developers
        else ""
    }
    <div class="game-links">
      <a href="https://store.steampowered.com/app/{
        game_data.appid
    }/" target="_blank" rel="noopener noreferrer">🛒 Steam Store</a>
      <a href="https://steamcommunity.com/app/{
        game_data.appid
    }/" target="_blank" rel="noopener noreferrer">💬 Community</a>
    </div>
  </div>
</div>

<div class="steam-game-progress">
## 🎮 Game Progress & Stats

<div class="stats-grid">
  <div class="stat-card">
    <h3>Achievements</h3>
    <div class="progress-bar">
      <div class="progress-fill" style="width: {game_data.completion_percentage}%">
        {game_data.completion_percentage}%
      </div>
    </div>
    <p>{game_data.unlocked_achievements}/{game_data.total_achievements} Unlocked</p>
  </div>
  
  <div class="stat-card">
    <h3>Playtime</h3>
    <div class="stat-value">{playtime_hours}h</div>
    <p>Total hours played</p>
  </div>
  
  {
        f'''<div class="stat-card">
    <h3>Last Played</h3>
    <div class="stat-value">{last_played_date}</div>
    <p>Most recent session</p>
  </div>'''
        if last_played_date
        else ""
    }
</div>
</div>

"""

    # Add unlocked achievements grid
    if unlocked:
        content += f"""
<div class="achievement-section">
<h2>🏆 Unlocked Achievements ({len(unlocked)})</h2>

<div class="achievements-grid">
"""
        for achievement in unlocked:
            unlock_date = (
                datetime.fromtimestamp(achievement.unlocktime, tz=timezone.utc)
                if achievement.unlocktime
                else None
            )
            date_str = unlock_date.strftime("%Y-%m-%d") if unlock_date else "unknown"
            achievement_safe_name = (
                "".join(
                    c
                    for c in (achievement.name or "")
                    if c.isalnum() or c in (" ", "-", "_")
                )
                .rstrip()
                .replace(" ", "-")
                .lower()
                if achievement.name
                else "achievement"
            )
            achievement_filename = (
                f"{date_str}-{safe_game_name}-{achievement_safe_name}.md"
            )
            achievement_url = f"/steam/{achievement_filename.replace('.md', '/')}"

            badge_url = achievement.icon or ""
            unlock_date_str = (
                unlock_date.strftime("%B %d, %Y") if unlock_date else "Unknown date"
            )

            content += f"""
<div class="achievement-item unlocked">
  <span class="achievement-icon-wrapper">
    <img src="{badge_url}" alt="{achievement.name}" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>{achievement.name or "Unknown Achievement"}</strong><br>
    {achievement.description or "No description"}<br>
    <small>Unlocked: {unlock_date_str}</small>
  </div>
</div>"""

        content += """
</div>
</div>
"""

    # Add locked achievements grid
    if locked:
        content += f"""
<div class="achievement-section">
<h2>🔒 Locked Achievements ({len(locked)})</h2>

<div class="achievements-grid">
"""
        for achievement in locked:
            badge_url = achievement.icongray or achievement.icon or ""

            content += f"""
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="{badge_url}" alt="{achievement.name}" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>{achievement.name or "Unknown Achievement"}</strong><br>
    {achievement.description or "No description"}
  </div>
</div>"""

        content += """
</div>
</div>
"""

    content += """
---

*Game data automatically imported from Steam. Achievement links will be created as individual posts when achievements are unlocked.*
"""

    # Ensure posts directory exists
    posts_dir.mkdir(parents=True, exist_ok=True)

    # Write the file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created game post: {filepath}")
    return True


def create_achievement_post(
    markata: "Markata",
    game_data: SteamGameData,
    achievement: SteamAchievement,
    posts_dir: Path,
) -> bool:
    """Create a markdown post for an individual achievement."""
    if not achievement.achieved or not achievement.unlocktime:
        return False  # Only create posts for unlocked achievements

    # Convert unlock timestamp to date
    unlock_date = datetime.fromtimestamp(achievement.unlocktime, tz=timezone.utc)
    date_str = unlock_date.strftime("%Y-%m-%d")

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

    # Generate game page URL for cross-linking
    game_url = f"/{safe_game_name}/"

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
title: "{json.dumps(achievement.name or f"Achievement in {game_data.name}").replace('"', "")}"
description: "{game_data.name}: {json.dumps(achievement.description or "").replace('"', "")}"
date: "{date_str}"
templateKey: steam_achievement
steam:
  game: "{json.dumps(game_data.name).replace('"', "")}"
  app_id: {game_data.appid}
  achievement:
    name: "{json.dumps(achievement.name or "").replace('"', "")}"
    description: "{json.dumps(achievement.description or "").replace('"', "")}"
    api_name: "{json.dumps(achievement.apiname).replace('"', "")}"
    unlock_time: "{achievement.unlocktime}"
    unlock_date: "{json.dumps(unlock_date.isoformat()).replace('"', "")}"
    icon: "{json.dumps(achievement.icon or "").replace('"', "")}"
    icongray: "{json.dumps(achievement.icongray or "").replace('"', "")}"
tags: {json.dumps(["steam", "achievement", safe_game_name])}
slug: "steam/{safe_achievement_name}"
---

{badge_html}

{achievement.description or ""}

Unlocked in **[{game_data.name}]({game_url})** on {unlock_date.strftime("%B %d, %Y at %I:%M %p")}.

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
    markata: "Markata",
    app_id: int,
    api_key: str,
    steam_id: str,
    game_data: Optional[Dict] = None,
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
            print(f"DEBUG: Processing achievement '{user_ach.get('apiname')}'")
            print(
                f"DEBUG: Raw API achieved field: {achieved_raw} (type: {type(achieved_raw)})"
            )
            print(f"DEBUG: Full user achievement data: {user_ach}")

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
                print(f"DEBUG: Created SteamAchievement object:")
                print(f"  - apiname: {achievement_obj.apiname}")
                print(
                    f"  - achieved: {achievement_obj.achieved} (type: {type(achievement_obj.achieved)})"
                )
                print(f"  - name: {achievement_obj.name}")
                print(f"  - unlocktime: {achievement_obj.unlocktime}")
                achievements.append(achievement_obj)
            except Exception as e:
                print(f"ERROR: Failed to create achievement object: {e}")
                print(f"ERROR: Exception details: {type(e).__name__}: {e}")
                # Fallback to minimal achievement object
                try:
                    fallback_obj = SteamAchievement(
                        apiname=user_ach.get("apiname", ""),
                        achieved=int(achieved_raw) if achieved_raw is not None else 0,
                        unlocktime=user_ach.get("unlocktime"),
                        name=schema_ach.get("displayName", ""),
                        description=schema_ach.get("description", ""),
                    )
                    print(f"DEBUG: Created fallback SteamAchievement object:")
                    print(f"  - apiname: {fallback_obj.apiname}")
                    print(
                        f"  - achieved: {fallback_obj.achieved} (type: {type(fallback_obj.achieved)})"
                    )
                    achievements.append(fallback_obj)
                except Exception as fallback_e:
                    print(f"ERROR: Fallback object creation also failed: {fallback_e}")

        # Create game data
        total_achievements = len(achievements)
        print(f"DEBUG: Final achievement list processing:")
        print(f"DEBUG: Total achievements objects created: {total_achievements}")

        unlocked_achievements = 0
        for i, a in enumerate(achievements):
            print(
                f"DEBUG: Achievement {i + 1}: {a.name} - achieved: {a.achieved} (type: {type(a.achieved)})"
            )
            if a.achieved:
                unlocked_achievements += 1

        print(f"DEBUG: Final counted unlocked achievements: {unlocked_achievements}")
        completion_percentage = (
            (unlocked_achievements / total_achievements * 100)
            if total_achievements > 0
            else 0
        )

        # Extract additional game metadata
        last_played = game_data.get("rtime_last_played") if game_data else None
        playtime_forever = game_data.get("playtime_forever") if game_data else None
        playtime_2weeks = game_data.get("playtime_2weeks") if game_data else None

        # Try to extract description and developers from schema data
        game_info = schema_data.get("game", {})
        description = None
        developers = []
        publishers = []

        # Check for description in multiple possible locations
        if "about" in game_info:
            description = game_info["about"].get("short_description") or game_info[
                "about"
            ].get("description")
        elif "description" in game_info:
            description = game_info["description"]

        # Check for developers and publishers
        if "developers" in game_info:
            developers = [
                dev.get("name", "")
                for dev in game_info["developers"]
                if isinstance(dev, dict)
            ]
        elif "developer" in game_info:
            developers = (
                [game_info["developer"]]
                if isinstance(game_info["developer"], str)
                else []
            )

        if "publishers" in game_info:
            publishers = [
                pub.get("name", "")
                for pub in game_info["publishers"]
                if isinstance(pub, dict)
            ]
        elif "publisher" in game_info:
            publishers = (
                [game_info["publisher"]]
                if isinstance(game_info["publisher"], str)
                else []
            )

        steam_game_data = SteamGameData(
            appid=app_id,
            name=schema_data["game"].get("gameName", f"Game {app_id}"),
            achievements=achievements,
            total_achievements=total_achievements,
            unlocked_achievements=unlocked_achievements,
            completion_percentage=round(completion_percentage, 2),
            last_played=last_played,
            playtime_forever=playtime_forever,
            playtime_2weeks=playtime_2weeks,
            description=description,
            developers=developers,
            publishers=publishers,
        )

        # Cache the data
        with open(cache_path, "w") as f:
            json.dump(steam_game_data.model_dump(), f, indent=2)

        return steam_game_data

    except requests.RequestException as e:
        print(f"Error fetching Steam data for app {app_id}: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing Steam data for app {app_id}: {e}")
        return None


def create_steam_game_posts(
    markata: "Markata", api_key: str, steam_id: str, posts_dir: Path
) -> int:
    """Create game posts for all Steam games with achievements."""
    print("🎮 Creating Steam game posts...")

    # Get all games from user's Steam library
    games = get_steam_games(api_key, steam_id)
    if not games:
        print("❌ No games found in Steam library")
        return 0

    game_posts_created = 0

    for game in games:
        app_id = game.get("appid")
        game_name = game.get("name", f"Game {app_id}")

        if not app_id:
            continue

        print(f"🎯 Processing game: {game_name} (ID: {app_id})")
        steam_data = fetch_steam_achievements(markata, app_id, api_key, steam_id, game)

        if steam_data and steam_data.achievements:
            created = create_game_post(markata, steam_data, posts_dir)
            if created:
                game_posts_created += 1
        else:
            print(f"  ⚠️  No achievement data for {game_name}")

    return game_posts_created


@hook_impl
def cli(app, markata):
    """CLI hook to create achievement and game posts before build."""

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
                    markata, app_id, api_key, steam_id, game
                )

                if steam_data and steam_data.achievements:
                    print(f"DEBUG: CLI counting for {steam_data.name}:")
                    print(
                        f"DEBUG: Total achievements in steam_data: {len(steam_data.achievements)}"
                    )
                    print(
                        f"DEBUG: steam_data.unlocked_achievements: {steam_data.unlocked_achievements}"
                    )

                    unlocked_count = 0
                    new_posts_count = 0
                    for i, achievement in enumerate(steam_data.achievements):
                        print(
                            f"DEBUG: CLI Achievement {i + 1}: {achievement.name} - achieved: {achievement.achieved} (type: {type(achievement.achieved)})"
                        )
                        if achievement.achieved:
                            unlocked_count += 1
                            created = create_achievement_post(
                                markata, steam_data, achievement, posts_dir
                            )
                            if created:
                                new_posts_count += 1
                                total_posts_created += 1

                    print(f"DEBUG: CLI final unlocked count: {unlocked_count}")
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

    @app.command()
    def steam_games():
        """Create Steam game posts with all achievements and cross-linking."""
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

        try:
            game_posts_created = create_steam_game_posts(
                markata, api_key, steam_id, posts_dir
            )
            print(f"\n🎉 Created {game_posts_created} game posts")
            print(f"📁 Posts saved to: {posts_dir}")
            print("🔧 Run 'git add pages/steam' to commit new posts")

        except Exception as e:
            print(f"❌ Error creating game posts: {e}")
            return


if __name__ == "__main__":
    f = __file__
