
class Bbcon:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = set()
        self.sensobs = []
        self.motob = None
        self.arbitrator = None
        self.wall = False

    # Add behavior to self.behaviors
    def add_behavior(self, behavior):
        self.behaviors.extend(behavior)

    # Add sensob to self.sensobs
    def add_sensob(self, sensob):
        self.sensobs.extend(sensob)

    # Add behavior to active_behaviors
    def activate_behavior(self, behavior):
        self.active_behaviors.add(behavior)

    # Remove behavior from active_behaviors
    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    # Return if behavior is active
    def behavior_is_active(self, behavior):
        return behavior in self.active_behaviors

    def get_wall(self):
        return self.wall

    # Main function of the bbcon object. Does all the heavy lifting
    def run_one_timestep(self):
        # Run update method in all sensob objects
        def update_sensobs():
            for behavior in self.behaviors:
                if behavior.consider_activation():
                    behavior.sensob.update()

        # Run update method in all behavior objects
        def update_behaviors():
            for behavior in self.behaviors:
                behavior.update()

        # Invoke the arbitrator with arbitrator.choose_action
        # If motor recommendation is ['S',0], set self.wall = True
        # else self.wall = False
        def update_arbitrator():
            motor_recommendation, halt_request = self.arbitrator.choose_action()
            if halt_request:
                # Quit program, dance maybe?
                print("finito")
                return False
            self.wall = True if motor_recommendation[0] == 'S' else False
            update_motobs(motor_recommendation)
            return True

        # Run update method in all motob objects
        def update_motobs(motor_recommendation):
            print(motor_recommendation)
            self.motob.update(motor_recommendation)
            reset_sensobs()

        # Wait while robot is moving for a short period
        # To be implemented?

        # Run reset method in all sensob objects
        def reset_sensobs():
            for sensob in self.sensobs:
                sensob.reset()

        update_sensobs()
        update_behaviors()
        return update_arbitrator()