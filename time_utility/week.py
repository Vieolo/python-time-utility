# Python
from datetime import date, timedelta, datetime


class TimeUtilityWeek:

    def __init__(self, od: date):
        self.od: date = od
        self.week_number: int = od.isocalendar()[1]
        self.week_start = od - timedelta(days=od.isoweekday() - 1)
        self.week_end = od + timedelta(days=7 - od.isoweekday())

    @classmethod
    def get_week_from_week_number(cls, year: int, week: int) -> 'TimeUtilityWeek':
        w = "{y}-W{wn}".format(y=year, wn=week)
        d = datetime.strptime(w + '-1', '%G-W%V-%u').date()
        return cls(d)

    @classmethod
    def get_four_week_period(cls, d: date) -> (date, int, date, int):
        week = cls(d)

        first_week = 1
        last_week = 4

        if week.week_number == 1 and d.month == 12:  # The last few days of year but in the first week of next year
            last_day_of_last_week = d - timedelta(days=1)
            last_week_of_year = cls(last_day_of_last_week)
            first_week = 49
            last_week = 1

            from_d = cls.get_week_from_week_number(d.year, 49).week_start
            to_d = date(week.week_start.year, 12, 31)

        elif week.week_number == 1 and d.month == 1 and week.week_start.month == 12:  # The Week 1 starts before Jan 1 and the selected date is in the new year
            first_week = 1
            last_week = 4
            from_d = date(d.year, 1, 1)
            to_d = cls.get_week_from_week_number(week.week_start.year + 1, 4).week_end

        elif week.week_number == 1 and week.week_start.month == 1 and week.week_start.isoweekday() == 1 and week.week_start.day == 1:  # The first day of year and the first day of the week 1
            first_week = 1
            last_week = 4
            from_d = date(week.week_start.year, 1, 1)
            to_d = date(week.week_start.year, 1, 28)
        elif week.week_number == 1 and week.week_start.month == 1 and week.week_start.isoweekday() > 1:  # The first day of the week 1 starts after Jan 1
            last_day_of_last_week = week.week_start - timedelta(days=1)
            last_week_of_year = cls(last_day_of_last_week)
            first_week = last_week_of_year.week_number
            last_week = 4
            from_d = week.week_start  # date(d.year, 1, 1)
            to_d = cls.get_week_from_week_number(week.week_start.year, 4).week_end
        elif week.week_number >= 52 and d.year > week.week_start.year:  # The first few days of the year in the last week of the last year
            first_week = week.week_number
            last_week = 4
            from_d = date(d.year, 1, 1)
            to_d = cls.get_week_from_week_number(d.year, 4).week_end
        elif week.week_number >= 49:
            first_week = 49
            from_d = cls.get_week_from_week_number(week.week_start.year, 49).week_start
            to_d = date(week.week_start.year, 12, 31)
            last_week = cls(to_d).week_number
        elif week.week_number <= 4:
            from_d = date(week.week_start.year, 1, 1)
            first_week = cls(from_d).week_number
            last_week = 4
            to_d = cls.get_week_from_week_number(week.week_start.year, 4).week_end
        else:
            if week.week_number % 4 == 0:
                first_week = week.week_number - 3
                last_week = week.week_number
            else:
                first_week = week.week_number - ((week.week_number % 4) - 1)
                last_week = week.week_number + (4 - (week.week_number % 4))

            # The first and last calculated weeks
            fw = cls.get_week_from_week_number(d.year, first_week)
            lw = cls.get_week_from_week_number(d.year, last_week)

            from_d = fw.week_start
            to_d = lw.week_end

        return from_d, first_week, to_d, last_week
