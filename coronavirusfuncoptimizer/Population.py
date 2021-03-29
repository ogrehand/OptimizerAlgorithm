# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:17:48 2021

@author: Tobing Setyawan
"""

# https://pubmed.ncbi.nlm.nih.gov/32716641/
import pandas as pd


class Population:

    def __init__(self, pdie, psupspread, ordinaryrate, superrate, preinfect,
                 pisolation, ptravel, socdist, pandduration, strains):

        #  parameter
        self.P_DIE = pdie
        self.P_SUPERSPREADER = psupspread
        self.ORDINARY_RATE = ordinaryrate
        self.SUPERSPREADER_RATE = superrate
        self.P_REINFECTION = preinfect
        self.P_ISOLATION = pisolation
        self.P_TRAVEL = ptravel
        self.SOCIAL_DISTANCING = socdist
        self.PANDEMIC_DURATION = pandduration
        self.strains = strains
        # initial population
        self.infected = []
        self.newinfected = []
        self.dead = []
        self.recovered = []
        self.time = 0
        # patien zero
        pz = self.generatepz()
        self.bestfitness = 0
        self.bestindividual = pz

    def iteration(self):
        pass

    def infect(self):
        pass

    def newinfection(self):
        pass

    def die(self):
        pass

    def fitnesss(self):
        pass

    @staticmethod
    def generatepz():
        return []


"""
1. patienzero first infection -> local minima/random init
2. disease propagation
    1. die: cannot infect other person
    2. alive: will infect other person
        ordinary spreader: infect new individual by spreadingrate
        superspreader: infect new individual by superspreadingrate
    3. traveling by travel rate
        a. non-traveler and normal spreadingrate
        b. traveler annd normal spreadingrate
        c. traveler and superspreadingrate
3. update populations
    maintain 3 population each generation
    1. death: death individual put here and never be used again
    2. recovered: after infect go to this population
        reinfection based on P_REINFECTION
        isolated individu goes to here based on P_ISOLATION
    3. infected: infected population each generation put here
        - remove repeated individuals
4. stop criteria
    nothing needed because the recovered and the dead will be bigger than infected
    and infected population decays overtime
    - optional PANDEMIC_DURATION to stop iteration
"""

# world = Population()
print("khcvjdtcgj")
