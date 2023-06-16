from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery

from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tires.carrigantires import CarriganTires
from tires.octoprimetires import OctoprimeTires


class CarFactory:
    @staticmethod
    def create_calliope1(current_date, last_service_date, current_mileage, last_service_mileage, tireSensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tireSensors)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_calliope2(current_date, last_service_date, current_mileage, last_service_mileage, tireSensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tireSensors)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade1(current_date, last_service_date, current_mileage, last_service_mileage, tireSensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tireSensors)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_glissade2(current_date, last_service_date, current_mileage, last_service_mileage, tireSensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tireSensors)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome1(current_date, last_service_date, warning_light_is_on, tireSenors):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tireSenors)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_palindrome2(current_date, last_service_date, warning_light_is_on, tireSenors):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tireSenors)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach1(current_date, last_service_date, current_mileage, last_service_mileage, tireSensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tireSensors)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_rorschach2(current_date, last_service_date, current_mileage, last_service_mileage, tireSensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tireSensors)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex1(current_date, last_service_date, current_mileage, last_service_mileage, tireSensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tireSensors)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_thovex2(current_date, last_service_date, current_mileage, last_service_mileage, tireSensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tireSensors)
        car = Car(engine, battery, tires)
        return car
