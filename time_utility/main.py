# Python
from datetime import datetime, timedelta, date
from calendar import monthrange
from typing import Tuple

# Third Party
import pytz

# This Package
from .week import TimeUtilityWeek


class TimeUtility:
    """Date and Time utility functions"""

    # Period Constants
    DAILY = "daily"
    MONTHLY = "monthly"
    ANNUAL = "annual"

    # Time Unit Constants
    MICROSECOND = "microsecond"
    SECOND = "second"
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"

    @staticmethod
    def is_naive(target_datetime: datetime) -> bool:
        """
        Checks if the given datetime object is naive or not

        :param target_datetime: The target datetime object to be checked
        """
        return target_datetime.tzinfo is None

    @staticmethod
    def is_aware(target_datetime: datetime) -> bool:
        """
        Checks if the given datetime object is aware or not

        :param target_datetime: The target datetime object to be checked
        """
        return target_datetime.tzinfo is not None

    @staticmethod
    def make_aware(target_datetime: datetime, timezone=pytz.utc) -> datetime:
        """
        Return a new datetime object with the timezone information

        :param target_datetime: The target datetime object
        :param timezone: The target timezone. The default value is UTC
        """
        return target_datetime.replace(tzinfo=timezone)

    @staticmethod
    def now(timezone=pytz.utc) -> datetime:
        """
        Returns the current date and time with the given time zone

        :param timezone: The desired timezone, defaults to UTC
        """
        return datetime.now(tz=timezone)

    @staticmethod
    def today(timezone=pytz.utc) -> date:
        """
        Returns the current date with the given timezone

        :param timezone: The desired timezone, defaults to UTC
        """
        return datetime.now(tz=timezone).date()

    @staticmethod
    def get_date_start(timezone=pytz.utc, year: int = None, month: int = None, day: int = None) -> datetime:
        """
        Returns the date and time of the beginning of the day with the given timezone

        :param timezone: The desired timezone, defaults to UTC
        :param year: The target year, ignore or pass None to use the current year
        :param month: The target month, ignore or pass None to use the current month
        :param day: The target day, ignore or pass None to use the current day
        """
        return datetime.now(tz=timezone).replace(
            year=year if year is not None else datetime.now(tz=timezone).year,
            month=month if month is not None else datetime.now(tz=timezone).month,
            day=day if day is not None else datetime.now(tz=timezone).day,
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

    @staticmethod
    def get_date_end(timezone=pytz.utc, year: int = None, month: int = None, day: int = None) -> datetime:
        """
        Returns the date and time of the ending of the day with the given timezone

        :param timezone: The desired timezone, defaults to UTC
        :param year: The target year, ignore or pass None to use the current year
        :param month: The target month, ignore or pass None to use the current month
        :param day: The target day, ignore or pass None to use the current day
        """
        return datetime.now(tz=timezone).replace(
            year=year if year is not None else datetime.now(tz=timezone).year,
            month=month if month is not None else datetime.now(tz=timezone).month,
            day=day if day is not None else datetime.now(tz=timezone).day,
            hour=23,
            minute=59,
            second=59,
            microsecond=999999
        )

    @staticmethod
    def get_month_start(timezone=pytz.utc, year: int = None, month: int = None) -> datetime:
        """
        Returns the date and time of the beginning of the month with the given timezone

        :param timezone: The desired timezone, defaults to UTC
        :param year: The target year, ignore or pass None to use the current year
        :param month: The target month, ignore or pass None to use the current month
        """
        return datetime.now(tz=timezone).replace(
            year=year if year is not None else datetime.now(tz=timezone).year,
            month=month if month is not None else datetime.now(tz=timezone).month,
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

    @staticmethod
    def get_month_end(timezone=pytz.utc, year: int = None, month: int = None) -> datetime:
        """
        Returns the date and time of the ending of the month with the given timezone

        :param timezone: The desired timezone, defaults to UTC
        :param year: The target year, ignore or pass None to use the current year
        :param month: The target month, ignore or pass None to use the current month
        """
        final_year = year if year is not None else datetime.now(tz=timezone).year
        final_month = month if month is not None else datetime.now(tz=timezone).month
        return datetime.now(tz=timezone).replace(
            year=final_year,
            month=final_month,
            day=monthrange(final_year, final_month)[1],
            hour=23,
            minute=59,
            second=59,
            microsecond=999999
        )

    @staticmethod
    def get_year_start(timezone=pytz.utc, year: int = None):
        """
        Returns the date and time of the beginning of the year with the given timezone

        :param timezone: The desired timezone, defaults to UTC
        :param year: The target year, ignore or pass None to use the current year
        """
        return datetime.now(tz=timezone).replace(
            year=year if year is not None else datetime.now(tz=timezone).year,
            month=1,
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

    @staticmethod
    def get_year_end(timezone=pytz.utc, year: int = None):
        """
        Returns the date and time of the ending of the year with the given timezone

        :param timezone: The desired timezone, defaults to UTC
        :param year: The target year, ignore or pass None to use the current year
        """
        return datetime.now(tz=timezone).replace(
            year=year if year is not None else datetime.now(tz=timezone).year,
            month=12,
            day=31,
            hour=23,
            minute=59,
            second=59,
            microsecond=999999
        )

    @staticmethod
    def adjust_offset(original_datetime: datetime, offset: int, local_to_utc: bool) -> datetime:
        """
        Returns a new datetime object by adjusting the original datetime according to the given offset (in minutes). Note that Javascript offset should be multiplied by -1

        :param original_datetime: The original and unchanged datetime object
        :param offset: The desired offset in minutes (Note that the Javascript offset obtained via `new Date().getTimezoneOffset()` should be multiplied by -1)
        :param local_to_utc: Set to True if the original datetime is in local time and set to False if the original datetime is in UTC timezone
        """
        if local_to_utc:
            new_time = original_datetime - timedelta(minutes=offset)
        else:
            new_time = original_datetime + timedelta(minutes=offset)
        return new_time

    @staticmethod
    def get_period(year: int, month: int, day: int, period: str, offset: int = 0) -> Tuple[datetime, datetime]:
        """
        Returns the beginning and the ending datetime of a period

        :param year: The target year
        :param month: The target month
        :param day: The target day
        :param period: The desired period time-span. Please use the period constants of TimeUtility such as `TimeUtility.DAILY'
        :param offset: The optional timezone offset in minutes. (Note that the Javascript offset obtained via `new Date().getTimezoneOffset()` should be multiplied by -1)
        """
        if period == TimeUtility.DAILY:
            start = TimeUtility.get_date_start(year, month, day)
            end = TimeUtility.get_date_end(year, month, day)
        elif period == TimeUtility.MONTHLY:
            start = TimeUtility.get_month_start(year, month)
            end = TimeUtility.get_month_end(year, month)
        elif period == TimeUtility.ANNUAL:
            start = TimeUtility.get_year_start(year)
            end = TimeUtility.get_year_end(year)
        else:
            raise ValueError()

        if offset == 0:
            return start, end

        return TimeUtility.adjust_offset(start, offset, False), TimeUtility.adjust_offset(end, offset, False)

    @staticmethod
    def difference(large_time: datetime, small_time: datetime, time_span: str = 'second') -> int:
        """
        The difference between two datetime objects in microseconds, seconds, minutes, hours, or days

        :param large_time: The larger datetime object
        :param small_time: The smaller datetime object
        :param time_span: The time-span of difference. Please use the time unit constants of TimeUtility such as `TimeUtility.HOUR`
        """

        final_large = large_time if TimeUtility.is_aware(large_time) else TimeUtility.make_aware(large_time)
        final_small = small_time if TimeUtility.is_aware(small_time) else TimeUtility.make_aware(small_time)

        if time_span == TimeUtility.SECOND:
            return abs((final_large - final_small).seconds)
        elif time_span == TimeUtility.MICROSECOND:
            return abs((final_large - final_small).microseconds)
        elif time_span == TimeUtility.DAY:
            return abs((final_large - final_small).days)
        elif time_span == TimeUtility.MINUTE:
            return int(abs((final_large - final_small).seconds)/60)
        elif time_span == TimeUtility.HOUR:
            return int(abs((final_large - final_small).seconds)/3600)
        else:
            raise ValueError()

    @staticmethod
    def is_leap_year(year: int = None):
        """
        Checks whether the given year is a leap year.

        :param year: The target year. Pass None or ignore to use the current year in UTC timezone
        """
        if year is None:
            year = TimeUtility.now().year

        if isinstance(year, int) is False:
            raise ValueError()

        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_week(d: date) -> TimeUtilityWeek:
        return TimeUtilityWeek(d)

    @staticmethod
    def get_week_by_week_number(year: int, week: int) -> TimeUtilityWeek:
        return TimeUtilityWeek.get_week_from_week_number(year, week)

    @staticmethod
    def get_four_week_period(d: date) -> (TimeUtilityWeek, TimeUtilityWeek):
        return TimeUtilityWeek.get_four_week_period(d)
