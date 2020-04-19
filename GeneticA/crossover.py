import abc
import random


class BaseCrossover(abc.ABC):

    @abc.abstractmethod
    def cross(self, pa, pb):
        raise NotImplementedError('BaseCrossover::cross()')


class SinglePointCrossover(BaseCrossover):

    def cross(self, pa, pb):

        c = random.randint(1, len(pa.position))

        if c != 1:
            for i in range(c, len(pa.position)):
                pa.position[i], pb.position[i] = pb.position[i], pa.position[i]

        return pa, pb

