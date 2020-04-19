import abc
import random


class BaseSelection(abc.ABC):

    @abc.abstractmethod
    def select(self, population):
        raise NotImplementedError('BaseSelection::select()')


class TournamentSelection(BaseSelection):

    def __init__(self, t=2):
        super().__init__()

        if t < 1:
            raise ValueError('t must be >= 1')

        self.t = t

    def select(self, population):

        best = random.choice(population)
        for i in range(1, self.t):
            nxt = random.choice(population)
            if nxt.fitness < best.fitness:
                best = nxt
        return best


class FitnessPropSelection(BaseSelection):

    def __init__(self):
        super().__init__()

    def select(self, population):
        pop = population
        global_f = pop.fitness

        for i in global_f:
            if i == 0:
                i = 1

        for i in range(2, len(global_f)):
            global_f[i] = global_f[i] + global_f[i - 1]

        n = random.randint(0, global_f[-1])
        for i in range(1, len(global_f)):
            # how to do this for minimum fitness?
            # following feels incorrect
            if i < len(global_f):
                if global_f[i] < n < global_f[i + 1]:
                    return pop[i]
