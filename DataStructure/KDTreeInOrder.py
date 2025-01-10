class KDTreeInOrder:
    def __init__(self, root):
            self.stack = []
            self.visited = []  # Zoznam už navštívených uzlov
            self.current_index = -1  # Ukazovateľ na aktuálny uzol
            self._push_left(root)
        
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        if not self.has_next():
            raise StopIteration
        
        if self.current_index + 1 < len(self.visited):
            self.current_index += 1
            return self.visited[self.current_index]
        
        
        current = self.stack.pop()
        self.visited.append(current)
        self.current_index += 1
        self._push_left(current.right)
        return current
    
    def previous(self):
        if not self.has_previous():
            raise StopIteration
        self.current_index -= 1
        return self.visited[self.current_index]
    
    def has_next(self):
        return self.current_index + 1 < len(self.visited) or bool(self.stack)
    
    def has_previous(self):
        return self.current_index > 0