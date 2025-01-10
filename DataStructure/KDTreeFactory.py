from DataStructure.DataStructure import IDataStructure
from DataStructure.IDataStructureFactory import IDataStructureFactory
from DataStructure.KDNode import KDNode
from DataStructure.KDTree import KDTree


class TreeFactory(IDataStructureFactory):
    def __init__(self, type: str, *args):
        self.type = type
        self.args = args
    def create_structure(self) -> IDataStructure:
        if self.type == "KDTree":
            return KDTree(*self.args)
    