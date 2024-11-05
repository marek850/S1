import random
import sys
from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode
from Locations.GpsPosition import GPSPosition as GpsPosition
from Locations.Parcel import Parcel
from Locations.Property import Property


class DataGenerator:
    def __init__(self,   parcel_tree, property_tree, all_tree, app, seed=None):
        self.__max_size = sys.maxsize
        self.__seed = seed if seed is not None else random.randint(1, self.__max_size)
        self.__parcel_tree = parcel_tree
        self.__property_tree = property_tree
        self.__all_tree = all_tree
        self.__app = app
        random.seed(self.__seed)
        
    
    def generate_inserts(self, num_operations=1000, percentage_of_duplicates=30):
        
        shared_gps_positions = self.__generate_shared_positions(num_operations, percentage_of_duplicates)
        added_elements = ""
        counter = 0
        for i in range(num_operations):
            value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
            
            # Step 2: Assign a shared or unique GpsPosition based on the intersection percentage
            if counter < len(shared_gps_positions):
                if i > 0 and i % 2 == 0:
                    counter += 1
                gps1 = shared_gps_positions[counter]  
                gps2 = GpsPosition(
                    random.choice("NS"),
                    random.randint(0, 10000000),
                    random.choice("WE"),
                    random.randint(0, 10000000)
                )
                
            else:  
                gps1 = GpsPosition(
                    random.choice("NS"),
                    random.randint(0, 10000000),
                    random.choice("WE"),
                    random.randint(0, 10000000)
                )
                gps2 = GpsPosition(
                    random.choice("NS"),
                    random.randint(0, 10000000),
                    random.choice("WE"),
                    random.randint(0, 10000000)
                )
            
            if i % 2 == 0:
                property = Property(
                    random.randint(0, 10000000), 
                    random.randint(0, 10000000), 
                    value, 
                    (gps1, gps2)
                )
                
                self.__app.add_property(property.property_number, \
                    property.description, property.boundary[0].latitude_direction, abs(property.boundary[0].latitude_value),\
                       property.boundary[0].longitude_direction, abs(property.boundary[0].longitude_value), \
                           property.boundary[1].latitude_direction, abs(property.boundary[1].latitude_value),\
                       property.boundary[1].longitude_direction, abs(property.boundary[1].longitude_value))
                
                """ start_node = KDNode((property.start_lat, property.start_lon), property)
                end_node = KDNode((property.end_lat, property.end_lon), property)
                self.__property_tree.insert(start_node)
                self.__property_tree.insert(end_node)
                self.__all_tree.insert(KDNode((property.start_lat, property.start_lon), property))
                self.__all_tree.insert(KDNode((property.end_lat, property.end_lon), property)) """
                added_elements += f"Pridana Nehnutelnost: {property}\n"
                #self.__app.update_parcel_references(property, start_node, end_node, "add")
            else:
                parcel = Parcel(
                    random.randint(0, 10000000), 
                    random.randint(0, 10000000), 
                    value, 
                    (gps2, gps1)
                )
                self.__app.add_parcel(parcel.parcel_number, \
                    parcel.description, parcel.boundary[0].latitude_direction, abs(parcel.boundary[0].latitude_value),\
                       parcel.boundary[0].longitude_direction, abs(parcel.boundary[0].longitude_value), \
                           parcel.boundary[1].latitude_direction, abs(parcel.boundary[1].latitude_value),\
                       parcel.boundary[1].longitude_direction, abs(parcel.boundary[1].longitude_value))
                """ start_node = KDNode((parcel.start_lat, parcel.start_lon), parcel)
                end_node = KDNode((parcel.end_lat, parcel.end_lon), parcel)
                self.__parcel_tree.insert(start_node)
                self.__parcel_tree.insert(end_node)
                self.__all_tree.insert(KDNode((parcel.start_lat, parcel.start_lon), parcel))
                self.__all_tree.insert(KDNode((parcel.end_lat, parcel.end_lon), parcel)) """
                added_elements += f"Pridana Parcela: {parcel}\n"
                #self.__app.update_property_references(parcel, start_node, end_node, "add")
        return added_elements

    def __generate_shared_positions(self, num_operations=1000, percentage_of_duplicates=30):
        
        shared_gps_positions = [
            GpsPosition(
                random.choice("NS"),
                random.randint(0, 10000000),
                random.choice("WE"),
                random.randint(0, 10000000)
            )
            for _ in range(int(num_operations * (percentage_of_duplicates / 100)))
        ]

        return shared_gps_positions