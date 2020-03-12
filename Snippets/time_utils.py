import re
from datetime import datetime, timedelta
from datetime import time as time_class


def calc_duration(time_val, units='s'):
    """Calculates the duration of the given time value in seconds

    Parameters:
        time_val (int): The amount of time to calculate the duration of
        units (str): The time unit of the given time value in hours, minutes, or seconds.
            (default is 's' for seconds)

    Returns:
        tuple: a tuple of the duration represented in hours, minutes, and seconds
    """
    time_val = float(time_val)
    if units == 'm' or units == 'mins':
        time_val *= 60
    elif time_val == "h" or units == 'hours':
        time_val *= 3600
    hours = int(time_val // 3600)
    minutes = int(time_val // 60)
    seconds = int(time_val % 60)
    return hours, minutes, seconds


def calc_time_remaining(end_time, units="s"):
    time_diff = end_time - datetime.now()
    total_time = time_diff.seconds
    if units == "h":
        total_time = int(total_time * 3600)
    elif units == "m":
        total_time = int(total_time * 60)
    elif units == 's':
        total_time = int(total_time)
    else:
        raise AttributeError("units argument must be h, m, or s")
    hours = int(total_time // 3600)
    minutes = int(total_time % 3600 // 60)
    seconds = int(total_time % 60)
    time_remaining = time_class(hours, minutes, seconds)
    return time_remaining


def create_time_string(time_obj):
    hours = time_obj.hour
    minutes = time_obj.minute
    seconds = time_obj.second
    if hours > 0:
        time_str = "{} Hours {} Minutes {} Seconds".format(
            hours, minutes, seconds)
    elif minutes > 0:
        time_str = "{} Minutes {} Seconds".format(minutes, seconds)
    # elif seconds > 0:
    else:
        time_str = "{} Seconds".format(seconds)
    return time_str


def parse_time_string(time_str):
    hour_regex = r"\d+(?=\sHour)"
    minute_regex = r"\d+(?=\sMinute*)"
    second_regex = r"\d+(?=\sSecond*)"
    hour_match = re.findall(hour_regex, time_str)
    minute_match = re.findall(minute_regex, time_str)
    second_match = re.findall(second_regex, time_str)
    if hour_match:
        hours = int(hour_match[0]) * 3600
    else:
        hours = 0
    if minute_match:
        minutes = int(minute_match[0]) * 60
    else:
        minutes = 0
    if second_match:
        seconds = int(second_match[0])
    else:
        seconds = 0
    time_obj = time_class(hours, minutes, seconds)
    return time_obj
# ------------------------Reference---------------------------------

if __name__ == "__main__":
    duration = calc_duration(64, "mins")
    end_time = datetime.now() + timedelta(seconds=10)
    tr = calc_time_remaining(end_time)
    time_str = create_time_string(tr)
    time_obj = parse_time_string(time_str)
    print("Duration:", duration)
    print("Time Remaining:", tr)
    print("Time String:", time_str)
    print("Time Object:", time_obj)
