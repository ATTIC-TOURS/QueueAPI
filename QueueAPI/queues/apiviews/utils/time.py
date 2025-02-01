import datetime
from django.utils import timezone
from django.conf import settings
import pytz


def get_starting_of_current_manila_timezone():

        year = timezone.now().now().year

        month = timezone.now().now().month

        day = timezone.now().now().day

        aware_dt = datetime.datetime(year, 1, 31, 16, tzinfo=datetime.timezone.utc)

        return aware_dt
       