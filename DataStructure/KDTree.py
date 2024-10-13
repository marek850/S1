from DataStructure.KDNode import KDNode

class KDTree:
    def __init__(self):
        self.root = None
        
    def __insert(self, current, point, node, depth):
        if current is None:
            return node

        dimension = depth % 2

        if point[dimension] <= current.point[dimension]:
            current.left = self.__insert(current.left, point, node, depth + 1)
        else:
            current.right = self.__insert(current.right, point, node, depth + 1)

        return current

    def insertNode(self, point, node):
        self.root = self.__insert(self.root, point, node, 0)
   
    def searchNode(self, point):
        results = []

        def recursive_search(current, depth):
            if current is None:
                return

            dimension = depth % 2
            
            if current.point == point:
                results.append(current.data)

            if point[dimension] <= current.point[dimension]:
                recursive_search(current.left, depth + 1)

            if point[dimension] > current.point[dimension]:
                recursive_search(current.right, depth + 1)

        recursive_search(self.root, 0)
        
        return results