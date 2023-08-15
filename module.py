import numpy as np

from node import AbstractNode


class Module:
    def __init__(self, input_layer:AbstractNode=None):
        self.current_layer = input_layer
        self.parameters = None

    def zero_grad(self):
        for param in self.parameters:
            param.grad = np.zeros_like(param.grad)

    def forward(self):
        pass