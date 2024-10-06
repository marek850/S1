class Parcel:
    def __init__(self, parcel_number, description, boundary):
        self.parcel_number = parcel_number
        self.description = description
        self.properties = []       # Zoznam referencií na nehnuteľnosti
        self.boundary = boundary   # Dve GPS pozície určujúce hranice parcely

    def add_property(self, property):
        self.properties.append(property)