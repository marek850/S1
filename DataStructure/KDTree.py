
from DataStructure.KDNode import KDNode


class KDTree:
    def __init__(self, dimensions=2):
        self.dim = dimensions
        self.root = None
        
        
    def insert(self, newNode: KDNode):
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
    def find_node(self,node):
        depth = 0
        dimension = 0
        current_node = self.root
        while current_node is not None:
            dimension = depth % self.dim
            if node == current_node:
                return current_node
            if node.keys[dimension] <= current_node.keys[dimension]:
                current_node = current_node.left
            else:
                current_node = current_node.right
            depth += 1
        return None    
    
    def delete(self, key, data):    
        def swap_nodes(node1, node2):
            node1_parent_t, node1_left_t, node1_right_t,node1_dim_t = node1.parent, node1.left, node1.right, node1.dim
            node2_parent_t, node2_left_t, node2_right_t,node2_dim_t = node2.parent, node2.left, node2.right, node2.dim
            if node2.parent == node1:
                node2.parent = node1_parent_t
                node1.parent = node2
                if node1.left == node2:
                    node2.left = node1
                    node2.right = node1_right_t
                elif node1.right == node2:
                    node2.right = node1
                    node2.left = node1_left_t
                node1.left = node2_left_t
                node1.right = node2_right_t
                if node1.left is not None:
                    node1.left.parent = node1
                if node1.right is not None:
                    node1.right.parent = node1
                if node1.left is not None:
                    node1.left.parent = node1
                if node2.right is not None:
                    node2.right.parent = node2
                if node2.left is not None:
                    node2.left.parent = node2
                if node2.parent is None:
                    self.root = node2
                else:
                    if node2.parent.left == node1:
                        node2.parent.left = node2
                    if node2.parent.right == node1:
                        node2.parent.right = node2
                
            else:
                node2.parent = node1_parent_t
                node1.parent = node2_parent_t
                node2.left = node1_left_t
                node2.right = node1_right_t
                node1.left = node2_left_t
                node1.right = node2_right_t
                if node1.left is not None:
                    node1.left.parent = node1
                if node1.right is not None:
                    node1.right.parent = node1
                if node2.left is not None:
                    node2.left.parent = node2
                if node2.right is not None:
                    node2.right.parent = node2
                if node2.parent.left == node1:
                    node2.parent.left = node2
                elif node2.parent.right == node1:
                    node2.parent.right = node2
                if node1.parent.left == node2:
                    node1.parent.left = node1
                elif node1.parent.right == node2:
                    node1.parent.right = node1
                if node2.parent is None:
                    self.root = node2
            node2.dim = node1_dim_t
            node1.dim = node2_dim_t    
                                    
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
        parent = current.parent
        # Ak je uzol list vymazeme ho priamo
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
            return

        
        duplicates_to_remove = []
        to_insert = []
        while True:
            # Ak uzol nie je list, najdeme nahradny uzol
            while current.left is not None or current.right is not None:
                    
                if current.left is not None:
                    replacement = self.__find_subtree_max(current.left, current.dim)
                    swap_nodes(current, replacement)
    
                else:
                    replacement = self.__find_subtree_min(current.right, current.dim)
                    rep_duplicates = self.__find_duplicates_by_dimension(current.right, current.dim)
                    for duplicate in rep_duplicates:
                        duplicates_to_remove.append(duplicate)
                    swap_nodes(current, replacement)
                                              
            parent = current.parent
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
            if duplicates_to_remove != []:
                current = duplicates_to_remove.pop()
                to_insert.append(current)
            else:
                if to_insert != []:
                    for node in to_insert:
                        self.insert(node)
                break
            
    
            
    def __find_duplicates_by_dimension(self, node, dimension):
        duplicates = []
        stack = [node]
        
        while stack:
            current = stack.pop()
            if current is None:
                continue
            if current != node and current.keys[dimension] == node.keys[dimension]:
                duplicates.append(current)
            stack.append(current.left)
            stack.append(current.right)
        
        return duplicates
        
    
    def __find_subtree_max(self,subtree_root, dimension):
        if subtree_root is None:
            return None
        max_node = subtree_root
        current = subtree_root
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
        return max_node
       
    def __find_subtree_min(self,subtree_root, dimension):
        if subtree_root is None:
            return None
        
        min_node = subtree_root
        current = subtree_root
        temp = []
        
        while True:
            if current is not None:
                temp.append(current)
                current = current.left
            else:
                if not temp:
                    break
                current = temp.pop()
                if min_node is None or current.keys[dimension] < min_node.keys[dimension]:
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