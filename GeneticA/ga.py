from GeneticA.individual import Individual

# a = GA(50, [-100], [100])
#needs function to optimise, number of iterations as well as pop size and search space
class GA:

    def __init__(self, pop_size, lower_bound, upper_bound, func, num_iterations):

        self.func = func
        self.num_iterations = num_iterations
        self.population = []
        self.pop_size = pop_size

        for i in range(pop_size):
            self.population.append(Individual(lower_bound, upper_bound))

        self.best = None

    def optimise(self):

        for individual in self.population:

            self.assess_fitness(individual)

            if self.best is None or individual.fitness > self.best.fitness:
                self.best = individual

        new_pop = []

        for i in range(self.pop_size/2):

            pa = self.select_with_replacement()
            pb = self.select_with_replacement()
            ca = self.crossover(pa, pb)
            cb = self.crossover(pa, pb)
            new_pop.append(ca)
            new_pop.append(cb)

        self.population = new_pop

    def assess_fitness(self, individual):
        individual.fitness = self.func(individual.position)

    def crossover(self, pa, pb):
        pass

    def mutate(self):
        pass

    def select_with_replacement(self):
        pass
