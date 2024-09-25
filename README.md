# TimeCounter Class Documentation

## Overview
The `TimeCounter` class provides a way to manage and manipulate time, represented in hours, minutes, and seconds. It allows you to increment or decrement the time, validate input, and convert between military and standard time formats.

## Constants
- **`SECONDS_IN_MINUTE`**: Number of seconds in one minute (60).
- **`MINUTES_IN_HOUR`**: Number of minutes in one hour (60).
- **`HOURS_IN_DAY`**: Number of hours in one day (24).
- **`SECONDS_IN_HOUR`**: Number of seconds in one hour (3600).
- **`SECONDS_IN_DAY`**: Number of seconds in one day (86400).

## Methods

### `__init__(self, hours=0, minutes=0, seconds=0)`
Initializes a new `TimeCounter` instance with the specified hours, minutes, and seconds.

**Parameters:**
- `hours` (int): The hour component (0 to 23).
- `minutes` (int): The minute component (0 to 59).
- `seconds` (int): The second component (0 to 59).

**Raises:**
- `ValueError`: If any parameter is out of the valid range.

### `_validate_time(self, hours, minutes, seconds)`
Validates the time values to ensure they are within acceptable ranges.

**Parameters:**
- `hours` (int): The hour component to validate.
- `minutes` (int): The minute component to validate.
- `seconds` (int): The second component to validate.

**Raises:**
- `ValueError`: If any parameter is out of the valid range.

### `_convert_to_seconds(self, hours, minutes, seconds)`
Converts the provided hours, minutes, and seconds into the total number of seconds.

**Parameters:**
- `hours` (int): The hour component.
- `minutes` (int): The minute component.
- `seconds` (int): The second component.

**Returns:**
- `int`: The total number of seconds.

### `_convert_from_seconds(self)`
Converts the total number of seconds stored in `self.total_seconds` back into hours, minutes, and seconds.

**Returns:**
- `tuple`: A tuple containing hours, minutes, and seconds.

### `increment(self, unit='second')`
Increments the time by the specified unit.

**Parameters:**
- `unit` (str): The unit to increment ('second', 'minute', 'hour').

**Raises:**
- `ValueError`: If the unit is not one of 'second', 'minute', or 'hour'.

**Behavior:**
- Increments `self.total_seconds` by the appropriate number of seconds.
- Ensures that `self.total_seconds` wraps around after reaching one day.

### `decrement(self, unit='second')`
Decrements the time by the specified unit.

**Parameters:**
- `unit` (str): The unit to decrement ('second', 'minute', 'hour').

**Raises:**
- `ValueError`: If the unit is not one of 'second', 'minute', or 'hour'.

**Behavior:**
- Decrements `self.total_seconds` by the appropriate number of seconds.
- Ensures that `self.total_seconds` wraps around to the previous day if it goes below zero.

### `get_military_time(self)`
Returns the time in 24-hour (military) format.

**Returns:**
- `str`: The time formatted as "HH:MM:SS".

### `get_standard_time(self)`
Returns the time in 12-hour standard format with AM/PM notation.

**Returns:**
- `str`: The time formatted as "HH:MM:SS AM/PM".

### `__str__(self)`
Returns a string representation of the `TimeCounter` instance, including both military and standard time formats.

**Returns:**
- `str`: A string representation of the time in both formats.

## Example Usage

```python
# Create a TimeCounter instance
tc = TimeCounter(13, 30, 45)

# Get military time
print(tc.get_military_time())  # Output: "13:30:45"

# Get standard time
print(tc.get_standard_time())  # Output: "01:30:45 PM"

# Increment by one minute
tc.increment(unit='minute')
print(tc.get_military_time())  # Output: "13:31:45"
print(tc.get_standard_time())  # Output: "01:31:45 PM"

# Decrement by one hour
tc.decrement(unit='hour')
print(tc.get_military_time())  # Output: "12:31:45"
print(tc.get_standard_time())  # Output: "12:31:45 PM"

# Test rollover
tc = TimeCounter(23, 59, 59)
tc.increment(unit='second')
print(tc.get_military_time())  # Output: "00:00:00"
print(tc.get_standard_time())  # Output: "12:00:00 AM"
