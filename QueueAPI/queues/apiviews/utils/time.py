import datetime
from django.utils import timezone


def get_starting_of_current_manila_timezone():
        year = timezone.now().now().year
        month = timezone.now().now().month
        day = timezone.now().now().day
        aware_dt = datetime.datetime(year, month, day-1, 16, tzinfo=datetime.timezone.utc)
        return aware_dt