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
        d = datetime.strptime(w + '-1', "%Y-W%W-%w").date()
        return cls(d)
