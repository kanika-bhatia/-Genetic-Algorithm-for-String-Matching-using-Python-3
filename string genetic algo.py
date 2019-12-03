import numpy as np
import random as rd

listy=list(input('Enter string '))
popusize=int(input('Enter population size '))
parsize=int(input('Enter selection size '))
if parsize%2 == 1:
    parsize = parsize - 1
#print('listy',listy)

def initial(popusize,listy):
    #global popusize,listy
    population=[]
    twisty=[]
    for i in range(ord('a'), (ord('z')+1)):
        twisty.append(chr(i))
    #print(twisty)

    for i in range(popusize):
        listy1=[]
        for j in range(0, len(listy)):
            listy1.append(rd.choice(twisty))
        while listy1 in population:
            listy1=[]
            for j in range(0, len(listy)):
                listy1.append(rd.choice(twisty))
        #print('listy1',listy1)
        population.append(listy1)
    return population, twisty
    

def fitness(listy,population):
    score=[]
    for index in range(len(population)):
        temp=population[index]
        diff=0
        diffy = []
        for j in range(0, len(temp)):
            var1 = temp[j]
            var2 = listy[j]
            val1 = ord(var1)
            val2 = ord(var2)
            diff = diff + abs(val2-val1)
            diffy.append((diff,abs(val2-val1),val1,val2,var1,var2))
        score.append([diff, index])
##        if diffy[len(listy)-1][0]==0:
##            print(diffy)
##            print()
    return score


def selection(parsize,population):
    parents=[]
    mini=[]
    for i in range(parsize):
        value = min(score)
        mini.append(value)
        score.remove(value)
    #print('mini', mini)

    for i,j in mini:
        memp=population[j]
        parents.append(memp)
    #print('parents', parents)
    return parents


def crossover(parents,population):
    new_population = []
    new_population.extend(parents)
    while len(new_population)<len(population):
        parent1=rd.choice(parents)
        parent2=rd.choice(parents)
        length = len(parent1)//2
        offspring1 = parent1[:length] + parent2[length:]
        offspring2 = parent2[:length] + parent1[length:]
        new_population.append(offspring1)
        new_population.append(offspring2)
    return new_population



def mutation(new_population,twisty):
    for i in range(len(new_population)):
        position = rd.choice(range(len(new_population[i])))
        new_population[i][position] = rd.choice(twisty)               
    return new_population
                     



population, twisty = initial(popusize,listy)
#print('population',population)

generation  = 0
while True:
    generation += 1
    print('generation',generation)
    score = fitness(listy,population)
    #print('score', score)
    print('one',min(score))
    print(population[min(score)[1]])

    if min(score)[0] == 0:
        print('final',population[min(score)[1]])
        break
    
    parents=selection(parsize,population)
    #print('parents ', parents)
    
    new_population=crossover(parents,population)
    #print('cross',new_population)
    
    score = fitness(listy,new_population)

    print('two',min(score))
    print(population[min(score)[1]])
    
    if min(score)[0] == 0:
        print('final',population[min(score)[1]])
        break
    
    new_population=mutation(new_population,twisty)
    #print('mutate',new_population)

    population = new_population

    
    
