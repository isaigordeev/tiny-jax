from node import AbstractNode

class AbstractActivation(AbstractNode):
    def __init__(self):
        super().__init__()

class ReLU(AbstractActivation):
    def __init__(self):
        super().__init__()

    def forward(self):
        self.value = 0 if self.value < 0 else self.value

        def _backward_pass():
            self.grad += self.value*self.grad

        self._backward_function = _backward_pass
