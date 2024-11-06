import random
import sys
from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode
from Locations.GpsPosition import GPSPosition as GpsPosition
from Locations.Property import Property
from DataGeneration.Generator import Generator
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
class Data:
    def __init__(self, primary_key, sec_x, sec_y):
        self.__primary_key = primary_key
        self.__sec_x = sec_x
        self.__sec_y = sec_y
    def __eq__(self, other):
        return self.__primary_key == other.__primary_key

class OpGenerator:
    def __init__(self,  seed=None):#parcel_tree, property_tree, all_tree,
        self.__max_size = sys.maxsize
        self.__seed = seed if seed is not None else random.randint(1, self.__max_size)
        self.__kd_tree = KDTree(4)
        self.__generated_keys = []
        self.__all_nodes = []
        self.__nodes = []
        random.seed(self.__seed)
        self.__generator = Generator(self.__seed)
        
    
    def generate_inserts(self, num_operations=1000, percentage_of_duplicates=30, type="property"):
        
        mistakes = 0
        currently_generated_data = []
        keys = self.__generate_keys(num_operations, percentage_of_duplicates)
        print(f"Generating {num_operations} insert operations:\n")
        for i in range(num_operations):
            self.generate_insert(i, num_operations)
        if mistakes == 0:
            print("All keys were inserted correctly")
        else:
            print(f"Number of mistakes during insertions: {mistakes}")
        #self.__test_inserts(currentlyGeneratedData)
    
    def generate_insert(self, i, num_operations=0):
        a = random.uniform(0.1, 10000.25)
        b = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(1, 10)))
        c = random.randint(0, 10000)
        d = random.uniform(0.1, 10000.25)
        uroven1 = Uroven1(a, b)
        uroven4 = Uroven4(b, c)
        value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
        data = Data(value, self.__generator.generate_number(1, 50), self.__generator.generate_number(1, 50))
        node1 = KDNode((uroven1, c, d, uroven4), data)
        
        """ lat = "NS"
        lon = "WE"
        
        gps1 = GpsPosition(lat[random.randint(0, 1)], 
                random.randint(0, self.__max_size),
                lon[random.randint(0, 1)]
                , random.randint(0, self.__max_size))
        gps2=GpsPosition(lat[random.randint(0, 1)],
                random.randint(0, self.__max_size),
                lon[random.randint(0, 1)],
                random.randint(0, self.__max_size))
        property = Property(random.randint(0, self.__max_size), random.randint(0, self.__max_size), value, (gps1, gps2)) """
        
        print(f"Inserting node with key: {node1.keys} and value: {node1.data}\n")
        self.__kd_tree.insert(node1)
        self.__all_nodes.append(node1)
        mistakes = 0
        whole_tree = self.__kd_tree.get_all_nodes()
        if whole_tree.count(node1) !=  self.__all_nodes.count(node1):
            mistakes += 1    
        self.__nodes.append(node1)
        if mistakes == 0:
            print("Tree remains consistent after insertion")
        else:
            print(f"Number of nodes not found after insertion: {mistakes}")
        return mistakes
    def generate_random_operations(self, num_operations=100):
        print(f"Generating {num_operations} random operations:\n")
        mistakes = 0
        for i in range(num_operations):
            if not self.__all_nodes:
                break
            operation = random.choice(["insert", "delete", "search"])
            if operation == "insert":
                mistakes += self.generate_insert(i)
            elif operation == "delete":
                mistakes += self.generate_delete(i)
            else:
                mistakes += self.generate_search(self.__all_nodes[random.randint(0, len(self.__all_nodes) - 1)])
        if mistakes == 0:
            print("All operations were successful")
        else:
            print(f"Number of mistakes: {mistakes}")   
    def test(self):
        self.generate_inserts(10000, 40)
        self.generate_random_operations()
    
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
        num_of_mistakes = 0
        print(f"Generating search operations for all inserted keys:\n")
        i = 0
        for node in self.__all_nodes:
            try:
                num_of_mistakes += self.generate_search(node)
            except Exception as e:
                print(f"Failed Error: {e}\n")
            i+=1
        if num_of_mistakes == 0:
            print("All keys were found")
        else:
            print(f"Number of mistakes: {num_of_mistakes}")
        
    def generate_delete(self,i):
        node_to_delete = self.__all_nodes[random.randint(0, len(self.__all_nodes) - 1)]
        print(f"Deleting node with key: {node_to_delete.keys} and value: {node_to_delete.data}\n")
        mistakes = 0
        if self.__kd_tree.delete(node_to_delete.keys, node_to_delete.data) == "Uzol nenájdený":
            not_deleted += 1
        else:
            self.__all_nodes.remove(node_to_delete)
            #nodes = self.__kd_tree.get_all_nodes()
            whole_tree = self.__kd_tree.get_all_nodes()
            if whole_tree.count(node_to_delete) !=  self.__all_nodes.count(node_to_delete):
                mistakes += 1
            if mistakes == 0:   
                print("Tree remains consistent after deletion")
            else: 
                print(f"Number of nodes not found after deletion: {mistakes}")
        return mistakes
    def generate_search(self, node):
        key = node.keys
        num_of_mistakes = 0
        print(f"Searching for key: {key}\n")
        foundNodes = self.__kd_tree.search(key)
        if foundNodes is not None and foundNodes != []:
            print(f"Found values:\n")
            for node in foundNodes:
                print(f"Value: {node.data}\n")
        num_of_found = 0
        for element in self.__all_nodes:
            if element.keys == key:
                num_of_found += 1
                
        if num_of_found != len(foundNodes):
            print(f"Number of found nodes: {len(foundNodes)} does not match the number of nodes with key: {key} in the tree: {num_of_found}\n")
            num_of_mistakes += 1
        if num_of_mistakes == 0:
            print("Search was successful")
        else:
            print(f"Number of mistakes: {num_of_mistakes}")
        return num_of_mistakes
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
                
    """ def __test_inserts(self, insertedData):
        numOfMistakes = 0
        for element in insertedData:
            found = 0
            for node in self.__kd_tree.get_all_nodes():
                if element == node.dsata:
                    found = 1
                
            if found == 0:
                numOfMistakes += 1
        if numOfMistakes == 0:
            print("All keys were inserted correctly")
        else:
            print(f"Number of mistakes: {numOfMistakes}")
             """
    