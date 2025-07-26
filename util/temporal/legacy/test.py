def epoch_to_date(epoch_seconds):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1970
    while epoch_seconds >= (365 + (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))) * 86400:
        epoch_seconds -= (365 + (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))) * 86400
        year += 1
    
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    month = 0
    while epoch_seconds >= (days_in_month[month] + (month == 1 and leap)) * 86400:
        epoch_seconds -= (days_in_month[month] + (month == 1 and leap)) * 86400
        month += 1

    day = epoch_seconds // 86400 + 1
    epoch_seconds %= 86400
    hour = epoch_seconds // 3600
    minute = (epoch_seconds % 3600) // 60
    second = epoch_seconds % 60
    YY=1970-year
    return [YY, month, day, hour, minute, second]
    
# # Example usage
# timestamp = 1714328714
# y, mo, d, h, mi, s = epoch_to_date(timestamp)
# print(f"{y}-{mo:02d}-{d:02d} {h:02d}:{mi:02d}:{s:02d}")


