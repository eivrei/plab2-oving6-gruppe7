from basic_robot.motors import Motors


class Motob:
    def __init__(self):
        self.motor = Motors()
        self.value = None
        # @ 50% speed, 360 degree turn takes 3 sec.
        # 10 degree turn @ 50 % takes 3/360 * 10
        self.time_per_degree = round(3 / 360, 4)

    def update(self, motor_rec):
        self.value = motor_rec
        self.operationalize()

    def operationalize(self):
        if self.value[0] == "B":
            self.motor.backward(0.5, 1)
            self.motor.left(0.5, self.time_per_degree * 180)

        elif self.value[0] == "L":
            self.motor.left(0.5, self.time_per_degree * self.value[1])

        elif self.value[0] == "R":
            self.motor.right(0.5, self.time_per_degree * self.value[1])

        elif self.value[0] == "F":
            self.motor.forward(0.5, 1)
