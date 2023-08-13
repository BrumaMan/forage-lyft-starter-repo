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
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Calliope(
                CapuletEngine(current_mileage, last_service_mileage),
                SpindlerBattery(last_service_date, current_date),
                OctoprimeTires(tire_wear)
                )
    
    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Glissade(
                WilloughbyEngine(current_mileage, last_service_mileage),
                SpindlerBattery(last_service_date, current_date),
                CarriganTires(tire_wear)
                )
    
    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_wear):
        return Palindrome(
                SternmanEngine(warning_light_on),
                SpindlerBattery(last_service_date, current_date),
                OctoprimeTires(tire_wear)
                )
    
    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Rorschach(
                WilloughbyEngine(current_mileage, last_service_mileage),
                NubbinBattery(last_service_date, current_date),
                CarriganTires(tire_wear)
                )
    
    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Thovex(
                CapuletEngine(current_mileage, last_service_mileage),
                NubbinBattery(last_service_date, current_date),
                CarriganTires(tire_wear)
                )
        