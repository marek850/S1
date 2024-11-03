from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode
from Locations.Parcel import Parcel, ParcelGui
from Locations.GpsPosition import GPSPosition
from Locations.Property import Property, PropertyGui
from DataGeneration.Generator import Generator
from DataGeneration.OperationGenerator import OpGenerator

class GeoApp:
    def __init__(self):
        # Initialize the KDTree for storing properties and parcels
        self.__properties_tree = KDTree()
        self.__parcels_tree = KDTree()
        self.__all_tree = KDTree()  # Combined KDTree for properties and parcels
        self.__generator = Generator()
        self.__op_generator = OpGenerator()
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
        id = self.__generator.generate_unique_id()
        new_property = Property(id, property_number, description, (start_gps_position, end_gps_position))
        start_node = KDNode((new_property.start_lat, new_property.start_lon), new_property)
        end_node = KDNode((new_property.end_lat, new_property.end_lon), new_property)
        self.properties_tree.insert(start_node)
        self.properties_tree.insert(end_node)
        #self.all_tree.insert(start_node)
        #self.all_tree.insert(end_node)
        print(f"Property {new_property} added")
        
        self._update_parcel_references(new_property, start_node, "add")
        self._update_parcel_references(new_property, end_node, "add")
        
        return True
    
    def insert_test(self, operation_number: int, percentage_of_duplicates: int):
        self.__generator.generate_inserts(operation_number, percentage_of_duplicates)
        

    def add_parcel(self, parcel_number, description, start_lat_dir, start_latitude, start_long_dir, start_longtitude,  end_lat_dir, \
        end_latitude, end_long_dir, end_longtitude):
      
        start_gps_position = GPSPosition(start_lat_dir, start_latitude, start_long_dir, start_longtitude)
        end_gps_position = GPSPosition(end_lat_dir, end_latitude, end_long_dir, end_longtitude)
        id = self.__generator.generate_unique_id()
        new_parcel = Parcel(id, parcel_number, description, (start_gps_position, end_gps_position))
        start_node = KDNode((new_parcel.start_lat, new_parcel.start_lon), new_parcel)
        end_node = KDNode((new_parcel.end_lat, new_parcel.end_lon), new_parcel)
        self.parcels_tree.insert(start_node)
        self.parcels_tree.insert(end_node)
        #self.all_tree.insert(start_node)
        #self.all_tree.insert(end_node)
        
        self._update_property_references(new_parcel, start_node, "add")
        self._update_property_references(new_parcel, end_node, "add")


    def _update_parcel_references(self, property, start_node, operation):
        
        start_node_layovers = self.parcels_tree.search(start_node.keys)
        #end_node_layovers = self.parcels_tree.search(end_node.keys)
        if operation == "add":
            """ for node in end_node_layovers:
                property.add_parcel(node.data)
                node.data.add_property(property) """
            for node in start_node_layovers:
                property.add_parcel(node.data)
                node.data.add_property(property)
                print(f"Parcel {node.data} added")
        else:
            """ for node in end_node_layovers:
                property.parcels.remove(node.data)
                node.data.properties.remove(property) """
            for node in start_node_layovers:
                property.parcels.remove(node.data)
                node.data.properties.remove(property)
                print(f"Parcel {node.data} removed")
            
    
    def _update_property_references(self, parcel, start_node, operation):
        start_node_layovers = self.properties_tree.search(start_node.keys)
        #end_node_layovers = self.parcels_tree.search(end_node.keys)
        if operation == "add":
            """ for node in end_node_layovers:
                parcel.add_parcel(node.data)
                node.data.add_property(parcel) """
            for node in start_node_layovers:
                parcel.add_property(node.data)
                node.data.add_parcel(parcel)
        else:
            """ for node in end_node_layovers:
                parcel.properties.remove(node.data)
                node.data.parcels.remove(parcel) """
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

    def search_all_by_gps(self, gps_position_1: GPSPosition, gps_position_2: GPSPosition):
        all_properties_1 = self.all_tree.search((gps_position_1.latitude_value, gps_position_1.longitude_value))
        filtered_objects = []
        for property in all_properties_1:
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
            if node.data == property:
                properties.append(node)
        for node in self.properties_tree.search((property.boundary[1].latitude_value, property.boundary[1].longitude_value)):
            if node.data == property:
                properties.append(node)
        for node in properties:
            self.properties_tree.delete(node.keys, node.data)
            #self.all_tree.delete(node.keys, node.data)
            self._update_parcel_references(node.data, node, "delete")
            
    def delete_parcel(self, parcel):
        parcel = Property(parcel.unique_id, parcel.property_number, parcel.description, parcel.boundary)
        parcels = []
        for node in self.parcels_tree.search((parcel.boundary[0].latitude_value, parcel.boundary[0].longitude_value)):
            if node.data == parcel:
                parcels.append(node)
        for node in self.parcels_tree.search((parcel.boundary[1].latitude_value, parcel.boundary[1].longitude_value)):
            if node.data == parcel:
                parcels.append(node)
        for node in parcels:
            self.parcels_tree.delete(node.keys, node.data)
            #self.all_tree.delete(node.keys, node.data)
            self._update_property_references(node.data, node, "delete")
               
    def edit_property(self, property_id, new_property_number, new_description, new_start_lat_dir, new_start_latitude, new_start_long_dir, new_start_longtitude,  new_end_lat_dir, \
        new_end_latitude, new_end_long_dir, new_end_longtitude):
        property = self.__properties_tree.search(property_id)
        if property is None:
            return False
        property.data.property_number = new_property_number
        property.data.description = new_description
        property.data.start_lat = new_start_lat_dir
        property.data.start_lon = new_start_long_dir
        property.data.end_lat = new_end_lat_dir
        property.data.end_lon = new_end_long_dir
        return True
