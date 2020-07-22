# Python
import unittest
from datetime import datetime

# Third Party
import pytz

# Time Utility
from time_utility import TimeUtility


class TestTimeUtility(unittest.TestCase):

    def test_now(self):
        TimeUtility.now(timezone=None)


if __name__ == '__main__':
    unittest.main()
