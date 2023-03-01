# This is a sample Python script.


import reliability.linearNormal as ln


ls = ln.LimitState()
ls.add_variable("r", 100, 10, 1, True)
ls.add_variable("q", 80, 8, 1, False)

print(ls.beta())
