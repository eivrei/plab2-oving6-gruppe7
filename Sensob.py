
class Sensob:

    def __init__(self):
        self.sensor_list = []

    def update(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def add_sensor(self, sensor):
        raise NotImplementedError
