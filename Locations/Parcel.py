from Locations.Area import Area


class Parcel(Area):
    def __init__(self, unique_id, parcel_number, description, boundary):
        super().__init__(unique_id, boundary, description, parcel_number)
        self.__parcel_number = parcel_number
        self.__properties = []   
    
    def __eq__(self, other):
        if isinstance(other, Parcel):
            if self.unique_id == other.unique_id:
                return True
        return False

    def add_property(self, property):
        for p in self.properties:
            if p == property:
                return
        self.properties.append(property)
        
    def __str__(self):
        boundary_str = f"Boundary: [{self.__boundary[0]}, {self.__boundary[1]}]"
        return f"Parcel {self.__parcel_number}: {self.__description}, {boundary_str}, Properties: {len(self.__properties)}"
    @property
    def parcel_number(self):
        return self.__parcel_number

    @property
    def properties(self):
        return self.__properties
class ParcelGui():
    def __init__(self, parcel):
        self.__description = parcel.description
        self.__property_number = parcel.parcel_number
        self.__unique_id = parcel.unique_id
        self.__boundary = parcel.boundary
    def __eq__(self, other):
        if isinstance(other, ParcelGui):
            if self.unique_id == other.unique_id:
                return True
        return False  
    def __str__(self):      
        return f"Parcela: Cislo:{self.parcel_number}, Popis: {self.__description} Zaciatok: {self.__boundary[0]}, Koniec: {self.__boundary[1]}\n"
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
