
class Bbcon:
    def __init__(self):
        self.behaviors = set()
        self.active_behaviors = set()
        self.sensobs = set()
        self.motobs = set()
        self.arbitrator = None

    def add_behavior(self, behavior):
        self.behaviors.add(behavior)

    def add_sensob(self, sensob):
        self.sensobs.add(sensob)

    def activate_behavior(self, behavior):
        self.active_behaviors.add(behavior)

    def deactivate_behavior(self, behavior):
        self.active_behaviors.remove(behavior)

    def behavior_is_active(self, behavior):
        return behavior in self.active_behaviors

    def run_one_timestep(self):
        def update_sensobs():
            pass

        def update_behaviors():
            pass

        # Invoke the arbitrator with arbitrator.choose_action

        def update_motobs():
            pass

        # Wait while robot is moving for a short period

        def reset_sensobs():
            pass