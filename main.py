import cv2
import numpy as np
from random import randint, getrandbits, random
from utility import *
from genetic import *

inputPath = "./test.png"
refrence = cv2.imread(inputPath)

image = createBlankImage(refrence.shape)
height, width, _ = image.shape

product = np.prod(refrence.shape[:2])

chromosome = []
for i in range(product):
    gene = Gen(random() < 0.001, (randint(0, height), randint(0, width)), randomColor(), randint(1, 20))
    chromosome.append(gene)
    if gene.isCircle:
        drawCircle(image, gene.coordianets, gene.radius, gene.color)

showImage(image)
