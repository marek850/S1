from abc import ABC
from Locations.Area import AreaUnit


class CompositeArea(AreaUnit, ABC):
    def __init__(self, unique_id, parcel_number, description, boundary):
        super().__init__(unique_id, boundary, description)
        self.children = []

    def add(self, unit: AreaUnit):
        self.children.append(unit)

    def remove(self, unit: AreaUnit):
        self.children.remove(unit)