import behavior


class FollowLine(behavior.Behavior):
    def __init__(self, bbcon, priority):
        super().__init__(bbcon, priority)
        self.match_degree = 1

    def sense_and_act(self):
        value = self.sensob.get_value()
        self.match_degree = 0.9
        if max(value) < 0.2:
            self.motor_recommendation = ['L', 90]
        elif value[2] < 0.2 or value[3] < 0.2:
            self.motor_recommendation = ['F', 0]
            self.match_degree = 0.1
        elif value[0] < 0.2:
            self.motor_recommendation = ['L', 15]
        elif value[1] < 0.2:
            self.motor_recommendation = ['L', 8]
            self.match_degree = 0.7
        elif value[-1] < 0.2:
            self.motor_recommendation = ['R', 15]
        elif value[-2] < 0.2:
            self.motor_recommendation = ['R', 8]
            self.match_degree = 0.7
        else:
            self.motor_recommendation = ['B', 0]
