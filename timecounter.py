class TimeCounter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    SECONDS_IN_HOUR = MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    SECONDS_IN_DAY = HOURS_IN_DAY * SECONDS_IN_HOUR
    
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._validate_time(hours, minutes, seconds)
        self.total_seconds = self._convert_to_seconds(hours, minutes, seconds)
    
    def _validate_time(self, hours, minutes, seconds):
        """Validate the time values to ensure they are within acceptable ranges."""
        if not (0 <= hours < self.HOURS_IN_DAY):
            raise ValueError("Hours must be between 0 and 23")
        if not (0 <= minutes < self.MINUTES_IN_HOUR):
            raise ValueError("Minutes must be between 0 and 59")
        if not (0 <= seconds < self.SECONDS_IN_MINUTE):
            raise ValueError("Seconds must be between 0 and 59")
    
    def _convert_to_seconds(self, hours, minutes, seconds):
        return hours * self.SECONDS_IN_HOUR + minutes * self.SECONDS_IN_MINUTE + seconds
    
    def _convert_from_seconds(self):
        seconds = self.total_seconds % self.SECONDS_IN_MINUTE
        total_minutes = self.total_seconds // self.SECONDS_IN_MINUTE
        minutes = total_minutes % self.MINUTES_IN_HOUR
        hours = (total_minutes // self.MINUTES_IN_HOUR) % self.HOURS_IN_DAY
        return hours, minutes, seconds
    
    def increment(self, unit='second'):
        if unit == 'second':
            self.total_seconds += 1
        elif unit == 'minute':
            self.total_seconds += self.SECONDS_IN_MINUTE
        elif unit == 'hour':
            self.total_seconds += self.SECONDS_IN_HOUR
        else:
            raise ValueError("Unit must be 'second', 'minute', or 'hour'")
        
        self.total_seconds %= self.SECONDS_IN_DAY
    
    def decrement(self, unit='second'):
        if unit == 'second':
            self.total_seconds -= 1
        elif unit == 'minute':
            self.total_seconds -= self.SECONDS_IN_MINUTE
        elif unit == 'hour':
            self.total_seconds -= self.SECONDS_IN_HOUR
        else:
            raise ValueError("Unit must be 'second', 'minute', or 'hour'")
        
        if self.total_seconds < 0:
            self.total_seconds += self.SECONDS_IN_DAY
    
    def get_military_time(self):
        hours, minutes, seconds = self._convert_from_seconds()
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    def get_standard_time(self):
        hours, minutes, seconds = self._convert_from_seconds()
        period = "AM" if hours < 12 else "PM"
        standard_hours = hours % 12
        if standard_hours == 0:
            standard_hours = 12
        return f"{standard_hours:02}:{minutes:02}:{seconds:02} {period}"
    
    def __str__(self):
        return f"Military Time: {self.get_military_time()}, Standard Time: {self.get_standard_time()}"
