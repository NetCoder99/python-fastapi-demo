import sys

from app.logging_utils.logging_cache import LogCache
sys.path.append("./")
import logging

from app.logging_utils.logging_handler import get_file_handler, get_db_handler

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-9s - %(message)s')

def config():
  logger = logging.getLogger("app_logger")

  cache_handler = LogCache()
  logger.addHandler(cache_handler)


  consoleHandler = logging.StreamHandler()
  consoleHandler.setFormatter(formatter)
  logger.addHandler(consoleHandler)

  logger.addHandler(get_file_handler("debug_handler",    "debug.log",    formatter, logging.DEBUG, file_mode="w"))
  logger.addHandler(get_file_handler("info_handler",     "info.log",     formatter, logging.INFO, file_mode="w"))
  logger.addHandler(get_file_handler("warning_handler",  "warning.log",  formatter, logging.WARNING, file_mode="w"))
  logger.addHandler(get_file_handler("error_handler",    "error.log",    formatter, logging.ERROR, file_mode="w"))
  logger.addHandler(get_file_handler("critical_handler", "critical.log", formatter, logging.CRITICAL, file_mode="w"))

  #logger.addHandler(get_db_handler("debug_handler",    "debug.log",    formatter, logging.DEBUG, file_mode="w"))


  #debug_handler = logging.FileHandler("debug.log", mode="w")
  #debug_handler.setLevel(logging.DEBUG)
  #debug_handler.setFormatter(formatter)
  #info_handler = logging.FileHandler("info.log", mode="w")
  #info_handler.setLevel(logging.INFO)
  #info_handler.setFormatter(formatter)
  #warning_handler = logging.FileHandler("warning.log", mode="w")
  #warning_handler.setLevel(logging.WARNING)
  #warning_handler.setFormatter(formatter)
  #error_handler = logging.FileHandler("error.log", mode="w")
  #error_handler.setLevel(logging.ERROR)
  #error_handler.setFormatter(formatter)
  #critical_handler = logging.FileHandler("critical.log", mode="w")
  #critical_handler.setLevel(logging.CRITICAL)
  #critical_handler.setFormatter(formatter)

  #logger.addHandler(debug_handler)
  #logger.addHandler(info_handler)
  #logger.addHandler(warning_handler)
  #logger.addHandler(error_handler)
  #logger.addHandler(critical_handler)

