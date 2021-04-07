import copy


class Particle:
    def __init__(self, gene, fFitness, velocity, rule, rounder, W, C1, C2):
        self.gene = gene[:]
        self.Pbest = gene[:]
        self.calcfitness = fFitness
        self.rule = rule
        self.rounder = rounder
        self.velo = velocity
        self.fitness = self.calcfitness()
        self.Pbestfitness = self.fitness
        self.w = W
        self.c1 = C1
        self.c2 = C2

    def __str__(self):
        return str(self.gene)+" "+str(self.fitness)

    def move(self):
        pass

    @staticmethod
    def generaterandom(fFitness, velocity, rule, rounder, W, C1, C2):
        return Particle([], fFitness, velocity, rule, rounder, W, C1, C2)
