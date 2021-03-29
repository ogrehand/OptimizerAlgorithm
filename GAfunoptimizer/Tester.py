import math
import Population
# beale function
# -4.5 <= x,y <= 4.5


def bealefunc(n):
    # max at 3,0.5 =>0
    x = n[0]
    y = n[1]
    return (1.5-x+(x*y))**2+(2.25-x+(x*y**2))**2+(2.625-x+(x*y**3))**2

# [-5.12,5.12]


def rastriginfunc(n):
    # max at 0,0 =>0
    x = n[0]
    y = n[1]
    A = 10
    return A*2 + (x**2-A*math.cos(2*math.pi*x))+(y**2-A*math.cos(2*math.pi*y))


def himmelblaufunc(n):
    # -5 <= x,y <= 5
    # min at 3.0        2.0
    # min at -2.805118  3.131312
    # min at -3.779310  -3.283186
    # min at 3.584428   -1.848126
    x = n[0]
    y = n[1]
    return (x**2+y-11)**2 + (x+y**2-7)**2


# populate = Population.Population(1000, 0.5, 0.5, 2, rastriginfunc, [[-5.12, 5.12],
#                                                                     [-5.12, 5.12]], 2)
populate = Population.Population(1000, 0.5, 0.5, 2, himmelblaufunc, [[-5, 5],
                                                                    [-5, 5]], 2)

print(-1, populate)

for i in range(10000):
    populate.evolve()
    print(i, populate)
    if(i % 10 == 0 and i != 0):
        populate.random_injection(30)
        print("random inject ", populate)
    if(populate.pool[0].fitness == 0):
        print("berhenti")
        break


# print("mating")
# print(populate.pool[0])
# print(populate.pool[1])
# populate.pool[0].mate(populate.pool[1])

# print("mutate")
# print(populate.pool[0])
# populate.pool[0].mutate()
