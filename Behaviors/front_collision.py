import behavior


class FrontCollision(behavior.Behavior):
    def sense_and_act(self):
        value = self.sensob.get_value()
        # If distance to object is more than 100cm, then this behavior is not important
        self.match_degree = (100 - value)/100 if value <= 100 else 0.01
        print("Avstand: ", value)
        if value < 15:
            self.motor_recommendation = ['T', 0]
        else:
            self.motor_recommendation = ['F', 0]
