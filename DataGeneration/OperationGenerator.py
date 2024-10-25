import random
from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode

class OpGenerator:
    def __init__(self, seed=None):
        self.seed = seed if seed is not None else random.randint(1, 10000000)
        self.kd_tree = KDTree()
        self.generated_keys = []
        self.all_nodes = []
        
    
    def generate_inserts(self, num_operations=1000, percentage_of_duplicates=30):
        random.seed(self.seed)
        currentlyGeneratedData = []
        keys = self.__generate_keys(num_operations, percentage_of_duplicates)
        print(f"Generating {num_operations} insert operations:\n")
        for i in range(num_operations):
            try:
                print(f"I'm currently generating insert operation {i + 1}/{num_operations}\n")
                key = keys[i]
                value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
                print(f"Inserting key: {key} with value: {value}\n")
                node = KDNode(key, value)
                self.generated_keys.append(key)
                currentlyGeneratedData.append(node.data)
                self.kd_tree.insert(node)
            except Exception as e:
                print(f"Failed to insert key: {key} with value: {value}. Error: {e}\n")
        self.__test_inserts(currentlyGeneratedData)
    
    def __generate_keys(self,num_tuples, duplicate_percentage):
    
        num_duplicates = int(num_tuples * (duplicate_percentage / 100))
        num_unique = num_tuples - num_duplicates
        unique_tuples = [(random.randint(0, 1000000000000), random.randint(0, 1000000000000)) for _ in range(num_unique)]
        duplicate_tuples = [random.choice(unique_tuples) for _ in range(num_duplicates)]
        all_tuples = unique_tuples + duplicate_tuples
        random.shuffle(all_tuples)

        return all_tuples

            
    def generate_searches(self):
        random.seed(self.seed)
        num_operations = len(self.generated_keys)
        notFound = 0
        print(f"Generating search operations for all inserted keys:\n")
        for i in range(num_operations):
            try:
                print(f"I'm currently generating search operation {i + 1}/{num_operations}\n")
                key = self.generated_keys[random.randint(0, len(self.generated_keys) - 1)]
                print(f"Searching for key: {key}\n")
                foundNodes = self.kd_tree.search(key)
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
                
    def generate_deletes(self):
        random.seed(self.seed)
        num_operations = len(self.generated_keys)
        self.all_nodes = self.kd_tree.get_all_nodes()
        nodes_to_delete = []
        for node in self.all_nodes:
            nodes_to_delete.append(node)
        not_deleted = 0
        not_found_after_delete = 0
        print(f"Generating delete operations for all inserted keys:\n")
        for i in range(num_operations):
            try:
                print(f"I'm currently generating delete operation {i + 1}/{num_operations}\n")
                node_to_delete = nodes_to_delete[random.randint(0, len(nodes_to_delete) - 1)]
                print(f"Deleting node with key: {node_to_delete.keys} and value: {node_to_delete.data}\n")
                if self.kd_tree.delete(node_to_delete.keys, node_to_delete.data) == "Uzol nenájdený":
                    not_deleted += 1
                else:
                    nodes_to_delete.remove(node_to_delete)
                    for node in nodes_to_delete:
                        if self.kd_tree.find_node(node) == None:
                            not_found_after_delete += 1
                        
                        
            except Exception as e:
                print(f"Failed to delete key: {node_to_delete.keys} and value: {node_to_delete.data}. Error: {e}\n")
                not_deleted += 1
        if not_deleted == 0:
            print("All keys were deleted")
        else:
            for node in nodes_to_delete:
                print(f"Key: {node.keys} and value: {node.data} was not deleted")
        if not_found_after_delete == 0:   
            print("Tree remains consistent after all deletions")
        else: 
            print(f"Number of nodes not found after deletion: {not_found_after_delete}")
                
    def __test_inserts(self, insertedData):
        numOfMistakes = 0
        for element in insertedData:
            found = 0
            for node in self.kd_tree.get_all_nodes():
                if element == node.data:
                    found = 1
                
            if found == 0:
                numOfMistakes += 1
        if numOfMistakes == 0:
            print("All keys were inserted correctly")
        else:
            print(f"Number of mistakes: {numOfMistakes}")
            
    