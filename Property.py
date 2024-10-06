#nehnutelnost
class Property:
    def __init__(self, property_number, description, boundary):
        self.property_number = property_number
        self.description = description
        self.parcels = []         # Zoznam referencií na parcely
        self.boundary = boundary  # Dve GPS pozície určujúce hranice nehnuteľnosti
        
    def add_parcel(self, parcel):
        self.parcels.append(parcel)