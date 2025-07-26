class Maths:
    @staticmethod
    def is_leap(year: int) -> bool:
        """Return True if a given year is a leap year."""
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

class ImperiumTime(Maths):
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self):
        pass

    def epoch_to_imperium(self, seconds: int, detailed: bool = False):
        if seconds < 0:
            raise ValueError("Negative epoch time not supported (use Centurian module).")

        year = 1970
        # Reduce seconds by whole years
        while seconds >= (365 + self.is_leap(year)) * 86400:
            seconds -= (365 + self.is_leap(year)) * 86400
            year += 1

        yy = year - 1970
        month = 0

        for days in self.DAYS_IN_MONTH:
            # Handle leap year February
            days_in_this_month = days + (month == 1 and self.is_leap(year))
            if seconds < days_in_this_month * 86400:
                break
            seconds -= days_in_this_month * 86400
            month += 1

        day = (seconds // 86400) + 1
        seconds %= 86400
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        sec = seconds % 60

        if detailed:
            return {
                "yy": yy,
                "m": month + 1,
                "d": day,
                "h": hours,
                "min": minutes,
                "sec": sec,
                "ir": f"{yy:02}{month+1:02}{day:02}_{hours:02}{minutes:02}{sec:02}"
            }
        else:
            return f"{yy:02}{month+1:02}{day:02}_{hours:02}{minutes:02}{sec:02}"

    def imperium_to_epoch(self, imperium: int) -> int:
        """Convert an Imperium timestamp (YYMMDD_HHMMSS-like integer) back to Unix epoch seconds."""
        parts = []
        temp = imperium
        for _ in range(6):
            parts.append(temp % 100)
            temp //= 100
        # Map: [sec, min, hour, day, month, year]
        sec, minute, hour, day, month, yy = parts
        current_year = 1970 + yy

        # Validate month/day
        if month < 1 or month > 12:
            raise ValueError("Invalid month.")
        max_day = self.DAYS_IN_MONTH[month - 1] + (month == 2 and self.is_leap(current_year))
        if day < 1 or day > max_day:
            raise ValueError("Invalid day for given month/year.")

        # Build total seconds
        seconds = sec + (minute * 60) + (hour * 3600)
        seconds += (day - 1) * 86400
        seconds += sum((self.DAYS_IN_MONTH[i] + (i == 1 and self.is_leap(current_year))) * 86400 for i in range(month - 1))
        seconds += sum((365 + self.is_leap(y)) * 86400 for y in range(1970, current_year))

        return seconds
