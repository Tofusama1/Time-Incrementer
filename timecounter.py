class TimeCounter:
    seconds_in_minute = 60
    minutes_in_hour = 60
    hours_in_day = 24
    seconds_in_hour = minutes_in_hour * seconds_in_minute
    seconds_in_day = hours_in_day * seconds_in_hour
    
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._validate_time(hours, minutes, seconds)
        self.total_seconds = self._convert_to_seconds(hours, minutes, seconds)
    
    def _validate_time(self, hours, minutes, seconds):
        """Validate the time values to ensure they are within acceptable ranges."""
        if not (0 <= hours < self.hours_in_day):
            raise ValueError("Hours must be between 0 and 23")
        if not (0 <= minutes < self.minutes_in_hour):
            raise ValueError("Minutes must be between 0 and 59")
        if not (0 <= seconds < self.seconds_in_minute):
            raise ValueError("Seconds must be between 0 and 59")
    
    def _convert_to_seconds(self, hours, minutes, seconds):
        return hours * self.seconds_in_hour + minutes * self.seconds_in_minute + seconds
    
    def _convert_from_seconds(self):
        seconds = self.total_seconds % self.seconds_in_minute
        total_minutes = self.total_seconds // self.seconds_in_minute
        minutes = total_minutes % self.minutes_in_hour
        hours = (total_minutes // self.minutes_in_hour) % self.hours_in_day
        return hours, minutes, seconds
    
    def increment(self, unit='second'):
        if unit == 'second':
            self.total_seconds += 1
        elif unit == 'minute':
            self.total_seconds += self.seconds_in_minute
        elif unit == 'hour':
            self.total_seconds += self.seconds_in_hour
        else:
            raise ValueError("Unit must be 'second', 'minute', or 'hour'")
        
        self.total_seconds %= self.seconds_in_day
    
    def decrement(self, unit='second'):
        if unit == 'second':
            self.total_seconds -= 1
        elif unit == 'minute':
            self.total_seconds -= self.seconds_in_minute
        elif unit == 'hour':
            self.total_seconds -= self.seconds_in_hour
        else:
            raise ValueError("Unit must be 'second', 'minute', or 'hour'")
        
        if self.total_seconds < 0:
            self.total_seconds += self.seconds_in_day
    
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

# Example Usage
if __name__ == "__main__":
    # Create a TimeCounter instance with 13 hours, 30 minutes, and 45 seconds
    tc = TimeCounter(13, 30, 45)

    # Print military time
    print(tc.get_military_time())  
    # Output: "13:30:45"

    # Print standard time
    print(tc.get_standard_time())  
    # Output: "01:30:45 PM"

    # Increment by one minute
    tc.increment(unit='minute')
    print(tc.get_military_time())  
    # Output: "13:31:45"
    print(tc.get_standard_time())  
    # Output: "01:31:45 PM"

    # Decrement by one hour
    tc.decrement(unit='hour')
    print(tc.get_military_time())  
    # Output: "12:31:45"
    print(tc.get_standard_time())  
    # Output: "12:31:45 PM"

    # Test rollover by setting time to 23:59:59 and incrementing by one second
    tc = TimeCounter(23, 59, 59)
    tc.increment(unit='second')
    print(tc.get_military_time())  
    # Output: "00:00:00"
    print(tc.get_standard_time())  
    # Output: "12:00:00 AM"

    # Test rollover by setting time to 00:00:00 and decrementing by one second
    tc = TimeCounter(0, 0, 0)
    tc.decrement(unit='second')
    print(tc.get_military_time())  
    # Output: "23:59:59"
    print(tc.get_standard_time())  
    # Output: "11:59:59 PM"
