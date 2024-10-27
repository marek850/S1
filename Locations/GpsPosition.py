class  GPSPosition:
    def __init__(self, latitude_direction: chr, latitude_value: float, longitude_direction: chr, longitude_value: float):
        self.__latitude_direction = latitude_direction    # 'N' alebo 'S'
        self.__latitude_value = latitude_value            # hodnota zemepisnej šírky
        self.__longitude_direction = longitude_direction  # 'E' alebo 'W'
        self.__longitude_value = longitude_value          # hodnota zemepisnej dĺžky
    
    def __eq__(self, other):
        if isinstance(other, GPSPosition):
            if self.latitude_direction == other.latitude_direction and self.latitude_value == other.latitude_value and \
            self.longitude_direction == other.longitude_direction and self.longitude_value == other.longitude_value:
                return True
        return False
    
    def __str__(self):
        return f"Sirka: {self.latitude_value}, Dlzka: {self.longitude_value}"
    @property
    def latitude_direction(self):
        return self.__latitude_direction

    @latitude_direction.setter
    def latitude_direction(self, value):
        if value not in ['N', 'S']:
            raise ValueError("Latitude direction must be 'N' or 'S'")
        self.__latitude_direction = value

    @property
    def latitude_value(self):
        if self.__latitude_direction == 'N':
            return self.__latitude_value
        elif self.__latitude_direction == 'S':
                    return -self.__latitude_value
    @latitude_value.setter
    def latitude_value(self, value):
        self.__latitude_value = value

    @property
    def longitude_direction(self):
        return self.__longitude_direction

    @longitude_direction.setter
    def longitude_direction(self, value):
        if value not in ['E', 'W']:
            raise ValueError("Longitude direction must be 'E' or 'W'")
        self.__longitude_direction = value

    @property
    def longitude_value(self):
        if self.__longitude_direction == 'E':
            return self.__longitude_value
        elif self.__longitude_direction == 'W':
            return -self.__longitude_value

    @longitude_value.setter
    def longitude_value(self, value):
        self.__longitude_value = value