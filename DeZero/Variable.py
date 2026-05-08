import numpy as np
class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError('{} is not supported'.format(type(data)))
        self.data = data
        self.creator = None
        self.grad = None
    def set_creator(self, func):
        self.creator = func
    