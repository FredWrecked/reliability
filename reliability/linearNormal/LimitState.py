import numpy as np
import reliability.linearNormal as ln


class LimitState:
    def __init__(self, constant=0):
        self.constant = constant
        self.variables = []

    def add_variable(self, name, loc, scale, constant=1, is_resistance=True):
        if is_resistance:
            self.variables.append(ln.Variable(name, loc, scale, constant))
        else:
            self.variables.append(ln.Variable(name, loc, scale, -constant))

    def beta(self):
        mean = self.constant
        variance = 0
        for variable in self.variables:
            mean += variable.loc*variable.constant
            variance += (variable.scale*variable.constant)**2
        std = variance ** 0.5
        print(mean, std)
        return mean / std
