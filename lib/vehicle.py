class Vehicle:
    
    def __init__(self, wheel_size, wheel_number):
        self._wheel_size = wheel_size
        self._wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"
