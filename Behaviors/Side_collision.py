import behavior

class SideCollision(behavior.Behavior):
    def sense_and_act(self):
        value = self.sensob.get_value()
        self.match_degree = 1 if value else 0
        if value:
            self.motor_recommendation = ['B', 0]
        else:
            self.motor_recommendation = ['F', 0]