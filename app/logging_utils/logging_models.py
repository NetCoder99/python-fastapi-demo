from datetime import datetime
import json
import logging

logger = logging.getLogger("app_logger")


class LogEntry:
    def __init__(self, module_name: str, message: any):
        self.date_time   = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.app_name    = "python-fastapi-demo"
        self.module_name = module_name
        self.log_level   = logging.getLevelName(logger.level)
        self.message     = message
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=None)