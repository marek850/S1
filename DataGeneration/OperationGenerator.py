import random
from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode

class OpGenerator:
    def __init__(self, num_operations=1000, seed=None):
        self.num_operations = num_operations
        self.seed = seed if seed is not None else random.randint(1, 10000000)
        self.kdtree = KDTree()
        self.generatedKeys = []
        
    
    def generate_inserts(self):
        random.seed(self.seed)
        print(f"Generating {self.num_operations} insert operations:\n")
        for i in range(self.num_operations):
            try:
                print(f"I'm currently generating insert operation {i + 1}/{self.num_operations}\n")
                key = (random.randint(1, 1000000000000), random.randint(1, 1000000000000))
                value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
                print(f"Inserting key: {key} with value: {value}\n")
                node = KDNode(key, value)
                self.generatedKeys.append(key)
                self.kdtree.insertNode(key,node)
            except Exception as e:
                print(f"Failed to insert key: {key} with value: {value}. Error: {e}\n")
            
    def generate_searches(self):
        random.seed(self.seed)
        print(f"Generating {self.num_operations} search operations:\n")
        for i in range(self.num_operations):
            try:
                print(f"I'm currently generating search operation {i + 1}/{self.num_operations}\n")
                key = self.generatedKeys[random.randint(0, len(self.generatedKeys) - 1)]
                print(f"Searching for key: {key}\n")
                value = self.kdtree.searchNode(key)
                if value is not None and value != []:
                    print(f"Found value: {value}\n")
                else:
                  print(f"Key: {key} not found\n")
            except Exception as e:
                print(f"Failed to find key: {key}. Error: {e}\n")
                
    def generate_random_searches(self):
        random.seed(self.seed)
        print(f"Generating {self.num_operations} random search operations:\n")
        for i in range(self.num_operations):
            try:
                print(f"I'm currently generating random search operation {i + 1}/{self.num_operations}\n")
                key = (random.randint(1, 1000000000000), random.randint(1, 1000000000000))
                print(f"Searching for random key: {key}\n")
                value = self.kdtree.searchNode(key)
                if value is not None and value != []:
                    print(f"Found value: {value}\n")
                else:
                    print(f"Key: {key} not found\n")
            except Exception as e:
                print(f"Failed to find key: {key}. Error: {e}\n")