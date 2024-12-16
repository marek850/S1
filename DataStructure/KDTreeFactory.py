from DataStructure.DataStructure import IDataStructure
from DataStructure.IDataStructureFactory import IDataStructureFactory
from DataStructure.KDNode import KDNode
from DataStructure.KDTree import KDTree
from DataStructure.Node import IDataNode


class KDTreeFactory(IDataStructureFactory):
    def __init__(self, dimension: int = 2):
        self.dimension = dimension
    def create_structure(self) -> IDataStructure:
        return KDTree(self.dimension)
    
    def create_node(self, keys: tuple, data: object) -> IDataNode:
        return KDNode(keys, data)