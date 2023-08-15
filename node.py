class AbstractNode:
    def __init__(self, value=0, _previous_nodes=(), _operator=None):
        self.value = value
        self.grad = 0
        self._previous_node = set(_previous_nodes)
        self._backward_function = lambda: None


    def __add__(self, other):
        other = other if isinstance(other, AbstractNode) else AbstractNode(other)

        out = AbstractNode(self.value + other.value, (self, other), '+')

        def _backward_pass():
            self.grad += out.grad
            other.grad += out.grad

        out._backward_function = _backward_pass

        return out

    def __mul__(self, other):
        other = other if isinstance(other, AbstractNode) else AbstractNode(other)

        out = AbstractNode(self.value * other.value, (self, other), '*')

        def _backward_pass():
            self.grad += out.grad * other.grad
            other.grad += out.grad * self.grad

        out._backward_function = _backward_pass

        return out

    def __pow__(self, other):
        assert isinstance(other, (float, int))

        out = AbstractNode(self.value ** other, (self,), f'**{other}')

        def _backward_pass():
            self.grad += (other*self.value**(other-1)) * out.grad

        out._backward_function = _backward_pass

        return out

