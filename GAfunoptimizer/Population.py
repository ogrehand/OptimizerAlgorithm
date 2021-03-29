# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:17:48 2021

@author: Tobing Setyawan
"""

# https://en.wikipedia.org/wiki/Test_functions_for_optimization
import Chromosome as chro
import math
import copy
import random


class Population:

    def __init__(self, Popsize, CR, MR, xchro, fFitness, Rule, rounder):
        self.popsize = Popsize
        self.cr = CR
        self.mr = MR
        self.xchro = xchro
        self.fFitness = fFitness
        self.rule = Rule
        self.rounder = rounder
        self.pool = sorted([chro.Chromosome.generaterandom(self.xchro, self.fFitness, self.rule, self.rounder)
                           for i in range(0, self.popsize)], key=lambda x: x.fitness, reverse=False)

    def __str__(self):
        return str(self.pool[0].gene)+" "+str(self.pool[0].fitness)

    def evolve(self):
        descendants = []
        cros = math.floor((self.cr * self.popsize) / 2)
        muta = math.floor(self.mr * self.popsize)
        i = 0
        while i < cros:
            par1 = random.randint(0, self.popsize-1)
            par2 = random.randint(0, self.popsize-1)
            while par1 == par2:
                par2 = random.randint(0, self.popsize-1)
            descendants.extend(self.pool[par1].mate(self.pool[par2]))
            i += 1
            # print(i,len(descendants),descendants[len(descendants)-1],descendants[len(descendants)-2])
        i = 0
        while i < muta:
            descendants.append(
                self.pool[random.randint(0, self.popsize-1)].mutate())
            i += 1
        descendants += self.pool
        self.pool = sorted(descendants, key=lambda x: x.fitness, reverse=False)[
            :self.popsize]

    def random_injection(self, percent):
        # percent positive round number between 1 to 100
        self.pool = sorted(self.pool[:math.ceil((100-percent)*self.popsize/100)] + [chro.Chromosome.generaterandom(self.xchro, self.fFitness,
                           self.rule, self.rounder) for i in range(math.ceil((percent)*self.popsize/100))], key=lambda x: x.fitness, reverse=False)
