class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.stochastic = None

    def choose_action(self):
        # Check active_behaviors
        # Pick the winner:
        winner_weight = 0
        winner = None
        for behavior in self.bbcon.active_behaviors:
            print("vekt: ", behavior.weight, "pri: ", behavior.priority)
            if behavior.halt_request:
                return ['S', 0], True
            if behavior.weight > winner_weight:
                winner_weight = behavior.weight
                winner = behavior
        return winner.motor_recommendation, False