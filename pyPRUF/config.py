class FuzzySetParameters:
    def __init__(self):
        self.t_norm = min
        self.s_norm = max
        self.complement = lambda x: 1 - x

fuzzy_sets_parameters = FuzzySetParameters()
