class Node:
    def __init__(self, value=0, _previous_node=()):
        self.value = value
        self.grad = 0
        self._previous_node = set(_previous_node)
        self._backward_function = lambda: None