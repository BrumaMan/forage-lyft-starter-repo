import unittest
from datetime import date

from battery.nubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_needs_service_true(self):
        current_date = date.fromisoformat("2023-07-25")
        last_service_date = date.fromisoformat("2018-07-25")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-08-15")
        last_service_date = date.fromisoformat("2021-03-10")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
        
        
class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-07-18")
        last_service_date = date.fromisoformat("2021-04-25")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-10-15")
        last_service_date = date.fromisoformat("2022-05-13")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
        
        
if __name__ == '__main__':
    unittest.main()
    