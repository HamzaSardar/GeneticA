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
