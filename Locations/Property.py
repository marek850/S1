#nehnutelnost
from Locations import Area


class Property(Area):
    def __init__(self, unique_id, property_number, description, boundary):
        super().__init__(unique_id, boundary, description, property_number)
        self.__property_number = property_number
        self.__parcels = []         
        
    def add_parcel(self, parcel):
        self.__parcels.append(parcel)
        
    def __str__(self):
        return f"Property {self.__property_number}: {self.__description}"
    @property
    def property_number(self):
        return self.__property_number

    @property_number.setter
    def property_number(self, value):
        self.__property_number = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def parcels(self):
        return self.__parcels

    @property
    def boundary(self):
        return self.__boundary

    @boundary.setter
    def boundary(self, value):
        self.__boundary = value