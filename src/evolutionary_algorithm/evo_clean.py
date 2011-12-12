#!/usr/bin/python

import random
import string

class Candidate(object):
    """
    Class representing an 'organism' with a fitness, which can be mutated and
    generate offspring. To change the fitness function or use different
    mutation probabilities and distances, you can inherit from this class and
    override the fitness() and mutate() methods.
    """
    def __init__(self, genotype, target):
        """
        Create a new Canidate class with `genotype` (a string of letters
        representing DNA) and a `target` string (for use in the `fitness()`
        function.
        """
        self.genotype = list(genotype)
        self.target = target

    def fitness(self):
        """
        Calculate the fitness of the candidate and return it. Fitness of 0
        indicates the end target has been reached. The higher the fitness
        value, the more unfit the candidate.
        """
        fitval = 0
        for i in range(0, len(self.genotype)):
            fitval += (ord(self.target[i]) - ord(self.genotype[i])) ** 2
        return(fitval)

    def mutate(self, probability=0.1, distance=1):
        """
        Mutate the genotype of our Candidate. The `probability` is a real number
        between 0 and 1 which indicates the probability of each element
        (character) in the genotype to mutate. The `distance` determines the maximum
        distance of the mutation (decrease or increase of the character's
        value).
        """
        for pos in range(len(self.genotype)):
            if random.random() < probability:
                self.genotype[pos] = chr(
                    ord(self.genotype[pos]) + random.randint(-distance, distance)
                )

    def crossover(self, partner):
        """
        Crossover (mixing of genotype) between this candidate and a partner
        candidate. This produces (returns) a new child candidate. The crossover
        is performed by taking a copy of this candidates genotype and
        overlapping it with a random part of the partner's genotype.
        """
        start = random.randint(0, len(partner.genotype) - 1)
        end = random.randint(0, len(partner.genotype) -1)
        if start > end:
            stop, end = start, end
        child_genotype = self.genotype[:]
        child_genotype[start:end] = partner.genotype[start:end]
        return(self.__class__(child_genotype, self.target))

    def __repr__(self):
        return('%7i  %s' % (self.fitness(), ''.join(self.genotype)))

class Population(object):
    """
    The Population class represents a population of competing `organisms`
    (Candidates).
    """
    def __init__(self, candidate, target, size=20, max_generations=5000):
        """
        Create a new population of `size` candidates. The `candidate` param is
        a reference to a class to be used as the candidate. `target` is the
        target genotype for the evolutionary algorithm. `max_generations` is
        the maximum number of generations to produce, after which (if no
        candidate has evolved that matches the target) the evolutionary
        emulation is terminated.
        """
        self.candidate = candidate
        self.size = size
        self.target = target
        self.generation = 0
        self.population = self.gen_population(self.size)
        self.max_generations = max_generations

    def evolve(self):
        """
        Evolve the population until a candidate is evolved with a fitness of 0
        or until `self.max_generations` is reached. Returns the number of
        generations required to reach the target or False if the target wasn't
        reached within `max_generations`.
        """
        while True:
            self.population.sort(key = lambda candidate: candidate.fitness())

            if self.population[0].fitness() == 0:
                return(self.generation)

            if self.generation == self.max_generations:
                return(False)

            self.generation += 1

            rnd1 = int(random.random() * random.random() * (self.size -1))
            rnd2 = int(random.random() * random.random() * (self.size -1))
            parent1 = self.population[rnd1]
            parent2 = self.population[rnd2]
            child = parent1.crossover(parent2)
            child.mutate()

            if child.fitness() < self.population[-1].fitness():
                self.population[-1] = child

    def gen_candidate(self, target):
        """
        Generate a random candidate.
        """
        return(
            self.candidate(
                [random.choice(string.printable[:-5]) for j in range(len(target))],
                target
            )
        )

    def gen_population(self, size):
        """
        Generate a population of `size` using `self.gen_candidate()`.
        """
        population = []
        for i in range(size):
            population.append(self.gen_candidate(self.target))
        return(population)

    def __repr__(self):
        return(
            '\n'.join(
                ['%7i  %7i  %s' % (self.generation, c.fitness(), ''.join(c.genotype)) for c in self.population]
            )
        )

def run(target, probability, distance):
    """
    Evolve a population to the target with user-defined probability and
    distance.
    """
    class CustomCandidate(Candidate):
        def mutate(self, probability=probability, distance=distance):
            return(Candidate.mutate(self, probability, distance))

    population = Population(CustomCandidate, target)
    generations = population.evolve()

    tmpl = "Target %s (probability=%f, distance=%i) within %i generations"
    if not generations:
        tmpl = tmpl % ("not reached", probability, distance, population.generation)
    else:
        tmpl = tmpl % ("reached", probability, distance, population.generation)
    print tmpl

run('Hello, World!', 0.1, 1)
run('Hello, World!', 0.5, 1)
run('Hello, World!', 0.7, 1)
run('Hello, World!', 0.1, 2)
run('Hello, World!', 0.5, 2)
run('Hello, World!', 0.7, 2)
run('Hello, World!', 0.1, 4)
run('Hello, World!', 0.5, 4)
run('Hello, World!', 0.7, 4)
