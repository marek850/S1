from collections import deque

class KDTreeLevelOrder:
    def __init__(self, root):
        self.queue = deque([root] if root else [])
        self.visited = []  # Zoznam už navštívených uzlov
        self.current_index = -1  # Ukazovateľ na aktuálny uzol
    
    def next(self):
        if not self.has_next():
            raise StopIteration
        
        if self.current_index + 1 < len(self.visited):
            self.current_index += 1
            return self.visited[self.current_index]
        
        current = self.queue.popleft()
        self.visited.append(current)
        self.current_index += 1
        if current.left:
            self.queue.append(current.left)
        if current.right:
            self.queue.append(current.right)
        return current
    
    def previous(self):
        if not self.has_previous():
            raise StopIteration
        self.current_index -= 1
        return self.visited[self.current_index]
    
    def has_next(self):
        return self.current_index + 1 < len(self.visited) or bool(self.queue)
    
    def has_previous(self):
        return self.current_index > 0