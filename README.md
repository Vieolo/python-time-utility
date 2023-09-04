# Time Utility 0.2.1

Time utility is a series of utility methods regarding date and time for python.

```text
Note: This package requires python 3.6 and higher
```

## Installation
```text
pip3 install time_utility
```

## Import
```python
from time_utility import TimeUtility
```

## Usage
The following are the methods available in TimeUtility

<br><br>
* ###`is_naive(target_datetime)`
Checks if the given datetime object is naive.

Parameters:<br>
1. `target_datetime: datetime.datetime` => The target datetime to be checked

Returns: `bool`

Example:
```python
from time_utility import TimeUtility

is_it_naive = TimeUtility.is_naive(TimeUtility.now())
```





<br><br>
* ###`is_aware(target_datetime)`
Checks if the given datetime object is aware

Example:
```python
from time_utility import TimeUtility

is_it_aware = TimeUtility.is_aware(TimeUtility.now())
```






<br><br>
* ####`make_aware(target_datetime, timezone=pytz.utc)`
Returns an aware datetime object based on the naive target_datetime

Parameters:<br>
1. `target_datetime: datetime.datetime` => The target datetime
2. `timezone` [optional] => The preferred timezone. [default: UTC] 

returns `datetime.datetime`

Example:
```python
from time_utility import TimeUtility
from datetime import datetime

aware = TimeUtility.make_aware(datetime.now())
```






<br><br>
* ####`now(timezone=pytz.utc)`
Returns an aware instance of the current datetime

Parameters:<br>
1. `timezone` [Optional] => The preferred timezone [default: UTC]

returns `datetime.datetime`

Example:
```python
from time_utility import TimeUtility

now = TimeUtility.now()
```





<br><br>
* ####`today(timezone=pytz.utc)`
Returns an aware instance of today's date

Parameters:<br>
1. `timezone` [Optional] => The preferred timezone [default: UTC]

returns `datetime.date`

Example:
```python
from time_utility import TimeUtility

today = TimeUtility.today()
```





<br><br>
* ####`get_date_start(timezone=pytz.utc, year = None, month = None, day = None)`
Returns the date and time of the beginning of the day with the given timezone

Parameters:<br>
1. `timezone` [Optional] => The preferred timezone [default: UTC]
2. `year: int` => The target year. [default: None (will be set to current year)]
3. `month: int` => The target month. [default: None (will be set to current month)]
4. `day: int` => The target day. [default: None (will be set to current day)]

returns `datetime.datetime`

Example:
```python
from time_utility import TimeUtility

day_start = TimeUtility.get_date_start(year=2020, month=5)
```




<br><br>
* ####`get_date_end(timezone=pytz.utc, year = None, month = None, day = None)`
Returns the date and time of the ending of the day with the given timezone

Parameters:<br>
1. `timezone` [Optional] => The preferred timezone [default: UTC]
2. `year: int` => The target year. [default: None (will be set to current year)]
3. `month: int` => The target month. [default: None (will be set to current month)]
4. `day: int` => The target day. [default: None (will be set to current day)]

returns `datetime.datetime`

Example:
```python
from time_utility import TimeUtility

day_start = TimeUtility.get_date_end(year=2020, month=5)
```




<br><br>
* ####`get_month_start(timezone=pytz.utc, year = None, month = None)`
Returns the date and time of the beginning of the month with the given timezone

Parameters:<br>
1. `timezone` [Optional] => The preferred timezone [default: UTC]
2. `year: int` => The target year. [default: None (will be set to current year)]
3. `month: int` => The target month. [default: None (will be set to current month)]

returns `datetime.datetime`

Example:
```python
from time_utility import TimeUtility

day_start = TimeUtility.get_month_start(year=2020, month=5)
```



<br><br>
* ####`get_month_end(timezone=pytz.utc, year = None, month = None)`
Returns the date and time of the ending of the month with the given timezone

