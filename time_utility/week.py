# Python
from datetime import date, timedelta


class TimeUtilityWeek:

    def __init__(self, od: date):
        self.od: date = od
        self.week_number: int = od.isocalendar()[1]
        self.week_start = od - timedelta(days=od.isoweekday() - 1)
        self.week_end = od + timedelta(days=7 - od.isoweekday())
