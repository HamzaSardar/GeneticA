from GeneticA.individual import Individual


class GA:

    def __init__(self, pop_size):

        population = []
        for i in range(0, pop_size):
            population.append(Individual)

        best = None

    def genetic_algorithm(self, pop_size, population, best):

    #   How to make this run until 'best' is the ideal solution?
    #   leave code indented for now

        for individual in population:

            self.assess_fitness(individual)
            if individual.fitness > best.fitness:
                best = individual
            # why is none showing an error? possibly change this
            # loop to a for i in range, then just leave below as
            # the case where i =0
            elif best.fitness = None:
                best = individual

        new_pop = []

        for i in range(pop_size/2):

            pa = self.select_with_replacement(population)
            pb = self.select_with_replacement(population)
            ca = self.crossover(pa, pb)
            cb = self.crossover(pa, pb)
            new_pop.append(ca)
            new_pop.append(cb)

        population = new_pop


    def assess_fitness(self):

    def crossover(self):

    def mutate(self):

    def select_with_replacement(self):
