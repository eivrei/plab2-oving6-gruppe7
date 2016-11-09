import behavior


class FrontCollision(behavior.Behavior):
    def sense_and_act(self):
        value = round(self.sensob.get_value(),2)
        # If distance to object is more than 6cm, then this behavior is not important
        self.match_degree = 1 if value <= 10 else 0.01
        if value < 10:
            self.motor_recommendation = ['S', 0]
        else:
            self.motor_recommendation = ['F', 0]
