from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.SpindlerBattery import SpindlerBattery
from battery.nubbinBattery import NubbinBattery


class CarFactory:
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Calliope(
                CapuletEngine(current_mileage, last_service_mileage),
                SpindlerBattery(last_service_date, current_date)
                )
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Glissade(
                WilloughbyEngine(current_mileage, last_service_mileage),
                SpindlerBattery(last_service_date, current_date)
                )
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        return Palindrome(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Rorschach(
                WilloughbyEngine(current_mileage, last_service_mileage),
                NubbinBattery(last_service_date, current_date)
                )
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Thovex(
                CapuletEngine(current_mileage, last_service_mileage),
                NubbinBattery(last_service_date, current_date)
                )
        