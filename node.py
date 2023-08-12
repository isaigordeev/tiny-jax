class Node:
    def __init__(self, value=0, _previous_nodes=(), _operator=None):
        self.value = value
        self.grad = 0
        self._previous_node = set(_previous_nodes)
        self._backward_function = lambda: None


    def __add__(self, other):
        other = other if isinstance(other, Node) else Node(other)
        out = Node(self.value + other.value, (self, other), '+')


        return out