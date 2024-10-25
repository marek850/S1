from Locations import Area


class Parcel(Area):
    def __init__(self, unique_id, parcel_number, description, boundary):
        super().__init__(unique_id, boundary, description, parcel_number)
        self.__parcel_number = parcel_number
        self.__properties = []   

    def add_property(self, property):
        self.__properties.append(property)
        
    def __str__(self):
        boundary_str = f"Boundary: [{self.__boundary[0]}, {self.__boundary[1]}]"
        return f"Parcel {self.__parcel_number}: {self.__description}, {boundary_str}, Properties: {len(self.__properties)}"
    @property
    def parcel_number(self):
        return self.__parcel_number

    @property
    def description(self):
        return self.__description

    @property
    def properties(self):
        return self.__properties

    @property
    def boundary(self):
        return self.__boundary