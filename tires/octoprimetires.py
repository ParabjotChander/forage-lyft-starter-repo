from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tireSensors):
        super.__init__(tireSensors)

    def needs_service(self):
        tireSen = self.tireSensors
        sum = 0
        for tire in tireSen:
            sum += tire
        if sum >= 3:
            return True
        else:
            return False

