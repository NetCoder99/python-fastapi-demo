import logging
import time

class LogCache(logging.Handler):
    _instance = None
    cntr = 0
    log_records = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LogCache, cls).__new__(cls)
        return cls._instance

    def emit(self, record: logging.LogRecord):
        self.log_records.append(record)
        print(f'emit::logRecord:{record}')

    @classmethod
    def getLogRecords(self):
        return self.log_records

    @classmethod
    def clearAllLogRecords(self):
        return self.log_records.clear()