#nehnutelnost
from Locations.Area import AreaUnit


class Property(AreaUnit):
    def __init__(self, unique_id, property_number, description, boundary):
        super().__init__(unique_id, boundary, description)
        self.__number = property_number
        self.__parcels = []       
        
    def __eq__(self, other):
        if isinstance(other, Property):
            if self.unique_id == other.unique_id:
                return True
        return False  
    def __str__(self):      
        return f"Nehnutelnost: Cislo:{self.__number}, Popis: {self.description} Zaciatok: {self.boundary[0]}, Koniec: {self.boundary[1]}\n"    
    def add_parcel(self, parcel):
        for p in self.parcels:
            if p == parcel:
                return
        self.parcels.append(parcel)
    def remove_parcel(self, parcel):
        self.parcels.remove(parcel)
             
             
    def get_data(self):
        return "".join(f"pro,{self.unique_id},{self.number},{self.description},{self.start_lat_dir},{abs(self.start_lat)},{self.start_lon_dir},{abs(self.start_lon)},{self.end_lat_dir},{self.end_lat},{self.end_lon_dir},{self.end_lon}")   
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

   
    @property
    def parcels(self):
        return self.__parcels

    @parcels.setter
    def parcels(self, value):
        self.__parcels = value

class PropertyGui():
    def __init__(self, property):
        self.__description = property.description
        self.__number = property.number
        self.__unique_id = property.unique_id
        self.__boundary = property.boundary
        self.__parcels = property.parcels
    def __eq__(self, other):
        if isinstance(other, PropertyGui):
            if self.unique_id == other.unique_id:
                return True
        return False  
    
    def __str__(self):
        parcels_str = "".join([f"{parcel}\n" for parcel in self.__parcels])
        return (
            f"Nehnutelnost: Cislo: {self.__number}, Popis: {self.__description}, "
            f"Zaciatok: {self.__boundary[0]}, Koniec: {self.__boundary[1]}\n"
            f"Parcely:\n{parcels_str}"
        )
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

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
