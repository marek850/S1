class KDNode:
    def __init__(self, point, data):
        self.point = point        # GPSPosition bod , tuple (x,y)
        self.data = data
        self.left = None          # Ľavý syn
        self.right = None         # Pravý syn