from basic_robot.motors import Motors


class Motob:
    def __init__(self):
        # self.motor = Motors()
        self.value = None
        # @ 50% speed, 360 degree turn takes 3 sec.
        # 10 degree turn @ 50 % takes 3/360 * 10
        self.time_per_degree = 3/360

    def update(self, motor_rec):
        self.value = motor_rec
        self.operationalize()

    def operationalize(self):
        motor = Motors()
        print(self.value)
        if self.value[0] == "T":
            motor.backward(0.3, 0.2)
            print(self.time_per_degree*self.value[1])
            motor.right(0.5, self.time_per_degree * self.value[1])
        elif self.value[0] == "L":
            motor.left(0.5, self.time_per_degree * self.value[1])
            # motor.set_value([.1, .3], self.time_per_degree * self.value[1])
        elif self.value[0] == "R":
            motor.right(0.5, self.time_per_degree * self.value[1])
            # motor.set_value([.3, .1], self.time_per_degree * self.value[1])
        elif self.value[0] == "F":
            motor.forward(0.3, 0.25)
        elif self.value[0] == 'B':
            motor.backward(0.3, 0.4)

        # self.motor.left(0.5, self.time_per_degree * 180)
        # self.motor.right(0.5, self.time_per_degree * 180)
        # self.motor.forward(0.5, 1)
        # self.motor.backward(0.5, 1)
