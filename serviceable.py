from car import Car


class Serviceable(Car):
    def needs_service(self):
        return super().needs_service() 