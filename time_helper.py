"""
时间转换类
"""

import time
from datetime import datetime


# 将python的datetime转换为unix时间戳
def datetime_to_timemill(date_time):
    if datetime:
        timemill = time.mktime(date_time.timetuple());
        print("timemill:", timemill)
        print("timestample:", date_time.timestamp())
        return timemill
    else:
        return datetime_to_timemill(datetime.now())


# 将unix时间戳转换为python的datetime
def timemill_to_datetime(unix_ts):
    if unix_ts > 0:
        return datetime.fromtimestamp(unix_ts)
    else:
        return datetime.now()
