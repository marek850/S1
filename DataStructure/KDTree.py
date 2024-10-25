
class KDTree:
    def __init__(self, dimensions=2):
        self.dim = dimensions
        self.root = None
        
        
    def insert(self, newNode):
        depth = 0
        dimension = 0
        parent = None
        current = self.root
        while current is not None:
            dimension = depth % self.dim
            parent = current
            if newNode.keys[dimension] <= current.keys[dimension]:
                current = current.left
            else:
                current = current.right
            depth += 1
        newNode.parent = parent
        if parent == None:
            self.root = newNode
        elif newNode.keys[dimension] <= parent.keys[dimension]:
            parent.left = newNode
            newNode.dim = depth % self.dim
        else:
            parent.right = newNode
            newNode.dim = depth  % self.dim
     
    def search(self, target_keys):
        depth = 0
        dimension = 0
        foundNodes = []
        current_node = self.root
        while current_node is not None:
            dimension = depth % self.dim
            if target_keys == current_node.keys:
                foundNodes.append(current_node)
            if target_keys[dimension] <= current_node.keys[dimension]:
                current_node = current_node.left
            else:
                current_node = current_node.right
            depth += 1
        return foundNodes      
    
    def delete(self, key, data):    
        current = self.root
        parent = None
        depth = 0
        currentDimension = 0

        # Najdeme uzol ktory chceme vymazat
        while current is not None:
            currentDimension = depth % self.dim
            if current.keys == key and current.data == data:
                break

            parent = current

            if key[currentDimension] <= current.keys[currentDimension]:
                current = current.left
            else:
                current = current.right
            depth += 1

        # Ak uzol neexistuje vratime chybu
        if current is None:
            return "Uzol nenájdený"

        # Ak je uzol list vymazeme ho priamo
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
            return

        # Ak uzol nie je list, najdeme nahradny uzol
        while current.left is not None or current.right is not None:
                
            if current.left is not None:
                replacement, replacementDimension = self.__find_subtree_max(current.left, current.dim)
                current.keys, replacement.keys = replacement.keys, current.keys
                current.data, replacement.data = replacement.data, current.data
                current = replacement
                
            else:
                replacement = self.__find_subtree_min(current.right, currentDimension)

        parent = current.parent
        if parent is None:
            self.root = None
        elif parent.left == current:
            parent.left = None
        else:
            parent.right = None
        return

            
    
    
    def __find_subtree_max(self,node, dimension):
        if node is None:
            return None
        max_node = node
        current = node
        temp = []
        
        while True:
            if current is not None:
                temp.append(current)
                current = current.left
            else:
                if not temp:
                    break
                
                current = temp.pop()
                
                if max_node is None or current.keys[dimension] > max_node.keys[dimension]:
                    max_node = current

                current = current.right
        return max_node, max_node.dim
       
    def __find_subtree_min(self,node, dimension):
        if node is None:
            return None
        
        min_node = None
        current = node.right
        temp = []
        
        while True:
            if current is not None:
                temp.append(current)
                current = current.left
            else:
                if not temp:
                    break
                current = temp.pop()
                if min_node is None or current.point[dimension] < min_node.point[dimension]:
                    min_node = current
                current = current.right
        
        return min_node

       

    def get_all_nodes(self):
        nodes = []
        current = self.root
        temp = []
        while True:
            if current is not None:
                temp.append(current)
                current = current.left
            else:
                if temp == []:
                    break
                current = temp[-1]  #current = s[len(s) - 1]
                nodes.append(current)
                temp.pop()
                current = current.right
        return nodes