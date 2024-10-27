#nehnutelnost
from Locations.Area import Area


class Property(Area):
    def __init__(self, unique_id, property_number, description, boundary):
        super().__init__(unique_id, boundary, description, property_number)
        self.__property_number = property_number
        self.__parcels = []       
        
    def __eq__(self, other):
        if isinstance(other, Property):
            if self.unique_id == other.unique_id:
                return True
        return False  
        
    def add_parcel(self, parcel):
        for p in self.parcels:
            if p == parcel:
                return
        self.parcels.append(parcel)
        
    def __str__(self):
        return f"Nehnutelnost: {self.__property_number}: {self.__description}"
    @property
    def property_number(self):
        return self.__property_number

    @property_number.setter
    def property_number(self, value):
        self.__property_number = value

   
    @property
    def parcels(self):
        return self.__parcels


class PropertyGui():
    def __init__(self, property):
        self.__description = property.description
        self.__property_number = property.property_number
        self.__unique_id = property.unique_id
        self.__boundary = property.boundary
    def __eq__(self, other):
        if isinstance(other, PropertyGui):
            if self.unique_id == other.unique_id:
                return True
        return False  
    def __str__(self):      
        return f"Nehnutelnost: Cislo:{self.__property_number}, Popis: {self.__description} Zaciatok: {self.__boundary[0]}, Koniec: {self.__boundary[1]}\n"
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def property_number(self):
        return self.__property_number

    @property_number.setter
    def property_number(self, value):
        self.__property_number = value

    @property
    def unique_id(self):
        return self.__unique_id

    @unique_id.setter
    def unique_id(self, value):
        self.__unique_id = value
    @property
    def boundary(self):
        return self.__boundary

    @boundary.setter
    def boundary(self, value):
        self.__boundary = value
