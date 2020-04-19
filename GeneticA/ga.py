from .individual import Individual
import random
from .selection import TournamentSelection
from .crossover import SinglePointCrossover
class GA:

    def __init__(self, pop_size, lower_bound, upper_bound,
                 func, num_iterations):

        self.func = func
        self.num_iterations = num_iterations
        self.population = []
        self.pop_size = pop_size
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.selection = TournamentSelection()
        self.crossover = SinglePointCrossover()
        self.initialise_population()
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

                ca, cb = self.crossover.cross(pa, pb)

                new_pop.append(self.mutate(ca))
                new_pop.append(self.mutate(cb))

            self.population = new_pop

        print(self.best.position)
        print(self.best.fitness)

    def assess_fitness(self, individual):
        individual.fitness = self.func(individual.position)

    def mutate(self, child):

        for i in range(len(child.position)):

            child.position[i] = child.position[i] * random.uniform(0.9, 1.1)
            if child.position[i] > self.upper_bound[i]:
                child.position[i] = self.upper_bound[i]
            if child.position[i] < self.lower_bound[i]:
                child.position[i] = self.lower_bound[i]

        return child

    def initialise_population(self):

        for i in range(self.pop_size):
            self.population.append(
                Individual(self.lower_bound, self.upper_bound)
            )