
import customtkinter as csc
from DataGeneration.OperationGenerator import OpGenerator
from DataStructure.KDNode import KDNode
from GUI.MainApp import MainApp
from GeoApp import GeoApp
from Locations.GpsPosition import GPSPosition
from Locations.Area import Area
from Locations.Parcel import Parcel
  

def main():
    """ tuple1 = (23, "2d")
    tuple2 = (23, "23")
    if tuple1 == tuple2:
       print("Tuples are equal") """
    
    
    operationGenerator = OpGenerator()
    operationGenerator.generate_inserts(5)
    operationGenerator.generate_searches()
    operationGenerator.generate_deletes()  
    """
    csc.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    csc.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"
    
    app = MainApp()
    app.mainloop() """
    """ csc.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    csc.set_default_color_theme("blue") """  # Themes: "blue" (default), "green", "dark-blue"
    #geo_app = GeoApp()
   # app = MainApp(geo_app)
   # app.mainloop()
    """ new_parcel = Parcel(5, 4, "description", ((GPSPosition('N',4,'E',5),GPSPosition('N',3,'E',8))))
    node = KDNode((new_parcel.start_lat, new_parcel.start_lon), new_parcel)
    node2 = KDNode((new_parcel.end_lat, new_parcel.end_lon), new_parcel)
    nodes = [node, node2]
    filtered_properties = []
    for property in nodes:
            if property.data not in filtered_properties:
                filtered_properties.append(property.data)
    print(filtered_properties) """
    def login():
        print("Login")
        
    """ frame = csc.CTkFrame(root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = csc.CTkLabel(frame, text="Login", font=("Roboto", 24))
    label.pack(pady=12, padx=10)
    
    entry1 = csc.CTkEntry(frame, font=("Roboto", 14), placeholder_text="Username")
    entry1.pack(pady=12, padx=10)
    
    entry2 = csc.CTkEntry(frame, font=("Roboto", 14), placeholder_text="Username")
    entry2.pack(pady=12, padx=10)
    
    button = csc.CTkButton(frame, text="Login", font=("Roboto", 14), command=login)
    button.pack(pady=12, padx=10)
    
    checkbox = csc.CTkCheckBox(frame, text="Remember me", font=("Roboto", 14))
    checkbox.pack(pady=12, padx=10) """
    #root.mainloop()
    """
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
     # Delete the node with the town "Senica – úrad"
    point_to_delete = (22, 32)
    kd_tree.delete(point_to_delete,towns[5])
    # Delete the node with the town "Hodonín"
    point_to_delete = (12, 41)
    kd_tree.delete(point_to_delete,towns[11])
   # Delete the node with the town "Senica – stanica"
    point_to_delete = (22, 42)
    kd_tree.delete(point_to_delete,towns[10])
    # Delete the node with the town "Senica – škola"
    point_to_delete = (22, 31)
    kd_tree.delete(point_to_delete,towns[4])
    
    # Delete the node with the town "Senica"
    point_to_delete = (22, 39)
    kd_tree.delete(point_to_delete, towns[3])
    print("Done") """
    # Delete the node with the town "Senica"
    """ point_to_delete = (24, 40)
    kd_tree.delete(point_to_delete) """
        

if __name__ == "__main__":  
    main()
   