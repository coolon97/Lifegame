import numpy as np


class Lifegame:
    def __init__(self, shape):
        self.WIDTH, self.HEIGHT = shape
        self.__state = np.zeros((self.WIDTH, self.HEIGHT))
        self.random()

    def do(self):
        new = np.zeros((self.WIDTH, self.HEIGHT)).astype(np.uint8)
        for j in range(1, self.HEIGHT-1):
            for i in range(1, self.WIDTH - 1):
                if bool(self.__state[i, j]):
                    if np.sum(self.__state[i - 1:i + 2, j - 1:j + 2]) <= 2:
                        new[i, j] = 0
                    elif 2 < np.sum(self.__state[i - 1:i + 2, j - 1:j + 2]) < 5:
                        new[i, j] = 1
                    elif 5 <= np.sum(self.__state[i - 1:i + 2, j - 1:j + 2]):
                        new[i, j] = 0
                    else:
                        new[i, j] = 1
                else:
                    if np.sum(self.__state[i - 1:i + 2, j - 1:j + 2]) == 3:
                        new[i, j] = 1
                    else:
                        new[i, j] = 0

        self.__state = new
        return self.__state * 255

    def random(self):
        _ = np.array(list(map(lambda x: int(x + 0.5),
                              np.random.rand(self.WIDTH*self.HEIGHT)))).astype(np.uint8)
        _.shape = (self.WIDTH, self.HEIGHT)
        self.__state = _


if __name__ == "__main__":
    life = Lifegame((40, 40))
    life.random()
    count = 0
    while (count <= 80):
        life.do()
        count += 1
