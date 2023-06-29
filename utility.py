import cv2
import numpy as np
from random import randint

def drawCircle(image, center: tuple, radius: int, color: tuple):
    cv2.circle(image, center, radius, color, -1)    


def createBlankImage(image_shape):
    return np.ones(image_shape, np.uint8) * 255


def showImage(image, title="iamge"):
    cv2.imshow(title, image)
    cv2.waitKey(0)


def randomColor():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def readImage(path, image_size):
    image = cv2.imread(path)
    return cv2.resize(image, image_size)