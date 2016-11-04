
class Behavior:

    # -------- Hovedoppgave --------
    # consider activation or deactivation
    # produce motor recommendations
    # update the match degree
    # Obs: ikke kommunisere direkte med andre behaviors


    def __init__(self, bbcon, priority):
        self.bbcon = bbcon # pointer to the controller that uses this behavior
        self.sensob = None # a list of all sensobs that this behavior uses
        self.motor_recommendation = [] # a list of recommendations, one per motob
        self.active_flag = True # boolean variable indicating that the behavior is currently active or inactive
        self.halt_request = None # some behaviors can request the robot to completely halt activity (and thus end the run)
        self.priority = priority # a static, pre-defined value indicating the importance of this behavior
        self.match_degree = 0 # in range (0,1)
        self.weight = self.priority * self.match_degree

    def set_sensob(self, sensob):
        self.sensob = sensob

    def consider_deactivation(self):
        # whenever a behavior is active, it should test whether it should deactivate
        return False

    def consider_activation(self):
        # whenever a behavior is inactive, it should test whether it should activate
        return True

    def update(self):
        # 1) update the activity status (different implementation for the behaviors)
        self.active_flag = not self.consider_deactivation() if self.active_flag else self.consider_activation()
        # 2) call sense_and_act
        self.sense_and_act()
        # 3) update the behavior's weight (
        self.weight = self.priority * self.match_degree

    def sense_and_act(self):
        # read self.sensobs to produce motor recommendations (and halt requests)
        raise NotImplementedError
