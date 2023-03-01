import matplotlib.pyplot as plt
import scipy.stats as ss
import numpy as np


class Normal:
    # Constructor method
    def __init__(self, loc, scale, name):
        self.loc = loc
        self.scale = scale
        self.name = name

    def plot(self):
        zs = np.arange(-3, 3.1, 0.1)
        xs = zs * self.scale + self.loc
        ys = ss.norm.pdf(xs, self.loc, self.scale)
        plt.plot(xs, ys)
