import unittest
from timecounter import TimeCounter  # Assuming the library is saved as time_counter.py

class TestTimeCounter(unittest.TestCase):
    
    def setUp(self):
        """Initialize TimeCounter with 13 hours, 30 minutes, and 45 seconds for testing."""
        self.tc = TimeCounter(13, 30, 45)
    
    def test_initialization(self):
        """Test correct initialization of military and standard time."""
        self.assertEqual(self.tc.get_military_time(), "13:30:45")
        self.assertEqual(self.tc.get_standard_time(), "01:30:45 PM")
    
    def test_valid_time(self):
        """Test that valid times do not raise an exception."""
        try:
            TimeCounter(0, 0, 0)  # Midnight
            TimeCounter(23, 59, 59)  # Just before midnight
            TimeCounter(12, 30, 30)  # Midday with some seconds
            TimeCounter(11, 0, 0)  # 11 AM
        except ValueError:
            self.fail("Valid time raised ValueError unexpectedly.")
    
    def test_invalid_hours(self):
        """Test that invalid hours raise ValueError."""
        with self.assertRaises(ValueError):
            TimeCounter(-1, 30, 30)  # Negative hour
        with self.assertRaises(ValueError):
            TimeCounter(24, 30, 30)  # Hour too high
    
    def test_invalid_minutes(self):
        """Test that invalid minutes raise ValueError."""
        with self.assertRaises(ValueError):
            TimeCounter(12, -1, 30)  # Negative minutes
        with self.assertRaises(ValueError):
            TimeCounter(12, 60, 30)  # Minutes too high
    
    def test_invalid_seconds(self):
        """Test that invalid seconds raise ValueError."""
        with self.assertRaises(ValueError):
            TimeCounter(12, 30, -1)  # Negative seconds
        with self.assertRaises(ValueError):
            TimeCounter(12, 30, 60)  # Seconds too high
    
    def test_increment_second(self):
        """Test incrementing by one second."""
        self.tc.increment(unit='second')
        self.assertEqual(self.tc.get_military_time(), "13:30:46")
        self.assertEqual(self.tc.get_standard_time(), "01:30:46 PM")
    
    def test_increment_minute(self):
        """Test incrementing by one minute."""
        self.tc.increment(unit='minute')
        self.assertEqual(self.tc.get_military_time(), "13:31:45")
        self.assertEqual(self.tc.get_standard_time(), "01:31:45 PM")
    
    def test_increment_hour(self):
        """Test incrementing by one hour."""
        self.tc.increment(unit='hour')
        self.assertEqual(self.tc.get_military_time(), "14:30:45")
        self.assertEqual(self.tc.get_standard_time(), "02:30:45 PM")
    
    def test_decrement_second(self):
        """Test decrementing by one second."""
        self.tc.decrement(unit='second')
        self.assertEqual(self.tc.get_military_time(), "13:30:44")
        self.assertEqual(self.tc.get_standard_time(), "01:30:44 PM")
    
    def test_decrement_minute(self):
        """Test decrementing by one minute."""
        self.tc.decrement(unit='minute')
        self.assertEqual(self.tc.get_military_time(), "13:29:45")
        self.assertEqual(self.tc.get_standard_time(), "01:29:45 PM")
    
    def test_decrement_hour(self):
        """Test decrementing by one hour."""
        self.tc.decrement(unit='hour')
        self.assertEqual(self.tc.get_military_time(), "12:30:45")
        self.assertEqual(self.tc.get_standard_time(), "12:30:45 PM")
    
    def test_rollover_increment(self):
        """Test incrementing time when it rolls over to the next day."""
        tc = TimeCounter(23, 59, 59)
        tc.increment(unit='second')
        self.assertEqual(tc.get_military_time(), "00:00:00")
        self.assertEqual(tc.get_standard_time(), "12:00:00 AM")
    
    def test_rollover_decrement(self):
        """Test decrementing time when it rolls over to the previous day."""
        tc = TimeCounter(0, 0, 0)
        tc.decrement(unit='second')
        self.assertEqual(tc.get_military_time(), "23:59:59")
        self.assertEqual(tc.get_standard_time(), "11:59:59 PM")
    
    def test_standard_time_format(self):
        """Test conversion of hours at AM/PM boundaries."""
        tc = TimeCounter(13, 0, 0)
        self.assertEqual(tc.get_standard_time(), "01:00:00 PM")
        tc = TimeCounter(0, 0, 0)
        self.assertEqual(tc.get_standard_time(), "12:00:00 AM")
    
    def test_invalid_unit(self):
        """Test that invalid time units raise errors."""
        with self.assertRaises(ValueError):
            self.tc.increment(unit='day')
        with self.assertRaises(ValueError):
            self.tc.decrement(unit='week')

if __name__ == '__main__':
    unittest.main()
