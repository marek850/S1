from DataStructure.KDTree import KDTree
from DataStructure.KDNode import KDNode
from Locations.GpsPosition import GPSPosition
from Locations.Property import Property
from DataGeneration.Generator import Generator

class GeoApp:
    def __init__(self):
        # Initialize the KDTree for storing properties and parcels
        self.__properties_tree = KDTree()
        self.__parcels_tree = KDTree()
        self.__all_tree = KDTree()  # Combined KDTree for properties and parcels
        self.__generator = Generator()
    @property
    def properties_tree(self):
        return self.__properties_tree

    @property
    def parcels_tree(self):
        return self.__parcels_tree

    @property
    def all_tree(self):
        return self.__all_tree
    def add_property(self, property_number, description, start_latitude, start_longtitude,  end_latitude, end_longtitude):
        if not (isinstance(start_latitude, list) and isinstance(start_longtitude, list) and isinstance(end_latitude, list) and isinstance(end_longtitude, list) and
                len(start_latitude) == 2 and len(start_longtitude) == 2 and len(end_latitude) == 2 and len(end_longtitude) == 2):  # Check if coordinates are lists of two elements 
            raise ValueError("Coordinates must be lists of two elements")
        start_gps_position = GPSPosition(start_latitude[0], start_latitude[1], start_longtitude[0], start_longtitude[1])
        end_gps_position = GPSPosition(end_latitude[0], end_latitude[1], end_longtitude[0], end_longtitude[1])
        id = self.__generator.generate_unique_id()
        new_property = Property(id, property_number, description, (start_gps_position, end_gps_position))
        start_node = KDNode((new_property.start_lat, new_property.start_lon), new_property)
        end_node = KDNode((new_property.end_lat, new_property.end_lon), new_property)
        self.properties_tree.insert(start_node)
        self.properties_tree.insert(end_node)
        self.all_tree.insert(start_node)
        self.all_tree.insert(end_node)
        
        #TODO Doplnit aktualizaciu referencii 
        self._update_parcel_references(new_property)
        

    def add_parcel(self, parcel_data):
        """
        Add a parcel to the system.
        :param parcel_data: A dictionary containing parcel data (including id, description, gps_coordinates).
        """
        new_parcel = Parcel(parcel_data["id"], parcel_data["description"], parcel_data["gps_coordinates"], [])
        self.parcels_tree.insert(new_parcel)
        self.all_tree.insert(new_parcel)
        self._update_property_references(new_parcel)

    def _update_parcel_references(self, property_obj):
        """
        Update the list of parcels that a property belongs to.
        :param property_obj: The property object to be updated.
        """
        for parcel in self.parcels_tree.in_order_traversal():
            if self._has_common_coordinates(parcel.gps_coordinates, property_obj.gps_coordinates):
                property_obj.parcels.append(parcel)
                parcel.properties.append(property_obj)

    def _update_property_references(self, parcel_obj):
        """
        Update the list of properties that are located on the parcel.
        :param parcel_obj: The parcel object to be updated.
        """
        for property in self.properties_tree.in_order_traversal():
            if self._has_common_coordinates(parcel_obj.gps_coordinates, property.gps_coordinates):
                parcel_obj.properties.append(property)
                property.parcels.append(parcel_obj)

    def _has_common_coordinates(self, gps_coordinates_1, gps_coordinates_2):
        """
        Check if two sets of GPS coordinates have any points in common.
        :param gps_coordinates_1: First set of GPS coordinates.
        :param gps_coordinates_2: Second set of GPS coordinates.
        :return: True if they have at least one point in common, False otherwise.
        """
        return any(point in gps_coordinates_2 for point in gps_coordinates_1)

    def search_properties_by_gps(self, gps_position):
        """
        Search properties that match the given GPS position.
        :param gps_position: GPS position to search for.
        :return: List of properties matching the GPS position.
        """
        return self.properties_tree.search(gps_position)

    def search_parcels_by_gps(self, gps_position):
        """
        Search parcels that match the given GPS position.
        :param gps_position: GPS position to search for.
        :return: List of parcels matching the GPS position.
        """
        return self.parcels_tree.search(gps_position)

    def search_all_by_gps(self, gps_position):
        """
        Search all properties and parcels that match the given GPS position.
        :param gps_position: GPS position to search for.
        :return: List of properties and parcels matching the GPS position.
        """
        return self.all_tree.search(gps_position)

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
