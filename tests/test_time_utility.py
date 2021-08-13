# Python
import unittest
from datetime import datetime, date
from calendar import monthrange

# Third Party
import pytz

# Time Utility
from time_utility import TimeUtility


class TestTimeUtility(unittest.TestCase):

    def test_is_naive(self):
        self.assertTrue(TimeUtility.is_naive(datetime.now()))

    def test_is_aware(self):
        self.assertTrue(TimeUtility.is_aware(TimeUtility.now()))

    def test_make_aware(self):
        self.assertTrue(TimeUtility.is_aware(TimeUtility.make_aware(datetime.now())))

    def test_now(self):
        self.assertEqual(type(TimeUtility.now()), type(datetime.now()))

    def test_today(self):
        self.assertEqual(type(TimeUtility.today()), type(datetime.now().date()))

    def test_get_date_start(self):
        start = TimeUtility.get_date_start()
        manual = datetime.now(tz=pytz.utc)

        self.assertEqual(start.year, manual.year)
        self.assertEqual(start.month, manual.month)
        self.assertEqual(start.day, manual.day)
        self.assertEqual(start.hour, 0)
        self.assertEqual(start.minute, 0)
        self.assertEqual(start.second, 0)
        self.assertEqual(start.microsecond, 0)

    def test_get_date_end(self):
        start = TimeUtility.get_date_end()
        manual = datetime.now(tz=pytz.utc)

        self.assertEqual(start.year, manual.year)
        self.assertEqual(start.month, manual.month)
        self.assertEqual(start.day, manual.day)
        self.assertEqual(start.hour, 23)
        self.assertEqual(start.minute, 59)
        self.assertEqual(start.second, 59)
        self.assertEqual(start.microsecond, 999999)

    def test_get_month_start(self):
        start = TimeUtility.get_month_start()
        manual = datetime.now(tz=pytz.utc)

        self.assertEqual(start.year, manual.year)
        self.assertEqual(start.month, manual.month)
        self.assertEqual(start.day, 1)
        self.assertEqual(start.hour, 0)
        self.assertEqual(start.minute, 0)
        self.assertEqual(start.second, 0)
        self.assertEqual(start.microsecond, 0)

    def test_get_month_end(self):
        start = TimeUtility.get_month_end()
        manual = datetime.now(tz=pytz.utc)

        self.assertEqual(start.year, manual.year)
        self.assertEqual(start.month, manual.month)
        self.assertEqual(start.day, monthrange(manual.year, manual.month)[1])
        self.assertEqual(start.hour, 23)
        self.assertEqual(start.minute, 59)
        self.assertEqual(start.second, 59)
        self.assertEqual(start.microsecond, 999999)

    def test_get_year_start(self):
        start = TimeUtility.get_year_start()
        manual = datetime.now(tz=pytz.utc)

        self.assertEqual(start.year, manual.year)
        self.assertEqual(start.month, 1)
        self.assertEqual(start.day, 1)
        self.assertEqual(start.hour, 0)
        self.assertEqual(start.minute, 0)
        self.assertEqual(start.second, 0)
        self.assertEqual(start.microsecond, 0)

    def test_get_year_end(self):
        start = TimeUtility.get_year_end()
        manual = datetime.now(tz=pytz.utc)

        self.assertEqual(start.year, manual.year)
        self.assertEqual(start.month, 12)
        self.assertEqual(start.day, 31)
        self.assertEqual(start.hour, 23)
        self.assertEqual(start.minute, 59)
        self.assertEqual(start.second, 59)
        self.assertEqual(start.microsecond, 999999)

    def test_adjust_offset(self):
        utc_time = TimeUtility.now()
        local_time = datetime.now()

        small_time = utc_time
        large_time = local_time

        minute_difference = TimeUtility.difference(large_time, small_time, TimeUtility.MINUTE)

        adjusted = TimeUtility.adjust_offset(utc_time, minute_difference, False)

        aware_local = TimeUtility.make_aware(local_time)

        self.assertEqual(aware_local.year, adjusted.year)
        self.assertEqual(aware_local.month, adjusted.month)
        self.assertEqual(aware_local.day, adjusted.day)
        self.assertEqual(aware_local.hour, adjusted.hour)
        self.assertEqual(aware_local.minute, adjusted.minute)
        self.assertEqual(aware_local.second, adjusted.second)
        
    def test_is_leap_year(self):
        self.assertTrue(TimeUtility.is_leap_year(2020))
        self.assertFalse(TimeUtility.is_leap_year(2019))

    def test_week(self):
        od = date(2021, 8, 13)

        week = TimeUtility.get_week(od)
        self.assertEqual(week.od, od)
        self.assertEqual(week.week_number, 32)
        self.assertEqual(week.week_start, date(2021, 8, 9))
        self.assertEqual(week.week_end, date(2021, 8, 15))

        week_2 = TimeUtility.get_week_by_week_number(2021, 32)
        self.assertEqual(week_2.od, date(2021, 8, 9))
        self.assertEqual(week_2.week_number, 32)
        self.assertEqual(week_2.week_start, date(2021, 8, 9))
        self.assertEqual(week_2.week_end, date(2021, 8, 15))


if __name__ == '__main__':
    unittest.main()
