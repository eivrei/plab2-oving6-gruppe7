
class Sensob:
    def __init__(self):
        self.sensor_list = []
        self.value_list = []

    def update(self):
        for sensor in self.sensor_list:
            sensor.update()
            self.value_list.append(sensor.get_value())

    def reset_sensors(self):
        for sensor in self.sensor_list:
            sensor.reset()

    def add_sensor(self, sensor):
        self.sensor_list.append(sensor)

    def get_sensorlist(self):
        return self.sensor_list

    def get_valuelist(self):
        return self.get_valuelist
