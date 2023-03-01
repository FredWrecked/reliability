import reliability.linearNormal as ln


class Variable:
    # Constructor method
    def __init__(self, name, loc, scale, constant):
        self.name = name
        self.loc = loc
        self.scale = scale
        self.constant = constant

    def plot(self):
        ln.Normal(self.loc, self.scale, self.name).plot()
