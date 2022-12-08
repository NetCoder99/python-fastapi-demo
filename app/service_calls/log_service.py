# ----------------------------------------------------------------------------------------
from logging import LogRecord
from typing import List

def save_log_records(log_records:List[LogRecord]):
    print('=======================================================================')
    for log_rec in log_records:
        print(f'msg::{log_rec.msg}')
