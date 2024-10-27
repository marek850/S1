from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode
from Locations import Parcel
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
        self.all_tree.insert(start_node)
        self.all_tree.insert(end_node)
        
        self._update_parcel_references(new_property, start_node, end_node, "add")
        
        return True
    
    def insert_test(self, operation_number: int, percentage_of_duplicates: int):
        self.__generator.generate_inserts(operation_number, percentage_of_duplicates)
        

    def add_parcel(self, parcel_number, description, start_latitude, start_longtitude,  end_latitude, end_longtitude):
      
        start_gps_position = GPSPosition(start_latitude[0], start_latitude[1], start_longtitude[0], start_longtitude[1])
        end_gps_position = GPSPosition(end_latitude[0], end_latitude[1], end_longtitude[0], end_longtitude[1])
        id = self.__generator.generate_unique_id()
        new_parcel = Parcel(id, parcel_number, description, (start_gps_position, end_gps_position))
        start_node = KDNode((new_parcel.start_lat, new_parcel.start_lon), new_parcel)
        end_node = KDNode((new_parcel.end_lat, new_parcel.end_lon), new_parcel)
        self.parcels_tree.insert(start_node)
        self.parcels_tree.insert(end_node)
        self.all_tree.insert(start_node)
        self.all_tree.insert(end_node)
        
        self._update_property_references(new_parcel, start_node, end_node, "add")

    def _update_parcel_references(self, property, start_node, end_node, operation):
        
        start_node_layovers = self.parcels_tree.search(start_node.keys)
        end_node_layovers = self.parcels_tree.search(end_node.keys)
        if operation == "add":
            for node in end_node_layovers:
                property.add_parcel(node.data)
                node.data.add_property(property)
            for node in start_node_layovers:
                property.add_parcel(node.data)
                node.data.add_property(property)
        else:
            for node in end_node_layovers:
                property.parcels.remove(node.data)
                node.data.properties.remove(property)
            for node in start_node_layovers:
                property.parcels.remove(node.data)
                node.data.properties.remove(property)
            
    
    def _update_property_references(self, parcel, start_node, end_node, operation):
        start_node_layovers = self.parcels_tree.search(start_node.keys)
        end_node_layovers = self.parcels_tree.search(end_node.keys)
        if operation == "add":
            for node in end_node_layovers:
                parcel.add_parcel(node.data)
                node.data.add_property(parcel)
            for node in start_node_layovers:
                parcel.add_parcel(node.data)
                node.data.add_property(parcel)
        else:
            for node in end_node_layovers:
                parcel.properties.remove(node.data)
                node.data.parcels.remove(parcel)
            for node in start_node_layovers:
                parcel.properties.remove(node.data)
                node.data.parcels.remove(parcel)
            

    def search_properties_by_gps(self, gps_position: GPSPosition):
        all_properties = self.properties_tree.search((gps_position.latitude_value, gps_position.longitude_value))
        filtered_properties = []
        for property in all_properties:
            gui_property = PropertyGui(property.data)
            if gui_property not in filtered_properties:
                filtered_properties.append(gui_property)
        
        return filtered_properties

    def search_parcels_by_gps(self, gps_position: GPSPosition):
        all_parcels = self.properties_tree.search((gps_position.latitude_value, gps_position.longitude_value))
        filtered_parcels = []
        for property in all_parcels:
            gui_property = Parcel.ParcelGui(property.data)
            if gui_property not in filtered_parcels:
                filtered_parcels.append(gui_property)
        return filtered_parcels

    def search_all_by_gps(self, gps_position_1: GPSPosition, gps_position_2: GPSPosition):
        all_properties_1 = self.all_tree.search((gps_position_1.latitude_value, gps_position_1.longitude_value))
        all_properties_2 = self.all_tree.search((gps_position_2.latitude_value, gps_position_2.longitude_value))
        filtered_objects = []
        for property in all_properties_1:
            if isinstance(property.data, Property):
                gui_property = PropertyGui(property.data)
                if gui_property not in filtered_objects:
                    filtered_objects.append(gui_property)
            else:
                gui_parcel = Parcel.ParcelGui(property.data)
                if gui_parcel not in filtered_objects:
                    filtered_objects.append(gui_parcel)
        for property in all_properties_2:
            if isinstance(property.data, Property):
                gui_property = PropertyGui(property.data)
                if gui_property not in filtered_objects:
                    filtered_objects.append(gui_property)
            else:
                gui_parcel = Parcel.ParcelGui(property.data)
                if gui_parcel not in filtered_objects:
                    filtered_objects.append(gui_parcel)
        
        return filtered_objects

    def search_all_by_gps_area(self, gps_position_1, gps_position_2):
        """
        Search all properties and parcels within a given rectangular area defined by two GPS positions.
        :param gps_position_1: First GPS position.
        :param gps_position_2: Second GPS position.
        :return: List of properties and parcels within the area.
        """
        matching_properties = self.properties_tree.search_range(gps_position_1, gps_position_2)
        matching_parcels = self.parcels_tree.search_range(gps_position_1, gps_position_2)
        return matching_properties + matching_parcels

    def remove_property_by_gps(self, gps_position):
        """
        Remove property at the specified GPS position.
        :param gps_position: GPS position to identify the property to be removed.
        """
        properties_to_remove = self.search_properties_by_gps(gps_position)
        for property_obj in properties_to_remove:
            self.properties_tree.delete(property_obj)
            self.all_tree.delete(property_obj)
        for parcel in property_obj.parcels:
                parcel.properties.remove(property_obj)

    def remove_parcel_by_gps(self, gps_position):
        """
        Remove parcel at the specified GPS position.
        :param gps_position: GPS position to identify the parcel to be removed.
        """
        parcels_to_remove = self.search_parcels_by_gps(gps_position)
        for parcel_obj in parcels_to_remove:
            self.parcels_tree.delete(parcel_obj)
            self.all_tree.delete(parcel_obj)
        for property in parcel_obj.properties:
                property.parcels.remove(parcel_obj)

    def edit_property_by_gps(self, gps_position, updated_data):
        """
        Edit the property at the specified GPS position.
        :param gps_position: GPS position to identify the property to be edited.
        :param updated_data: A dictionary containing updated property data.
        """
        properties_to_edit = self.search_properties_by_gps(gps_position)
        for property_obj in properties_to_edit:
            property_obj.update(updated_data)
            # Update KDTree since coordinates might have changed
            self.properties_tree.delete(property_obj.gps_coordinates)
            self.all_tree.delete(property_obj.gps_coordinates)
            self.properties_tree.insert(property_obj)
            self.all_tree.insert(property_obj)
            self._update_parcel_references(property_obj)

    def edit_parcel_by_gps(self, gps_position, updated_data):
        """
        Edit the parcel at the specified GPS position.
        :param gps_position: GPS position to identify the parcel to be edited.
        :param updated_data: A dictionary containing updated parcel data.
        """
        parcels_to_edit = self.search_parcels_by_gps(gps_position)
        for parcel_obj in parcels_to_edit:
            parcel_obj.update(updated_data)
            # Update KDTree since coordinates might have changed
            self.parcels_tree.delete(parcel_obj.gps_coordinates)
            self.all_tree.delete(parcel_obj.gps_coordinates)
            self.parcels_tree.insert(parcel_obj)
            self.all_tree.insert(parcel_obj)
            self._update_property_references(parcel_obj)

    def display_all_data(self):
        """
        Display all properties and parcels.
        """
        print("Properties:")
        for property_obj in self.properties_tree.get_all():
            print(property_obj)
        print("\nParcels:")
        for parcel_obj in self.parcels_tree.get_all():
            print(parcel_obj)
