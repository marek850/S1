
import customtkinter as csc
from DataGeneration.Tester import OpGenerator
from DataStructure.KDNode import KDNode
from DataStructure.KDTree import KDTree
from DataStructure.KDTreeFactory import TreeFactory
from GUI.MainApp import MainApp
from App.GeoApp import GeoApp
from Locations.GpsPosition import GPSPosition
from Locations.Area import AreaUnit
from Locations.Parcel import Parcel


  

def main():
    
    operationGenerator = OpGenerator()
    #operationGenerator.generate_inserts(10000)
    #operationGenerator.generate_searches()
    #operationGenerator.generate_deletes() 
    #operationGenerator.test()

    #kd_tree_factory = TreeFactory("KDTree")
    geo_app = GeoApp()
    app = MainApp(geo_app)
    app.mainloop()
    
    
    tree = KDTree(dimensions=2)
    nodes = [
    KDNode((30, 40), "A"),
    KDNode((5, 25), "B"),
    KDNode((70, 70), "C"),
    KDNode((10, 12), "D"),
    KDNode((50, 50), "E"),
    KDNode((35, 45), "F")
    ]

    for node in nodes:
        tree.insert(node)

    # Inicializácia in-order iterátora
    iterator = tree.create_levelorder_iterator()

    # Test pre pohyb `next`
    print("In-order traversal using next:")
    while iterator.has_next():
        current = iterator.next()
        print(f"Node: keys={current.keys}, data={current.data}")

    # Test pre pohyb `previous`
    print("\nIn-order traversal using previous:")
    while iterator.has_previous():
        current = iterator.previous()
        print(f"Node: keys={current.keys}, data={current.data}")    
if __name__ == "__main__":  
    main()
   