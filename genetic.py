from utility import *
from constants import *
from random import random, randint, uniform
from copy import deepcopy


class Gen:
    def __init__(self, isCircle=False
                 , coordinates=(0, 0)
                 , color=(0, 0, 0)
                 , radius=0
                 , fitness=0) -> None:
        self.isCircle = isCircle
        self.coordianets = coordinates
        self.color = color
        self.radius = radius
        self.fitness = fitness

def fitness(image, reference):
    fit = 0
    shape = image.shape
    return cv2.PSNR(image, reference)

def createPopulation(n, reference):
    height, width, _ = reference.shape 
    solutions = []
    for i in range(n):
        chromosome = []
        image = createBlankImage(reference.shape)
        for i in range(height * width):
            h = (i) // width
            w = i % width
            gene = Gen(random() < 0.003, (h, w), randomColor(), randint(5, 10))
            if gene.isCircle:
                drawCircle(image, gene.coordianets, gene.radius, gene.color)
            chromosome.append(gene)
        solutions.append((chromosome, image, fitness(image, reference)))
    return solutions

def findSolution(solutions, r):
    fitnessSum = 0
    for solution in solutions:
        fitnessSum += solution[2]

    normalizedFiness = []
    for solution in solutions:
        normalizedFiness.append((solution[0], solution[2] / fitnessSum))

    accumulate = 0
    i = 0
    while accumulate < r:
        accumulate += normalizedFiness[i][1]
        i += 1
    return solutions[i - 1]

def select(solutions):
    r = uniform(0, 1)
    rp = (r + 0.5) % 1
    return findSolution(solutions, r), findSolution(solutions, rp)

def crossover(solution1, solution2, reference):
    chromosome1 = solution1[0]
    chromosome2 = solution2[0]

    childChoromosome1 = deepcopy(chromosome1)
    childChoromosome2 = deepcopy(chromosome2)
    childSolution1 = deepcopy(solution1)
    childSolution2 = deepcopy(solution2)

    cutPoint = randint(1, len(chromosome1))

    childChoromosome1[cutPoint:] = chromosome2[cutPoint:]
    childChoromosome2[cutPoint:] = chromosome1[cutPoint:]

    image = createBlankImage(solution1[1].shape)
    for gene in childChoromosome1:
        if gene.isCircle:
            drawCircle(image, gene.coordianets, gene.radius, gene.color)
    childSolution1 = (childChoromosome1, image, fitness(image, reference))

    image = createBlankImage(solution1[1].shape)
    for gene in childChoromosome2:
        if gene.isCircle:
            drawCircle(image, gene.coordianets, gene.radius, gene.color)
    childSolution2 = (childChoromosome2, image, fitness(image, reference))

    return childSolution1, childSolution2 

def mutation(solution, reference,mutation_probability):
    i = uniform(0, 1)
    if i < mutation_probability:
        print("mutation happend!")
        chromosome = solution[0]

        # color and radius mutation
        i = randint(1, len(chromosome))
        gene = chromosome[i]
        gene.color = randomColor()
        gene.radius = randint(radius_min, radius_max)
        chromosome[i] = gene

        # coordiantes mutation
        swapIndex1 = randint(1, len(chromosome))
        swapIndex2 = randint(1, len(chromosome))
        temp = chromosome[swapIndex2]
        chromosome[swapIndex2] = chromosome[swapIndex1]
        chromosome[swapIndex1] = temp
        
        image = createBlankImage(reference.shape)
        for gene in chromosome:
            if gene.isCircle:
                drawCircle(image, gene.coordianets, gene.radius, gene.color)
        solution = (chromosome, image, fitness(image, reference))
        
    return solution 
