import copy
import random
# import Tester
# assumption all func need gene x and y
# x and y can have difference range
# fitness func is input


class Chromosome:
    def __init__(self, Gene, fFitness, rule, rounder):

        self.gene = [round(x, rounder) for x in Gene]
        self.fFitness = fFitness
        self.fitness = self.calcfit()
        self.rule = rule
        self.rounder = rounder
        # print(self.gene, self.fitness)

    def __str__(self):
        return str(self.gene)+" "+str(self.fitness)

    def calcfit(self):
        return self.fFitness(self.gene)

    def mate(self, partner):
        descendant1 = copy.deepcopy(self.gene)
        descendant2 = copy.deepcopy(partner.gene)
        for i in range(len(self.gene)):
            if(random.random() > 0.5):
                descendant1[i], descendant2[i] = descendant2[i], descendant1[i]
        return Chromosome(descendant1, self.fFitness, self.rule, self.rounder), Chromosome(descendant2, self.fFitness, self.rule, self.rounder)

    def mutate(self):
        descendant = copy.deepcopy(self.gene)
        for i in range(len(descendant)):
            descendant[i] = random.uniform(self.rule[i][0], self.rule[i][1])
            # if(descendant[i] > self.rule[i][1]):
            #     descendant[i] -= (self.rule[i][1]-self.rule[i][0])
        return Chromosome(descendant, self.fFitness, self.rule, self.rounder)

    @staticmethod
    def generaterandom(xgene, fFitness, rule, rounder):
        return Chromosome(copy.deepcopy([random.uniform(rule[i][0], rule[i][1])
                                         for i in range(xgene)]), fFitness, rule, rounder)
