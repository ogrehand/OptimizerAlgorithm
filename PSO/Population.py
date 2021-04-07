import Particle as part
import copy


class Population:
    def __init__(self, popsize, fFitness, velocity, rule, rounder, W, C1, C2):
        self.popsize = popsize
        self.pool = [part.Particle.generaterandom(fFitness, velocity, rule, rounder, W, C1, C2)
                     for i in range(self.popsize)]
        self.Gbest = copy.deepcopy(self.pool[0].Pbest)
        self.Gbestfitness = self.pool[0].Pbestfitness

    def updateAll(self):
        pass
