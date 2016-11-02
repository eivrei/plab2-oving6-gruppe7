
class Sensob:

    def __init__(self):
        self.sensor_list = []
        self.value_list = []


    def update(self):
        for sensor in self.sensor_list:
            sensor.update()
            get_valuelist.append(sensor.get_value())


    def reset_sensors(self):
        for sensor in sensor_list:
            sensor.reset()


    def add_sensor(self, sensor):
        get_sensorlist.append(sensor)


    def get_sensorlist(self): #unødvendig?
        return self.sensor_list


    def get_valuelist(self): #unøvendig?
        return self.get_valuelist
