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


    def relu(self):

        self.value = 0 if self.value < 0 else self.value

        out = AbstractNode(self.value, (self,), 'relu')

        def _backward_pass():
            self.grad += out.value*out.grad

        out._backward_function = _backward_pass()

        return out


    def backward(self):

        topo = []
        visited = set()
        def build_order(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_order(child)
                topo.append(v)

        build_order(self)

        self.grad = 1
        for v in reversed(topo):
            v._backward_function()


    def __neg__(self): 
        return self * -1
    
    def __radd__(self, other):
        return self + other

    def __sub__(self, other): 
        return self + (-other)

    def __rsub__(self, other): 
        return other + (-self)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * other**-1

    def __rtruediv__(self, other): 
        return other * self**-1

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
