import datetime
from django.utils import timezone


def get_starting_of_current_manila_timezone():
        yesterday_dt = timezone.now() - datetime.timedelta(days=1)
        year = yesterday_dt.year
        month = yesterday_dt.month
        day = yesterday_dt.day
        aware_dt = datetime.datetime(year, month, day, 8, tzinfo=datetime.timezone.utc)
        return aware_dt