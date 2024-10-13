class Parcel:
    def __init__(self, parcel_number, description, boundary):
        self.parcel_number = parcel_number
        self.description = description
        self.properties = []       # Zoznam referencií na nehnuteľnosti
        self.boundary = boundary   # Dve GPS pozície určujúce hranice parcely

    def add_property(self, property):
        self.properties.append(property)
        
    def __str__(self):
        boundary_str = f"Boundary: [{self.boundary[0]}, {self.boundary[1]}]"
        return f"Parcel {self.parcel_number}: {self.description}, {boundary_str}, Properties: {len(self.properties)}"