import asyncio
from pathlib import Path
import time
from datetime import datetime
from fastapi import FastAPI, Request
from app.logging_utils.logging_cache import LogCache
from app.logging_utils.logging_models import LogEntry
from app.logging_utils.logging_utils import test_logging_by_level
from app.service_calls.log_service import save_log_records
from app.service_calls.reddit_calls import get_reddit_top, get_reddit_top_async

app = FastAPI(
    title="Python Fast API Demo",
    version="1.0.0",
)

# ----------------------------------------------------------------------------------------
# need this for vs code to find sibling and child directories
# ----------------------------------------------------------------------------------------
import sys
sys.path.append("./")

# ----------------------------------------------------------------------------------------
# other misc app related logging imports
# ----------------------------------------------------------------------------------------
import logging
from   . logging_utils import logging_config
from   . database_utils import sqllite_demo

# ----------------------------------------------------------------------------------------
# configure the basic logging handlers, formatting, etc
# ----------------------------------------------------------------------------------------
logging_config.config()
logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

# ----------------------------------------------------------------------------------------
# session state research
# ----------------------------------------------------------------------------------------
log_cache = LogCache()

# ----------------------------------------------------------------------------------------
# add run-time to response 
# ----------------------------------------------------------------------------------------
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# ----------------------------------------------------------------------------------------
# FastApi test and research
# ----------------------------------------------------------------------------------------
@app.get("/")
async def root():
    log_cache.cntr = log_cache.cntr + 1
    msg={"message": "Hello World", "cntr": log_cache.cntr}
    log_entry = LogEntry('root', msg)
    logger.info(log_entry.toJSON())
    save_log_records(log_cache.log_records)
    log_cache.clearAllLogRecords()
    return log_entry  #msg  #{"message": "Hello World"}




# ----------------------------------------------------------------------------------------
# FastApi test and research
# ----------------------------------------------------------------------------------------
@app.get("/testLogging")
async def test_logging():
  try:
    test_logging_by_level("hello")
    logger.info(sqllite_demo.get_db_version())
    return {"message": "Logging Test Completed Ok"}
  except Exception as ex:
    print("Error while executing applicaiton", ex)
    logger.exception("error trapped by main:{}".format(ex))


# ----------------------------------------------------------------------------------------
@app.get("/fetchIdeas")
def fetch_ideas() -> dict:
  try:
    data: dict = {}  # 3
    get_reddit_top("recipes", data)
    get_reddit_top("easyrecipes", data)
    get_reddit_top("TopSecretRecipes", data)
    return data
  except Exception as ex:
    print("Error while executing applicaiton", ex)
    logger.exception("error trapped by main:{}".format(ex))


# ----------------------------------------------------------------------------------------
@app.get("/fetchIdeas/async")
async def fetch_ideas_async() -> dict:
  try:
    data: dict = {}
    await asyncio.gather(  # 5
        get_reddit_top_async("recipes", data),
        get_reddit_top_async("easyrecipes", data),
        get_reddit_top_async("TopSecretRecipes", data),
    )
    return data
  except Exception as ex:
    print("Error while executing applicaiton", ex)
    logger.exception("error trapped by main:{}".format(ex))
