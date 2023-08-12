import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_needs_service_true(self):
        current_mileage = 40000
        last_service_mileage = 10
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_needs_service_false(self):
        current_mileage = 20000
        last_service_mileage = 10
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_sternman_engine_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
        

class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_needs_service_true(self):
        current_mileage = 75000
        last_service_mileage = 10
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_needs_service_false(self):
        current_mileage = 40000
        last_service_mileage = 10
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
