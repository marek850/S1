class KDNode:
    def __init__(self, keys, data):
        self.dim = 0
        self.keys = keys         # Tuple klucov
        self.data = data
        self.parent = None        # Rodič
        self.left = None          # Ľavý syn
        self.right = None         # Pravý syn