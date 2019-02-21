from datetime import datetime, timedelta, timezone
import pytz

class InvasionTimer:
   
    invasion_delta = timedelta(hours=19)
    invasion_duration = timedelta(hours=7)

    def __init__(self, now=None):
        if now is None:
            now = datetime.now(tz=pytz.utc)

        self.now = now + timedelta(hours=3)

  
    def next_invasion_date(self) -> datetime:
        """Return the next invasion date.
        Invasions start every 18.5 hours and last 6 hours."""
        # This is our base date. We now an invasion happened at that point (UTC).
        invasion_date = datetime(2019, 2, 18, 7, 0, 0, tzinfo=pytz.utc)

        while True:
            # Add 18.5h hours to the first know date
            # as long as it's smaller than the current date.
            if invasion_date >= self.now:
                return invasion_date

            invasion_date += InvasionTimer.invasion_delta


    def last_invasion_date(self, idate):
        """Return the date of the last invasion."""
        return idate - InvasionTimer.invasion_delta

    
    def invasion_running(self,lidate):
        """Return True or False if an invasion is currently going on."""
        invasion_date = self.last_invasion_date
        return lidate <= self.now <= lidate + InvasionTimer.invasion_duration

    def invasion_time_left(self,lidate,invasionStatus):
        """Return the time left on an invasion if there's one going on."""
        if invasionStatus:
            return (lidate + InvasionTimer.invasion_duration) - self.now
    
    def till_next_invasion(self,next_invasion):
        return next_invasion - self.now

