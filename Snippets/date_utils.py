from datetime import date
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, WEEKLY, WE, TH
from pprint import pprint as pp


def parse_datetime_strings():
    log_line = 'INFO 2014-07-03T23:27:51 supybot Shutdown complete.'
    log_line_alt = 'INFO 2014-07-03T11:27:51AM supybot Shutdown complete.'
    print(parse(log_line, fuzzy=True))
    print(parse(log_line_alt, fuzzy=True))


def advanced_timedelta():
    today = date.today()
    birthday = date(year=1989, month=9, day=22)
    diff = relativedelta(today, birthday)
    print(diff)
    print(diff.years)
    print(diff.months)

def schedule_quality_meetings():
    next_thursday = date.today() + relativedelta(weekday=TH(+1))
    print(next_thursday)
    meetings = list(rrule(WEEKLY, count=10, dtstart=next_thursday))
    pp(meetings)


if __name__ == "__main__":
    parse_datetime_strings()
    advanced_timedelta()
    schedule_quality_meetings()
