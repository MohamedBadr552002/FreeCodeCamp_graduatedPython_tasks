import copy
import random
# Consider using the modules imported above.

class Hat:
    '''
    The Hat class takes a variable number of keyword arguments (**kwargs) that specify the number of balls of each color in the hat.
    '''
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for i in range(count):
                self.contents.append(color)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        balls_drawn = []
        for i in range(num_balls):
            index = random.randint(0, len(self.contents) - 1)
            balls_drawn.append(self.contents.pop(index))
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    succ_experiments = 0  # keeps track of the number of successful experiments.
    for i in range(num_experiments):
        #In each experiment, the function creates a deep copy of the hat object to avoid modifying the original object.
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        success = True
        for color, count in expected_balls.items():
            if balls_drawn.count(color) < count:
                success = False
                break
        if success:
            succ_experiments += 1
    return succ_experiments / num_experiments
