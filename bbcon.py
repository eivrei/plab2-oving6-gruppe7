
class Bbcon:
    def __init__(self):
        self.behaviors = set()
        self.active_behaviors = set()
        self.sensobs = set()
        self.motobs = set()
        self.arbitrator = None

    # Add behavior to self.behaviors
    def add_behavior(self, behavior):
        self.behaviors.add(behavior)

    # Add sensob to self.sensobs
    def add_sensob(self, sensob):
        self.sensobs.add(sensob)

    # Add behavior to active_behaviors
    def activate_behavior(self, behavior):
        self.active_behaviors.add(behavior)

    # Remove behavior from active_behaviors
    def deactivate_behavior(self, behavior):
        self.active_behaviors.remove(behavior)

    # Return if behavior is active
    def behavior_is_active(self, behavior):
        return behavior in self.active_behaviors

    # Main function of the bbcon object. Does all the heavy lifting
    def run_one_timestep(self):
        # Run update method in all sensob objects
        def update_sensobs():
            pass

        # Run update method in all behavior objects
        def update_behaviors():
            pass

        # Invoke the arbitrator with arbitrator.choose_action
        # To be implemented...

        # Run update method in all motob objects
        def update_motobs():
            pass

        # Wait while robot is moving for a short period
        # To be implemented...

        # Run reset method in all sensob objects
        def reset_sensobs():
            pass