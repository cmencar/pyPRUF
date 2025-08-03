class FuzzySetParameters:
    """
    Class used in pyPRUF library to manage its config
    """
    def __init__(self):
        self.t_norm = min
        self.s_norm = max
        self.complement = lambda x: 1 - x

fuzzy_sets_parameters = FuzzySetParameters()