Parameters:<br>
1. `timezone` [Optional] => The preferred timezone [default: UTC]
2. `year: int` => The target year. [default: None (will be set to current year)]
3. `month: int` => The target month. [default: None (will be set to current month)]

returns `datetime.datetime`

Example:
```python
from time_utility import TimeUtility

day_start = TimeUtility.get_month_end(year=2020, month=5)
```



<br><br>
* ####`get_year_start(timezone=pytz.utc, year = None)`
Returns the date and time of the beginning of the year with the given timezone

Parameters:<br>
1. `timezone` [Optional] => The preferred timezone [default: UTC]
2. `year: int` => The target year. [default: None (will be set to current year)]

returns `datetime.datetime`

Example:
```python
from time_utility import TimeUtility

day_start = TimeUtility.get_year_start(year=2020)
```



<br><br>
* ####`get_year_end(timezone=pytz.utc, year = None)`
Returns the date and time of the ending of the year with the given timezone

Parameters:<br>
1. `timezone` [Optional] => The preferred timezone [default: UTC]
2. `year: int` => The target year. [default: None (will be set to current year)]

returns `datetime.datetime`

Example:
```python
from time_utility import TimeUtility

day_start = TimeUtility.get_year_end(year=2020)
```





<br><br>
* ####`adjust_offset(original_datetime, offset, local_to_utc)`
Creates and returns a new datetime object using the given datetime object with the given offset in minutes.
The offset should be positive for timezones ahead of UTC (e.g. India) and negative for timezones before UTC (e.g. US) <br>
Note that the offset obtained in Javascript via `new Date().getTimezoneOffset()` should be multiplied by -1.

Parameters:<br>
1. `original_datetime: datetime.datetime` => The original datetime to be adjusted
2. `offset: int` => The offset in minutes
3. `local_to_utc` => Set to True if the original datetime is in local time and set to False if the original datetime is in UTC time

returns `datetime.datetime`

Example:
```python
from time_utility import TimeUtility
from datetime import datetime

adjusted_datetime = TimeUtility.adjust_offset(TimeUtility.make_aware(datetime.now()), 330, True)
```




<br><br>
* ####`get_period(year, month, day, period, offset = 0)`
Gets the start and the end datetime of a selected period

Parameters:<br>
1. `year: int` => The selected year
2. `month: int` => The selected month
3. `day: int` => The selected day
4. `period: str` => The selected period. Your options are: `TimeUtility.DAILY`, `TimeUtility.MONTHLY`, and `TimeUtility.ANNUAL`
5. `offset: int` [optional] => The offset from UTC to adjust the start and the end [default: 0]

returns `(datetime.datetime, datetime.datetime)`

Example:
```python
from time_utility import TimeUtility

start, end = TimeUtility.get_period(year=2020, month=2, day=10, period=TimeUtility.MONTHLY, offset=330)
```




<br><br>
* ####`difference(large_time, small_time, time_span = TimeUtility.SECOND)`
Calculates the difference between two datetime object based on the given time-span

Parameters:<br>
1. `large_time: datetime.datetime` => The bigger datetime object of the two
2. `small_time: datetime.datetime` => The smaller datetime object of the two
3. `time_span: str` [Optional] => The time-span unit of time to calculate the difference. The options are `TimeUtility.MICROSECOND`, `TimeUtility.SECOND`, `TimeUtility.MINUTE`, `TimeUtility.HOUR`, `TimeUtility.DAY`. [default: TimeUtility.SECOND] 

returns `int`

Example:
```python
from time_utility import TimeUtility

difference = TimeUtility.difference(TimeUtility.adjust_offset(TimeUtility.now(), 120, False), TimeUtility.now(), TimeUtility.MINUTE)
```




<br><br>
* ####`is_leap_year(year = None)`
Checks if the given year is a leap year or not

Parameters:<br>
1. `year: int` [Optional] => The target year [default: None (will be set to current year)]

returns `bool`

Example:
```python
from time_utility import TimeUtility

is_leap = TimeUtility.is_leap_year(year=2020)
```
