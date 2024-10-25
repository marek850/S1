import random
from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode

class OpGenerator:
    def __init__(self, seed=None):
        self.seed = seed if seed is not None else random.randint(1, 10000000)
        self.kdtree = KDTree()
        self.generatedKeys = []
        
    
    def generate_inserts(self, num_operations=1000):
        random.seed(self.seed)
        currentlyGeneratedData = []
        print(f"Generating {num_operations} insert operations:\n")
        for i in range(num_operations):
            try:
                print(f"I'm currently generating insert operation {i + 1}/{num_operations}\n")
                key = (random.randint(1, 1000000000000), random.randint(1, 1000000000000))
                value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
                print(f"Inserting key: {key} with value: {value}\n")
                node = KDNode(key, value)
                self.generatedKeys.append(key)
                currentlyGeneratedData.append(node.data)
                self.kdtree.insert(node)
            except Exception as e:
                print(f"Failed to insert key: {key} with value: {value}. Error: {e}\n")
        self.__test_inserts(currentlyGeneratedData)
            
    def generate_searches(self):
        random.seed(self.seed)
        num_operations = len(self.generatedKeys)
        notFound = 0
        print(f"Generating search operations for all inserted keys:\n")
        for i in range(num_operations):
            try:
                print(f"I'm currently generating search operation {i + 1}/{num_operations}\n")
                key = self.generatedKeys[random.randint(0, len(self.generatedKeys) - 1)]
                print(f"Searching for key: {key}\n")
                foundNodes = self.kdtree.search(key)
                if foundNodes is not None and foundNodes != []:
                    print(f"Found values:\n")
                    for node in foundNodes:
                        print(f"Value: {node.data}\n")
                else:
                    print(f"Key: {key} not found\n")
                    notFound += 1
            except Exception as e:
                print(f"Failed to find key: {key}. Error: {e}\n")
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
                
                
    def __test_inserts(self, insertedData):
        numOfMistakes = 0
        for element in insertedData:
            found = 0
            for node in self.kdtree.get_all_nodes():
                if element == node.data:
                    found = 1
                
            if found == 0:
                numOfMistakes += 1
        if numOfMistakes == 0:
            print("All keys were inserted correctly")
        else:
            print(f"Number of mistakes: {numOfMistakes}")
            
    