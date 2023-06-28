class Gen:
    def __init__(self, isCircle=False
                 , coordinates=(0, 0)
                 , color=(0, 0, 0)
                 , radius=0) -> None:
        self.isCircle = isCircle
        self.coordianets = coordinates
        self.color = color
        self.radius = radius


def fitness(image, refrence):
    fit = 0
    shape = image.shape

    for x in range(shape[0]):
        for y in range(shape[1]):
            fit += sum(image[x, y] - refrence[x, y])

    return fit