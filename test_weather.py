import unittest
from weather_app import convert_c_to_f

class TestWeatherApp(unittest.TestCase):
    def test_convert_c_to_f(self):
        self.assertEqual(convert_c_to_f(0), 32.0)
        self.assertEqual(convert_c_to_f(25), 77.0)
        self.assertEqual(convert_c_to_f(-10), 14.0)
        self.assertEqual(convert_c_to_f(100), 212.0)

if __name__ == "__main__":
    unittest.main()
