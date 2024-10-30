class KDNode:
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
    def nastav_syna(self, povodny_syn, novy_syn):
        if self.left == povodny_syn:
            self.left = novy_syn
        elif self.right == povodny_syn:
            self.right = novy_syn
    def vymen_pozicie_vrcholov(self, vrchol):
        povodna_uroven = vrchol.dim
        povodny_otec = vrchol.parent
        povodny_lavy_syn = vrchol.left
        povodny_pravy_syn = vrchol.right
        # nastavenie nahradneho vrcholu na poziciu vymazavaneho vrcholu
        if self.parent is not None:
            self.parent.nastav_syna(self, vrchol)
        vrchol.dim = self.dim
        vrchol.parent = self.parent
        if self.left is vrchol:
            vrchol.left = self
        else:
            vrchol.left = self.left

        if self.right is vrchol:
            vrchol.right = self
        else:
            vrchol.right = self.right

        if self.left is not None and self.left is not vrchol:
            self.left.parent = vrchol
        if self.right is not None and self.right is not vrchol:
            self.right.parent = vrchol

        # nastavenie vymazavaneho vrcholu na poziciu nahradneho vrcholu
        if povodny_otec is self:
            self.parent = vrchol
        else:
            self.parent = povodny_otec
            if povodny_otec is not None:
                povodny_otec.nastav_syna(vrchol, self)
        self.dim = povodna_uroven
        self.left = povodny_lavy_syn
        self.right = povodny_pravy_syn

        if povodny_lavy_syn is not None:
            povodny_lavy_syn.parent = self
        if povodny_pravy_syn is not None:
            povodny_pravy_syn.parent = self