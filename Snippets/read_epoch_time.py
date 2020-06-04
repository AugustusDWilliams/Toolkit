import time


def get_readable_date(epoch):
    return time.strftime("%a %-d %b %Y %H:%M", time.gmtime(epoch))


get_readable_date(12345)
