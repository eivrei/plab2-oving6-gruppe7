import behavior

class SideCollision(behavior.Behavior):
    def sense_and_act(self):
        value = self.sensob.get_value()
        self.match_degree = 1 if value[0] or value[1] else 0
        if value:
            self.motor_recommendation = ['T', 180]
        else:
            self.motor_recommendation = ['F', 0]
