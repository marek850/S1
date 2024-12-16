from 
class KDNode(IDataNode):
    def __init__(self, keys: tuple, data):
        self.__dim = 0
        self.__keys = keys         # Tuple klucov
        self.__data = data
        self.__parent = None        # Rodič
        self.__left = None          # Ľavý syn
        self.__right = None         # Pravý syn
        
    @property
    def dim(self):
        return self.__dim

    @dim.setter
    def dim(self, value):
        self.__dim = value

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, value):
        self.__keys = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value
   