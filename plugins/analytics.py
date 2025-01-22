"""Analytics plugin for Markata"""

from markata.hookspec import hook_impl, register_attr
from matplotlib import pyplot as plt
import pandas as pd
from pathlib import Path
import pydantic
import seaborn as sns


class AnalyticsConfig(pydantic.BaseModel):
    output_dir: str = "analytics"
    contributions_max_post_scale: int = 5
    contributions_cmap: str = "rocket"


class Config(pydantic.BaseModel):
    analytics: AnalyticsConfig = AnalyticsConfig()


@hook_impl
@register_attr("post_models")
def config_model(markata: "Markata") -> None:
    markata.config_models.append(Config)


@hook_impl
def pre_render(markata: "Markata") -> None:
    output_dir = Path(markata.config.analytics.output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    post_dates = [post["date"] for post in markata.articles]
    post_dates.sort()

    # Contribution Graph as Heatmap
    df = pd.DataFrame(post_dates, columns=["date"])
    df["date"] = pd.to_datetime(df["date"])

    df["year"] = df["date"].dt.year
    df["week"] = df["date"].dt.isocalendar().week
    df["day_of_week"] = df["date"].dt.weekday

    all_weeks = range(1, 53)
    all_days = range(0, 7)

    day_labels = ["", "MON", "", "WED", "", "FRI", ""]
    month_labels = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]

    # Determine global vmax for all years
    overall_max_value = df.groupby(["day_of_week", "week"]).size().max()
    vmax = max(5, overall_max_value // 2)
    vmax = min(markata.config.analytics.contributions_max_post_scale, vmax)

    plt.style.use("dark_background")

    for year in df["year"].unique():
        fig, ax = plt.subplots(figsize=(15, 3))
        yearly_data = df[df["year"] == year]
        heatmap_data = (
            yearly_data.groupby(["day_of_week", "week"]).size().unstack(fill_value=0)
        )
        heatmap_data = heatmap_data.reindex(
            index=all_days, columns=all_weeks, fill_value=0
        )

        sns.heatmap(
            heatmap_data,
            cmap=markata.config.analytics.contributions_cmap,
            linewidths=3,
            linecolor="black",
            square=True,
            vmax=vmax,
            cbar=False,
            ax=ax,
        )
        ax.set_yticklabels(day_labels, rotation=0, color="white")
        ax.set_xticks([i * 4 for i in range(13)])
        ax.set_xticklabels(month_labels, rotation=0, color="white")
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.tick_params(left=False, bottom=False)
        ax.set_title(f"Post Contributions in {year}", color="white", fontsize=16)

        # Add bottom scale with matching square sizes
        scale_data = pd.DataFrame(
            [[0, vmax * 0.33, vmax * 0.67, vmax]], index=[0], columns=range(4)
        )
        scale_ax = fig.add_axes([0.8, 0.1, 0.15, 0.05])
        sns.heatmap(
            scale_data,
            cmap=markata.config.analytics.contributions_cmap,
            linewidths=3,
            linecolor="black",
            square=True,
            ax=scale_ax,
            cbar=False,
        )
        scale_ax.set_xticks([])
        scale_ax.set_yticks([])
        scale_ax.set_title(f"{vmax} posts", color="white", fontsize=12, x=2, y=-0.2)
        scale_ax.axis("off")

        plt.savefig(
            output_dir / f"contributions_{year}.png",
            facecolor="black",
            bbox_inches="tight",
            pad_inches=0.1,
        )
        plt.savefig(
            output_dir / f"contributions_{year}.svg",
            facecolor="black",
            bbox_inches="tight",
            pad_inches=0.1,
        )
        plt.close()
