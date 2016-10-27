
class Behavior:

    # -------- Hovedoppgave --------
    # consider activation or deactivation
    # produce motor recommendations
    # update the match degree
    # Obs: ikke kommunisere direkte med andre behaviors


    def __init__(self):
        self.bbcon = BBCON() # pointer to the controller that uses this behavior
        self.sensobs = [] # a list of all sensobs that this behavior uses
        self.motor_recommendations = [] # a list of recommendations, one per motob
        self.active_flag = None # boolean variable indicating that the behavior is currently active or inactive
        self.halt_request = None # some behaviors can request the robot to completely halt activity (and thus end the run)
        self.priority = None # a static, pre-defined value indicating the importance of this behavior
        self.match_degree = 0 # in range (0,1)
        self.weight = self.priority * self.match_degree # evt implementere som get-funksjon?


    def consider_deactivation(self):
        # whenever a behavior is active, it should test whether it should deactivate
        if self.active_flag:
            raise NotImplementedError


    def consider_activation(self):
        # whenever a behavior is inactive, it should test whether it should activate
        if not self.active_flag:
            raise NotImplementedError


    def update(self):
        # 1) update the aticity status (different implementation for the behaviors)
        # 2) call sense_and_act
        # 3) update the behavior's weight (
        raise NotImplementedError


    def sense_and_act(self):
        # read self.sensobs to produce motor recommendations (and halt requests)
        raise NotImplementedError