import unittest
from datetime import datetime

# from car import Car
# from serviceable import Serviceable
# from carFactory import CarFactory
# from utils import add_years_to_date

from battery.Battery import Battery
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery

from engine.Engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class testingBatteryAndEngine(unittest.TestCase):
    
    def nubbinBatteryTest1(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        nb = NubbinBattery(today, last_service_date)
        self.assertTrue(nb.needs_service())
    
    def nubbinBatteryTest2(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        nb = NubbinBattery(today, last_service_date)
        self.assertFalse(nb.needs_service())

    def spindlerBatteryTest1(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        sb = SpindlerBattery(today, last_service_date)
        self.assertFalse(sb.needs_service())
    
    def spindlerBatteryTest2(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        sb = SpindlerBattery(today, last_service_date)
        self.assertTrue(sb.needs_service())

    def capuletEngineTest1(self):
        cm = 100000
        lsm = 8000
        ce = CapuletEngine(cm, lsm)
        self.assertTrue(ce.needs_service())
    
    def capuletEngineTest2(self):
        cm = 8000
        lsm = 3000
        ce = CapuletEngine(cm, lsm)
        self.assertFalse(ce.needs_service())
    
    def willoughbyEngineTest1(self):
        cm = 100000
        lsm = 8000
        we = WilloughbyEngine(cm, lsm)
        self.assertTrue(we.needs_service())
    
    def willoughbyEngineTest2(self):
        cm = 8000
        lsm = 3000
        we = WilloughbyEngine(cm, lsm)
        self.assertFalse(we.needs_service())
    
    def sternmanEngineTest1(self):
        warninglight = True
        se = SternmanEngine(warninglight)
        self.assertTrue(se.needs_service())

    def sternmanEngineTest2(self):
        warninglight = False
        se = SternmanEngine(warninglight)
        self.assertFalse(se.needs_service())

if __name__ == '__main__':
    unittest.main()    
        
