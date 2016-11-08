import behavior


class CheckWall(behavior.Behavior):
    def consider_activation(self):
        if self.bbcon.get_wall():
            return super().consider_activation()
        return False

    def consider_deactivation(self):
        if not self.bbcon.get_wall():
            self.bbcon.deactivate_behavior(self)
            return True
        return False

    def sense_and_act(self):
        colors = self.get_main_color(self.sensob.get_value())
        print(colors)
        if colors[1] > 140 and colors[0] < 100 and colors[2] < 60:
            self.halt_request = True
            self.motor_recommendation = ['S', 0]
        else:
            self.motor_recommendation = ['T', 160]
        self.match_degree = 1

    def get_main_color(self, img):
        colors = img.getcolors(10000) #put a higher value if there are many colors in your image
        max_occurence, most_present = 0, 0
        try:
            for c in colors:
                if c[0] > max_occurence:
                    (max_occurence, most_present) = c
            return most_present
        except TypeError:
            print("TypeError getting main color in picture")