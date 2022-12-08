from datetime import datetime
import logging

from app.logging_utils.logging_models import LogEntry

logger = logging.getLogger("app_logger")

# ----------------------------------------------------------------------------------------
# test the logging handlers 
# ----------------------------------------------------------------------------------------
def test_logging_by_level(msg):
  logger.debug   ("debug    - test:{}".format(msg))
  logger.info    ("info     - test:{}".format(msg))
  logger.warning ("warning  - test:{}".format(msg))
  logger.error   ("error    - test:{}".format(msg))
  logger.critical("critical - test:{}".format(msg))

class LogUtils:
  def debug(msg: LogEntry):
    msg.log_level = "DEBUG"
    msg.date_time = datetime.now().isoformat()
    logger.debug(msg.toJSON())

  def info(msg: LogEntry):
    msg.log_level = "INFO"
    msg.date_time = datetime.now().isoformat()
    logger.info(msg.toJSON())

  def warning(msg: LogEntry):
    msg.log_level = "WARNING"
    msg.date_time = datetime.now().isoformat()
    logger.warning(msg.toJSON())

  def error(msg: LogEntry):
    msg.log_level = "ERROR"
    msg.date_time = datetime.now().isoformat()
    logger.error(msg.toJSON())

  def critical(msg: LogEntry):
    msg.log_level = "CRITICAL"
    msg.date_time = datetime.now().isoformat()
    logger.critical(msg.toJSON())
