import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = [item for key, value in kwargs.items() for item in [key] * value]

    def draw(self, num_balls_draw):
        if num_balls_draw > len(self.contents):
            return self.contents
        else:
            return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls_draw)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    contents = copy.copy(hat.contents)
    many_times = 0
    for _ in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        if all(key in drawn and drawn.count(key) >= expected_balls[key] for key in expected_balls):
            many_times += 1
        hat.contents = copy.copy(contents)
    return many_times / num_experiments
