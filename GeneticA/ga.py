from GeneticA.individual import Individual
import random


class GA:

    def __init__(self, pop_size, lower_bound, upper_bound, func, num_iterations):

        self.func = func
        self.num_iterations = num_iterations
        self.population = []
        self.pop_size = pop_size
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

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
                pa = self.select_with_replacement()
                pb = self.select_with_replacement()
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

    def select_with_replacement(self, t=2):

        best = random.choice(self.population)
        for i in range(1, t):
            nxt = random.choice(self.population)
            if nxt.fitness < best.fitness:
                best = nxt
        return best
