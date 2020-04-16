from .individual import Individual
import random
from .selection import TournamentSelection


'''To do list: 
        
        -Variable mutations
        -Variable mutation chance
        -Add in different selection algorithms
        -Are you writing this for an end user to be able to input their own algorithms?
        -Different optimisation algorithms
        -Different crossover methods

'''
class GA:

    def __init__(self, pop_size, lower_bound, upper_bound, func, num_iterations, selection=None):

        self.func = func
        self.num_iterations = num_iterations
        self.population = []
        self.pop_size = pop_size
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.selection = TournamentSelection()

        for i in range(pop_size):
            self.population.append(Individual(lower_bound, upper_bound))

        self.best = None

    def optimise(self):

        for i in range(self.num_iterations):

            for individual in self.population:
                self.assess_fitness(individual)

                if self.best is None or individual.fitness < self.best.fitness:
                    self.best = individual

            new_pop = []
            for i in range(self.pop_size//2):

                pa = self.selection.select(population=self.population)
                pb = self.selection.select(population=self.population)

                ca, cb = self.crossover(pa, pb)
                new_pop.append(self.mutate(ca))
                new_pop.append(self.mutate(cb))

            self.population = new_pop

        print(self.best.position)
        print(self.best.fitness)

    def assess_fitness(self, individual):
        individual.fitness = self.func(individual.position)

    def crossover(self, pa, pb):

        c = random.randint(1, len(pa.position))
        if c != 1:
            for i in range(c, len(pa.position)):
                pa.position[i], pb.position[i] = pb.position[i], pa.position[i]
        return pa, pb

    def mutate(self, child):

        for i in range(len(child.position)):

            child.position[i] = child.position[i] * random.uniform(0.9, 1.1)
            if child.position[i] > self.upper_bound[i]:
                child.position[i] = self.upper_bound[i]
            if child.position[i] < self.lower_bound[i]:
                child.position[i] = self.lower_bound[i]

        return child

    @staticmethod
    def tournament_selection(population, t=2):

        best = random.choice(population)
        for i in range(1, t):
            nxt = random.choice(population)
            if nxt.fitness < best.fitness:
                best = nxt
        return best
