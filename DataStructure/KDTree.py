
from DataStructure.KDNode import KDNode


class KDTree:
    def __init__(self, dimensions=2):
        self.dim = dimensions
        self.root = None
        self.size = 0
        
        
    def insert(self, newNode: KDNode):
        """ depth = 0
        current = self.root
        parent = None

        while current is not None:
            dimension = depth % self.dim
            parent = current
            
            
            if newNode.keys[dimension] <= current.keys[dimension]:
                current = current.left
            else:
                current = current.right

            depth += 1

        newNode.parent = parent
        newNode.dim = depth % self.dim

        
        if parent is None:
            self.root = newNode  
        else:
            dimension = (depth - 1) % self.dim  
            if newNode.keys[dimension] <= parent.keys[dimension]:
                parent.left = newNode
            else:
                parent.right = newNode """
        #self.size += 1
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
        self.size += 1
     
    def search(self, target_keys: tuple):
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
          
    def search_with_data(self, target_keys: tuple, data):
        depth = 0
        dimension = 0
        found_node = None
        current_node = self.root
        while current_node is not None:
            dimension = depth % self.dim
            if target_keys == current_node.keys and data == current_node.data:
                found_node = current_node
            if target_keys[dimension] <= current_node.keys[dimension]:
                current_node = current_node.left
            else:
                current_node = current_node.right
            depth += 1
        return found_node
    
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
    
    def update(self, key, data, new_data):
        node_to_update = self.search_with_data(key, data)
        if node_to_update is not None:
            node_to_update.data = new_data
        
        
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
                    if node2.parent != None and node2.parent.left == node1:
                        node2.parent.left = node2
                    if node2.parent != None and node2.parent.right == node1:
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
                if node2.parent != None and node2.parent.left == node1:
                    node2.parent.left = node2
                elif node2.parent != None and node2.parent.right == node1:
                    node2.parent.right = node2
                if node1.parent != None and node1.parent.left == node2:
                    node1.parent.left = node1
                elif node1.parent != None and node1.parent.right == node2:
                    node1.parent.right = node1
                if node2.parent is None:
                    self.root = node2
            node2.dim = node1_dim_t
            node1.dim = node2_dim_t
               
                                    
        current = self.root
        parent = None
        depth = 0
        currentDimension = 0       

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

        if current is None:
            return "Uzol nenájdený"
        parent = current.parent

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
                self.size -= 1
            elif parent.left == current:
                parent.left = None
                self.size -= 1
            else:
                parent.right = None
                self.size -= 1
            return

        
        duplicates_to_remove = []
        to_insert = []
        while True:
            if duplicates_to_remove != []:  
                current = duplicates_to_remove.pop()
                to_insert.append(current)
         
            while current.left is not None or current.right is not None:
                    
                if current.left is not None:
                    replacement = self.__find_subtree_max(current.left, current.dim)
                    swap_nodes(current, replacement)
                    
                else:
                    replacement = self.__find_subtree_min(current.right, current.dim)
                    swap_nodes(current, replacement)
                    rep_duplicates = self.__find_duplicates_by_dimension(replacement, replacement.dim)
                    for duplicate in rep_duplicates:
                        duplicates_to_remove.append(duplicate)
                    
                    
                                              
            parent = current.parent
            if parent is None:
                self.root = None
                self.size -= 1
            elif parent.left == current:
                parent.left = None
                self.size -= 1
            else:
                parent.right = None
                self.size -= 1
            if duplicates_to_remove == []:
                break
        if to_insert != []:
                for node in to_insert:
                    self.insert(node)    
    
            
    def __find_duplicates_by_dimension(self, node, dimension):
        duplicates = []
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
                
                if  current.keys[dimension] == node.keys[dimension]:
                    duplicates.append(current)
                current = current.right
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