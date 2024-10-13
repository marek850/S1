
from DataStructure.KDNode import KDNode
from GpsPosition import GPSPosition
from Parcel import Parcel
from DataStructure.KDTree import KDTree
from Property import Property
from DataGeneration.OperationGenerator import OpGenerator

def main():
    operationGenerator = OpGenerator(1000)
    operationGenerator.generate_inserts()
    operationGenerator.generate_random_searches()
    #operationGenerator.generate_searches()
    """ 
    points = [
        (5, 8),
        (12, 3),
        (18, 22),
        (7, 14),
        (20, 1),
        (15, 9),
        (8, 19),
        (3, 4),
        (11, 17),
        (6, 13),
        (2, 23)
    ]
    kd_tree = KDTree()

# Postupne vkladáme body do k-d stromu, druhý parameter bude poradie prvku
    for index, point in enumerate(points):
        kd_tree.insert(point, KDNode(point, index)) 
    print("K-d strom po vložení bodov:") """
if __name__ == "__main__":
    main()