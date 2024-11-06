import random
from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode
from Locations.Parcel import Parcel, ParcelGui
from Locations.GpsPosition import GPSPosition
from Locations.Property import Property, PropertyGui
from DataGeneration.Generator import Generator
from DataGeneration.Tester import OpGenerator
from DataGeneration.DataGenerator import DataGenerator
from FileProcessing.FileProcessor import FileHandler

class GeoApp:
    def __init__(self):
        # Initialize the KDTree for storing properties and parcels
        self.__properties_tree = KDTree()
        self.__parcels_tree = KDTree()
        self.__all_tree = KDTree()  # Combined KDTree for properties and parcels
        self.__generator = Generator()
        self.__data_generator = DataGenerator(self.__parcels_tree, self.__properties_tree, self.__all_tree, self)
        self.__last_unique_id = random.randint(1, 10000000)
    @property
    def properties_tree(self):
        return self.__properties_tree

    @property
    def parcels_tree(self):
        return self.__parcels_tree

    @property
    def all_tree(self):
        return self.__all_tree
    
    def add_property(self, property_number, description, start_lat_dir, start_latitude, start_long_dir, start_longtitude,  end_lat_dir, \
        end_latitude, end_long_dir, end_longtitude):
        start_gps_position = GPSPosition(start_lat_dir, start_latitude, start_long_dir, start_longtitude)
        end_gps_position = GPSPosition(end_lat_dir, end_latitude, end_long_dir, end_longtitude)
        id = self.__last_unique_id
        new_property = Property(id, property_number, description, (start_gps_position, end_gps_position))
        start_node = KDNode((new_property.start_lat, new_property.start_lon), new_property)
        end_node = KDNode((new_property.end_lat, new_property.end_lon), new_property)
        self.properties_tree.insert(start_node)
        self.properties_tree.insert(end_node)
        self.all_tree.insert(KDNode((new_property.start_lat, new_property.start_lon), new_property))
        self.all_tree.insert(KDNode((new_property.end_lat, new_property.end_lon), new_property))
        print(f"Property {new_property} added")
        
        self.update_parcel_references(new_property, start_node, end_node, "add")
        self.__last_unique_id += 1
    
    def insert_test(self, operation_number: int, percentage_of_duplicates: int):
        self.__generator.generate_inserts(operation_number, percentage_of_duplicates)
        

    def add_parcel(self, parcel_number, description, start_lat_dir, start_latitude, start_long_dir, start_longtitude,  end_lat_dir, \
        end_latitude, end_long_dir, end_longtitude):
      
        start_gps_position = GPSPosition(start_lat_dir, start_latitude, start_long_dir, start_longtitude)
        end_gps_position = GPSPosition(end_lat_dir, end_latitude, end_long_dir, end_longtitude)
        id = self.__last_unique_id
        new_parcel = Parcel(id, parcel_number, description, (start_gps_position, end_gps_position))
        start_node = KDNode((new_parcel.start_lat, new_parcel.start_lon), new_parcel)
        end_node = KDNode((new_parcel.end_lat, new_parcel.end_lon), new_parcel)
        self.parcels_tree.insert(start_node)
        self.parcels_tree.insert(end_node)
        self.all_tree.insert(KDNode((new_parcel.start_lat, new_parcel.start_lon), new_parcel))
        self.all_tree.insert(KDNode((new_parcel.end_lat, new_parcel.end_lon), new_parcel))
        
        self.update_property_references(new_parcel, start_node, end_node, "add")
        self.__last_unique_id += 1

    def update_parcel_references(self, property, start_node, end_node, operation):
        
        start_node_layovers = self.parcels_tree.search(start_node.keys)
        if end_node is not None:
            end_node_layovers = self.parcels_tree.search(end_node.keys)
            for node in end_node_layovers:
                if node not in start_node_layovers:
                    start_node_layovers.append(node)
        if operation == "add":
            for node in start_node_layovers:
                property.add_parcel(node.data)
                node.data.add_property(property)
                print(f"Parcel {node.data} added")
        else:
            for node in start_node_layovers:
                property.parcels.remove(node.data)
                node.data.properties.remove(property)
                print(f"Parcel {node.data} removed")
            
    def clear_trees(self):
        self.__all_tree.clear()
    def update_property_references(self, parcel, start_node, end_node, operation):
        start_node_layovers = self.properties_tree.search(start_node.keys)
        if end_node is not None:
            end_node_layovers = self.properties_tree.search(end_node.keys)
            for node in end_node_layovers:
                if node not in start_node_layovers:
                    start_node_layovers.append(node)
        if operation == "add":
            for node in start_node_layovers:
                parcel.add_property(node.data)
                node.data.add_parcel(parcel)
        else:
            for node in start_node_layovers:
                parcel.properties.remove(node.data)
                node.data.parcels.remove(parcel)
            

    def search_properties_by_gps(self, gps_position: GPSPosition):
        all_properties = self.properties_tree.search((gps_position.latitude_value, gps_position.longitude_value))
        filtered_properties = []
        for property in all_properties:
            gui_property = PropertyGui(property.data)
            print(f"Property {gui_property}")
            if gui_property not in filtered_properties:
                filtered_properties.append(gui_property)
        
        return filtered_properties

    def search_parcels_by_gps(self, gps_position: GPSPosition):
        all_parcels = self.parcels_tree.search((gps_position.latitude_value, gps_position.longitude_value))
        filtered_parcels = []
        for parcel in all_parcels:
            gui_parcel = ParcelGui(parcel.data)
            if gui_parcel not in filtered_parcels:
                filtered_parcels.append(gui_parcel)
        return filtered_parcels
    
    def save_to_file(self, file_name):
        all_nodes = self.all_tree.level_order_traversal_unique_data()
        sorted_nodes = sorted(all_nodes, key=lambda Area: Area.unique_id)
        file_handler = FileHandler(file_name, self)
        file_handler.save_to_file(sorted_nodes)
        
    def load_from_file(self, file_name):
        self.clear_trees()
        file_handler = FileHandler(file_name, self)
        file_handler.load_from_file()
        
    def search_all_by_gps(self, gps_position_1: GPSPosition, gps_position_2: GPSPosition):
        all_properties_1 = self.all_tree.search((gps_position_1.latitude_value, gps_position_1.longitude_value))
        all_properties_2 = self.all_tree.search((gps_position_2.latitude_value, gps_position_2.longitude_value))
        combined_properties = all_properties_1 + all_properties_2
        filtered_objects = []
        for property in combined_properties:
            if isinstance(property.data, Property):
                gui_property = PropertyGui(property.data)
                if gui_property not in filtered_objects:
                    filtered_objects.append(gui_property)
            else:
                gui_parcel = ParcelGui(property.data)
                if gui_parcel not in filtered_objects:
                    filtered_objects.append(gui_parcel)
        return filtered_objects

    def delete_property(self, property):
        property = Property(property.unique_id, property.property_number, property.description, property.boundary)
        properties = []
        for node in self.properties_tree.search((property.boundary[0].latitude_value, property.boundary[0].longitude_value)):
            if node.data == property and node not in properties:
                properties.append(node)
        for node in self.properties_tree.search((property.boundary[1].latitude_value, property.boundary[1].longitude_value)):
            if node.data == property and node not in properties:
                properties.append(node)
        for node in properties:
            self.properties_tree.delete(node.keys, node.data)
            self.all_tree.delete(node.keys, node.data)
            self.update_parcel_references(node.data, node, None, "delete")
            
    def delete_parcel(self, parcel):
        parcel = Parcel(parcel.unique_id, parcel.parcel_number, parcel.description, parcel.boundary)
        parcels = []
        for node in self.parcels_tree.search((parcel.boundary[0].latitude_value, parcel.boundary[0].longitude_value)):
            if node.data == parcel and node not in parcels:
                parcels.append(node)
        for node in self.parcels_tree.search((parcel.boundary[1].latitude_value, parcel.boundary[1].longitude_value)):
            if node.data == parcel and node not in parcels:
                parcels.append(node)
        for node in parcels:
            self.parcels_tree.delete(node.keys, node.data)
            self.all_tree.delete(node.keys, node.data)
            self.update_property_references(node.data, node, None, "delete")
               
    def edit_property(self, property_id, new_property_number, new_description, new_start_lat_dir, new_start_latitude, new_start_long_dir, new_start_longtitude,  new_end_lat_dir, \
        new_end_latitude, new_end_long_dir, new_end_longtitude, initial_property_number, initial_description, initial_start_lat_dir, \
            initial_start_latitude, initial_start_long_dir, initial_start_longtitude,  initial_end_lat_dir, \
                initial_end_latitude, initial_end_long_dir, initial_end_longtitude):
        initial_gps_start = GPSPosition(initial_start_lat_dir, initial_start_latitude, initial_start_long_dir, initial_start_longtitude)
        initial_gps_end = GPSPosition(initial_end_lat_dir, initial_end_latitude, initial_end_long_dir, initial_end_longtitude)
        initial_property = Property(property_id, initial_property_number, initial_description, (initial_gps_start, initial_gps_end))
        initial_node_start = KDNode((initial_property.start_lat, initial_property.start_lon), initial_property)
        initial_node_end = KDNode((initial_property.end_lat, initial_property.end_lon), initial_property)
        
        new_gps_start = GPSPosition(new_start_lat_dir, new_start_latitude, new_start_long_dir, new_start_longtitude)
        new_gps_end = GPSPosition(new_end_lat_dir, new_end_latitude, new_end_long_dir, new_end_longtitude)
        new_property = Property(property_id, new_property_number, new_description, (new_gps_start, new_gps_end))
        new_node_start = KDNode((new_property.start_lat, new_property.start_lon), new_property)
        new_node_end = KDNode((new_property.end_lat, new_property.end_lon), new_property)
        if initial_node_start.keys != new_node_start.keys or initial_node_end.keys != new_node_end.keys:
            self.delete_property(initial_property)
            self.add_property(new_property_number, new_description, new_start_lat_dir, new_start_latitude, new_start_long_dir, new_start_longtitude,  new_end_lat_dir, \
                new_end_latitude, new_end_long_dir, new_end_longtitude)
        else:
            old_property = self.properties_tree.update_data(initial_node_start.keys, initial_node_start.data,  new_node_start.data)
            new_property.parcels = old_property.parcels
            for parcel in old_property.parcels:
                parcel.remove_property(old_property)
                parcel.add_property(new_property)
            self.properties_tree.update_data(initial_node_end.keys, initial_node_end.data,  new_node_end.data)
            self.all_tree.update_data(initial_node_start.keys, initial_node_start.data,  new_node_start.data)
            self.all_tree.update_data(initial_node_end.keys, initial_node_end.data,  new_node_end.data)
            
    def edit_parcel(self, parcel_id, new_parcel_number, new_description, new_start_lat_dir, new_start_latitude, new_start_long_dir, new_start_longtitude,  new_end_lat_dir, \
        new_end_latitude, new_end_long_dir, new_end_longtitude, initial_parcel_number, initial_description, initial_start_lat_dir, \
            initial_start_latitude, initial_start_long_dir, initial_start_longtitude,  initial_end_lat_dir, \
                initial_end_latitude, initial_end_long_dir, initial_end_longtitude):
        initial_gps_start = GPSPosition(initial_start_lat_dir, initial_start_latitude, initial_start_long_dir, initial_start_longtitude)
        initial_gps_end = GPSPosition(initial_end_lat_dir, initial_end_latitude, initial_end_long_dir, initial_end_longtitude)
        initial_parcel = Parcel(parcel_id, initial_parcel_number, initial_description, (initial_gps_start, initial_gps_end))
        initial_node_start = KDNode((initial_parcel.start_lat, initial_parcel.start_lon), initial_parcel)
        initial_node_end = KDNode((initial_parcel.end_lat, initial_parcel.end_lon), initial_parcel)
        
        new_gps_start = GPSPosition(new_start_lat_dir, new_start_latitude, new_start_long_dir, new_start_longtitude)
        new_gps_end = GPSPosition(new_end_lat_dir, new_end_latitude, new_end_long_dir, new_end_longtitude)
        new_parcel = Parcel(parcel_id, new_parcel_number, new_description, (new_gps_start, new_gps_end))
        new_node_start = KDNode((new_parcel.start_lat, new_parcel.start_lon), new_parcel)
        new_node_end = KDNode((new_parcel.end_lat, new_parcel.end_lon), new_parcel)
        if initial_node_start.keys != new_node_start.keys or initial_node_end.keys != new_node_end.keys:
            self.delete_parcel(initial_parcel)
            self.add_parcel(new_parcel_number, new_description, new_start_lat_dir, new_start_latitude, new_start_long_dir, new_start_longtitude,  new_end_lat_dir, \
                new_end_latitude, new_end_long_dir, new_end_longtitude)
        else:
            old_parcel = self.parcels_tree.update_data(initial_node_start.keys, initial_node_start.data,  new_node_start.data)
            new_parcel.properties = old_parcel.properties
            for property in old_parcel.properties:
                property.remove_parcel(old_parcel)
                property.add_parcel(new_parcel)
            self.parcels_tree.update_data(initial_node_end.keys, initial_node_end.data,  new_node_end.data)
            self.all_tree.update_data(initial_node_start.keys, initial_node_start.data,  new_node_start.data)
            self.all_tree.update_data(initial_node_end.keys, initial_node_end.data,  new_node_end.data)      
    def test_add(self, operations, overlap):
        
        return self.__data_generator.generate_inserts(operations, overlap)   
