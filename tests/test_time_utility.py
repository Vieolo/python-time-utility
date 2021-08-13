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

        week_3 = TimeUtility.get_week_by_week_number(2020, 23)
        self.assertEqual(week_3.od, date(2020, 6, 1))
        self.assertEqual(week_3.week_number, 23)
        self.assertEqual(week_3.week_start, date(2020, 6, 1))
        self.assertEqual(week_3.week_end, date(2020, 6, 7))

    def test_four_week_period(self):
        # 1. The week is neither in the first nor in the last four weeks of the year
        one_date = date(2020, 6, 5)
        one_start_date, one_start_week, one_end_date, one_end_week = TimeUtility.get_four_week_period(one_date)

        self.assertEqual(one_start_week, 21)
        self.assertEqual(one_start_date, date(2020, 5, 18))
        self.assertEqual(one_end_week, 24)
        self.assertEqual(one_end_date, date(2020, 6, 14))

        # 2. First week of the year starts in the previous year, (given date in month of Jan)
        two_date = date(2020, 1, 1)
        two_start_date, two_start_week, two_end_date, two_end_week = TimeUtility.get_four_week_period(two_date)

        self.assertEqual(two_start_week, 1)
        self.assertEqual(two_start_date, date(2020, 1, 1))
        self.assertEqual(two_end_week, 4)
        self.assertEqual(two_end_date, date(2020, 1, 26))

        # 3. First week of the year starts in the previous year, (given date in month of Dec)
        three_date = date(2019, 12, 31)
        three_start_date, three_start_week, three_end_date, three_end_week = TimeUtility.get_four_week_period(three_date)

        self.assertEqual(three_start_week, 49)
        self.assertEqual(three_start_date, date(2019, 12, 2))
        self.assertEqual(three_end_week, 1)
        self.assertEqual(three_end_date, date(2019, 12, 31))

        # 4. First day of the year is the first day of the week 1
        four_date = date(2018, 1, 1)
        four_start_date, four_start_week, four_end_date, four_end_week = TimeUtility.get_four_week_period(four_date)

        self.assertEqual(four_start_week, 1)
        self.assertEqual(four_start_date, date(2018, 1, 1))
        self.assertEqual(four_end_week, 4)
        self.assertEqual(four_end_date, date(2018, 1, 28))

        # 5. The week 1 starts after Jan 1
        five_date = date(2021, 1, 7)
        five_start_date, five_start_week, five_end_date, five_end_week = TimeUtility.get_four_week_period(five_date)

        self.assertEqual(five_start_week, 53)
        self.assertEqual(five_start_date, date(2021, 1, 1))
        self.assertEqual(five_end_week, 4)
        self.assertEqual(five_end_date, date(2021, 1, 31))

        # 6. The first few days of the year is in the last week of the last year
        six_date = date(2021, 1, 1)
        six_start_date, six_start_week, six_end_date, six_end_week = TimeUtility.get_four_week_period(six_date)

        self.assertEqual(six_start_week, 53)
        self.assertEqual(six_start_date, date(2021, 1, 1))
        self.assertEqual(six_end_week, 4)
        self.assertEqual(six_end_date, date(2021, 1, 31))

        # 7. The last week of the year ends before the year
        seven_date = date(2019, 12, 29)
        seven_start_date, seven_start_week, seven_end_date, seven_end_week = TimeUtility.get_four_week_period(seven_date)

        self.assertEqual(seven_start_week, 49)
        self.assertEqual(seven_start_date, date(2019, 12, 2))
        self.assertEqual(seven_end_week, 1)
        self.assertEqual(seven_end_date, date(2019, 12, 31))

        # 8. The last week of the year ends at Dec 31
        eight_date = date(2017, 12, 20)
        eight_start_date, eight_start_week, eight_end_date, eight_end_week = TimeUtility.get_four_week_period(eight_date)

        self.assertEqual(eight_start_week, 49)
        self.assertEqual(eight_start_date, date(2017, 12, 4))
        self.assertEqual(eight_end_week, 52)
        self.assertEqual(eight_end_date, date(2017, 12, 31))

        # 9. The last week of the year ends after Dec 31
        nine_date = date(2020, 12, 31)
        nine_start_date, nine_start_week, nine_end_date, nine_end_week = TimeUtility.get_four_week_period(nine_date)

        self.assertEqual(nine_start_week, 49)
        self.assertEqual(nine_start_date, date(2020, 11, 30))
        self.assertEqual(nine_end_week, 53)
        self.assertEqual(nine_end_date, date(2020, 12, 31))

        # 10. The week number of the given date is 4
        ten_date = date(2021, 1, 27)
        ten_start_date, ten_start_week, ten_end_date, ten_end_week = TimeUtility.get_four_week_period(ten_date)

        self.assertEqual(ten_start_week, 53)
        self.assertEqual(ten_start_date, date(2021, 1, 1))
        self.assertEqual(ten_end_week, 4)
        self.assertEqual(ten_end_date, date(2021, 1, 31))

        # 11. The week number of the given date is the multiple of 4
        eleven_date = date(2021, 2, 27)
        eleven_start_date, eleven_start_week, eleven_end_date, eleven_end_week = TimeUtility.get_four_week_period(eleven_date)

        self.assertEqual(eleven_start_week, 5)
        self.assertEqual(eleven_start_date, date(2021, 2, 1))
        self.assertEqual(eleven_end_week, 8)
        self.assertEqual(eleven_end_date, date(2021, 2, 28))


if __name__ == '__main__':
    unittest.main()
