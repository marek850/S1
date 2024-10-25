
from DataStructure.KDNode import KDNode
from GpsPosition import GPSPosition
from Parcel import Parcel
from DataStructure.KDTree import KDTree
from Property import Property
from DataGeneration.OperationGenerator import OpGenerator

def main():
   # tuple1 = (23, "2d")
    #tuple2 = (23, "23")
    #if tuple1 == tuple2:
     #   print("Tuples are equal")
    #operationGenerator = OpGenerator()
    #operationGenerator.generate_inserts(10)
    #operationGenerator.generate_random_searches()
    #operationGenerator.generate_searches()
    points = [
            (23, 35),
            (24, 36),
            (24, 40),
            (22, 39),
            (22, 31),
            (22, 32),
            (24, 34),
            (30, 33),
            (29, 46),
            (27, 43),
            (22, 42),
            (12, 41),
            (24, 35)
        ]
    towns = ["Nitra", "Tlmače – úrad", "Tlmače parkovisko", "Senica", "Senica – škola", 
            " Senica – úrad", "Tlmače", "Levice", "Bojnice", "Nováky", 
            "Senica – stanica", "Hodonín", "Tlmače - nem"]
    kd_tree = KDTree()
    for index, point in enumerate(points):
        kd_tree.insert(KDNode(point,towns[index]))
    # Postupne vkladáme body do k-d stromu, druhý parameter bude poradie prvku
    
        # Delete the node with the town "Nitra"
    point_to_delete = (23, 35)
    kd_tree.delete(point_to_delete,towns[0])
    point_to_delete = (21, 32)
    kd_tree.delete(point_to_delete, towns[5])
    # Delete the node with the town "Senica – úrad"
    
    # Delete the node with the town "Senica – škola"
    point_to_delete = (22, 32)
    kd_tree.delete(point_to_delete)
    # Delete the node with the town "Senica – stanica"
    point_to_delete = (22, 42)
    kd_tree.delete(point_to_delete)
    # Delete the node with the town "Hodonín"
    point_to_delete = (12, 41)
    kd_tree.delete(point_to_delete)
    # Delete the node with the town "Senica"
    point_to_delete = (24, 40)
    kd_tree.delete(point_to_delete)
        

if __name__ == "__main__":  
    main()
   