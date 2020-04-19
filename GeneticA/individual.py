import random


class Individual:

    def __init__(self, lower_bound, upper_bound):

        if len(lower_bound) != len(upper_bound):
            raise ValueError('yuor lowe bound and uppe bound not same lemgth')

        self.position = []
        for i in range(len(lower_bound)):
            self.position.append(random.uniform(lower_bound[i], upper_bound[i]))

        self.fitness = None
