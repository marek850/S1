import random
import sys
from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode
from Locations.GpsPosition import GPSPosition as GpsPosition
from Locations.Property import Property

class Uroven1:
    def __init__(self, a: float, b: str):
        self.a = a
        self.b = b

    def __str__(self):
        return f"a={self.a}, b='{self.b}'"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Uroven1):
            return NotImplemented
        return abs(self.a - other.a) < 1e-9 and self.b == other.b

    def __lt__(self, other):
        if not isinstance(other, Uroven1):
            return NotImplemented
        if abs(self.a - other.a) >= 1e-9:
            return self.a < other.a
        return self.b < other.b

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other
class Uroven4:
    def __init__(self, b: str, c: int):
        self.b = b
        self.c = c

    def __str__(self):
        return f"b='{self.b}', c={self.c}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Uroven4):
            return NotImplemented
        return self.b == other.b and self.c == other.c

    def __lt__(self, other):
        if not isinstance(other, Uroven4):
            return NotImplemented
        if self.b < other.b:
            return True
        if self.b == other.b:
            return self.c < other.c
        return False

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other



class OpGenerator:
    def __init__(self,  seed=None):#parcel_tree, property_tree, all_tree,
        self.__max_size = sys.maxsize
        self.__seed = seed if seed is not None else random.randint(1, self.__max_size)
        """ self.__parcel_tree = parcel_tree
        self.__property_tree = property_tree
        self.__all_tree = all_tree """
        self.__kd_tree = KDTree(4)
        self.__generated_keys = []
        self.__all_nodes = []
        self.__nodes = []
        random.seed(self.__seed)
        
    
    def generate_inserts(self, num_operations=1000, percentage_of_duplicates=30, type="property"):
        
        mistakes = 0
        currentlyGeneratedData = []
        keys = self.__generate_keys(num_operations, percentage_of_duplicates)
        print(f"Generating {num_operations} insert operations:\n")
        for i in range(num_operations):
            a = random.uniform(0.1, 10000.25)
            b = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(1, 10)))
            c = random.randint(0, 10000)
            d = random.uniform(0.1, 10000.25)
            uroven1 = Uroven1(a, b)
            uroven4 = Uroven4(b, c)
            value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
            node1 = KDNode((uroven1, c, d, uroven4), value)
            
            lat = "NS"
            lon = "WE"
            
            gps1 = GpsPosition(lat[random.randint(0, 1)], 
                    random.randint(0, self.__max_size),
                    lon[random.randint(0, 1)]
                    , random.randint(0, self.__max_size))
            gps2=GpsPosition(lat[random.randint(0, 1)],
                    random.randint(0, self.__max_size),
                    lon[random.randint(0, 1)],
                    random.randint(0, self.__max_size))
            property = Property(random.randint(0, self.__max_size), random.randint(0, self.__max_size), value, (gps1, gps2))
            try:
                print(f"I'm currently generating insert operation {i + 1}/{num_operations}\n")
                key = keys[i]
                
                
                
                print(f"Inserting key: {key} with value: {property}\n")
                node = KDNode(key, value)
                
                self.__generated_keys.append(key)
                currentlyGeneratedData.append(node.data)
                self.__kd_tree.insert(node1)
                self.__all_nodes.append(node1)
                if self.__kd_tree.size != len(self.__all_nodes):
                    mistakes += 1
                    print(f"Insertion of key {node1.keys} with data: {node1.data} was not successful\n")
                    
                self.__nodes.append(node)
            except Exception as e:
                print(f"Failed to insert key: {node1.keys} with value: {node1.data}. Error: {e}\n")
        if mistakes == 0:
            print("All keys were inserted correctly")
        else:
            print(f"Number of mistakes during: {mistakes}")
        #self.__test_inserts(currentlyGeneratedData)
    
    def __generate_keys(self,num_tuples, duplicate_percentage):
    
        num_duplicates = int(num_tuples * (duplicate_percentage / 100))
        num_unique = num_tuples - num_duplicates
        unique_tuples = [(random.randint(0, self.__max_size), random.randint(0, self.__max_size)) for _ in range(num_unique)]
        duplicate_tuples = [random.choice(unique_tuples) for _ in range(num_duplicates)]
        all_tuples = unique_tuples + duplicate_tuples
        random.shuffle(all_tuples)

        return all_tuples

            
    def generate_searches(self):
        
        num_operations = len(self.__generated_keys)
        notFound = 0
        print(f"Generating search operations for all inserted keys:\n")
        i = 0
        for node in self.__all_nodes:
            try:
                print(f"I'm currently generating search operation {i + 1}\n")
                key = node.keys
                print(f"Searching for key: {key}\n")
                foundNodes = self.__kd_tree.search(key)
                if foundNodes is not None and foundNodes != []:
                    print(f"Found values:\n")
                    for node in foundNodes:
                        print(f"Value: {node.data}\n")
                else:
                    print(f"Key: {key} not found\n")
                    notFound += 1
            except Exception as e:
                print(f"Failed to find key: {key}. Error: {e}\n")
            i+=1
        if notFound == 0:
            print("All keys were found")
        else:
            print(f"Number of not found keys: {notFound}")
    """  
    def generate_random_searches(self):
        random.seed(self.seed)
        print(f"Generating {self.num_operations} random search operations:\n")
        for i in range(self.num_operations):
            try:
                print(f"I'm currently generating random search operation {i + 1}/{self.num_operations}\n")
                key = (random.randint(1, 1000000000000), random.randint(1, 1000000000000))
                print(f"Searching for random key: {key}\n")
                foundNodes = self.kdtree.search(key)
                if foundNodes is not None and foundNodes != []:
                    print(f"Found values:\n")
                    for node in foundNodes:
                        print(f"Value: {node.data}\n")
                else:
                    print(f"Key: {key} not found\n")
            except Exception as e:
                print(f"Failed to find key: {key}. Error: {e}\n") """
                
    def generate_deletes(self):
        
        print(f"seed:{self.__seed}")
        num_operations = len(self.__generated_keys)
        self.__all_nodes = self.__kd_tree.get_all_nodes()
        nodes_to_delete = []
        for node in self.__all_nodes:
            nodes_to_delete.append(node)
        not_deleted = 0
        mistakes = 0
        print(f"Generating delete operations for all inserted keys:\n")
        i = 0
        while self.__all_nodes != []:
            try:
                if i == 25:
                    print("")
                print(f"I'm currently generating delete operation {i + 1}\n")
                node_to_delete = self.__all_nodes[random.randint(0, len(self.__all_nodes) - 1)]
                print(f"Deleting node with key: {node_to_delete.keys} and value: {node_to_delete.data}\n")
                if self.__kd_tree.delete(node_to_delete.keys, node_to_delete.data) == "Uzol nenájdený":
                    not_deleted += 1
                else:
                    self.__all_nodes.remove(node_to_delete)
                    #nodes = self.__kd_tree.get_all_nodes()
                    if len(self.__all_nodes) != self.__kd_tree.size:
                        print(f"Tree is not consistent after deletion of key: {node_to_delete.keys} and value: {node_to_delete.data}\n")
                        mistakes += 1
                        
                        
            except Exception as e:
                print(f"Failed to delete key: {node_to_delete.keys} and value: {node_to_delete.data}. Error: {e}\n")
            i+=1
               
        if len(self.__all_nodes) == 0:
            print("All keys were deleted")
        else:
            for node in self.__all_nodes:
                print(f"Key: {node.keys} and value: {node.data} was not deleted")
        if mistakes == 0:   
            print("Tree remains consistent after all deletions")
        else: 
            print(f"Number of nodes not found after deletion: {mistakes}")
                
    def __test_inserts(self, insertedData):
        numOfMistakes = 0
        for element in insertedData:
            found = 0
            for node in self.__kd_tree.get_all_nodes():
                if element == node.data:
                    found = 1
                
            if found == 0:
                numOfMistakes += 1
        if numOfMistakes == 0:
            print("All keys were inserted correctly")
        else:
            print(f"Number of mistakes: {numOfMistakes}")
            
    