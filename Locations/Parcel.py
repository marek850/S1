from Locations.Area import Area


class Parcel(Area):
    def __init__(self, unique_id, parcel_number, description, boundary):
        super().__init__(unique_id, boundary, description)
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
    def remove_property(self, property):
       self.properties.remove(property)
        
        
    def __str__(self):
        return f"Parcela {self.__parcel_number}: {self.description}, Zaciatok: {self.boundary[0]}, Koniec: {self.boundary[1]}\n"
    def get_data(self):
        return "".join(f"par,{self.unique_id},{self.__parcel_number},{self.description},{self.start_lat_dir},{abs(self.start_lat)},{self.start_lon_dir},\
                       {abs(self.start_lon)},{self.end_lat_dir},{self.end_lat},{self.end_lon_dir},{self.end_lon}")
    @property
    def parcel_number(self):
        return self.__parcel_number

    @property
    def properties(self):
        return self.__properties
    
    @properties.setter
    def properties(self, value):
        self.__properties = value
class ParcelGui():
    def __init__(self, parcel):
        self.__description = parcel.description
        self.__parcel_number = parcel.parcel_number
        self.__unique_id = parcel.unique_id
        self.__boundary = parcel.boundary
        self.__properties = parcel.properties
    def __eq__(self, other):
        if isinstance(other, ParcelGui):
            if self.unique_id == other.unique_id:
                return True
        return False  
    
    def __str__(self):
        properties_str = "\n".join([f"{property}" for property in self.__properties])
        return (
            f"Parcela: Cislo: {self.__parcel_number}, Popis: {self.__description}, "
            f"Zaciatok: {self.__boundary[0]}, Koniec: {self.__boundary[1]}\n"
            f"Nehnutelnosti na parcele:\n{properties_str}"
        )
    
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def parcel_number(self):
        return self.__parcel_number

    @parcel_number.setter
    def parcel_number(self, value):
        self.__parcel_number = value

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