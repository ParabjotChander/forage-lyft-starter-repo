from tires import Tires

class CarriganTires(Tires):
    def __init__(self, tireSensors):
        super.__init__(tireSensors)
    
    def needs_service(self):
        tireSen = self.tireSensors
        
        for tire in tireSen:
            if tire >= 0.9:
                return True
        return False