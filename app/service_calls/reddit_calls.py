from datetime import datetime
import json
import logging
import httpx
from app.logging_utils.logging_utils import LogUtils
from app.logging_utils.logging_models import LogEntry


logger = logging.getLogger("app_logger")

# ----------------------------------------------------------------------------------------
def get_reddit_top(subreddit: str, data: dict) -> None:
    LogUtils.info(LogEntry(__name__, {"message": "started"}))

    response = httpx.get(
        f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5",
        headers={"User-agent": "recipe bot 0.1"},
    )  # 2
    subreddit_recipes = response.json()
    subreddit_data = []
    for entry in subreddit_recipes["data"]["children"]:
        score = entry["data"]["score"]
        title = entry["data"]["title"]
        link = entry["data"]["url"]
        subreddit_data.append(f"{str(score)}: {title} ({link})")
    data[subreddit] = subreddit_data
    LogUtils.debug(LogEntry(__name__, subreddit_recipes))
    LogUtils.info (LogEntry(__name__, {"message": "finished"}))


# ----------------------------------------------------------------------------------------
async def get_reddit_top_async(subreddit: str, data: dict) -> None:  # 2
    async with httpx.AsyncClient() as client:  # 3
        response = await client.get(  # 4
            f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5",
            headers={"User-agent": "recipe bot 0.1"},
        )

    subreddit_recipes = response.json()
    subreddit_data = []
    for entry in subreddit_recipes["data"]["children"]:
        score = entry["data"]["score"]
        title = entry["data"]["title"]
        link = entry["data"]["url"]
        subreddit_data.append(f"{str(score)}: {title} ({link})")
    data[subreddit] = subreddit_data