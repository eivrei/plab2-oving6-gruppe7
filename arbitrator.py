import random

class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.stochastic = None

    # def pick_behavior(self):
    #     weights = 0
    #     weights += self.bbcon.weight
    #     nr = random.randrange(weights)

    # Check active_behaviors and pick the winner
    # Return tuple with motor recommendations and a boolean indicating whether the run should be halted or not
    def choose_action(self):
        pass

