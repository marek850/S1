class  GPSPosition:
    def __init__(self, latitude_direction, latitude_value, longitude_direction, longitude_value):
        self.latitude_direction = latitude_direction    # 'N' alebo 'S'
        self.latitude_value = latitude_value            # hodnota zemepisnej šírky
        self.longitude_direction = longitude_direction  # 'E' alebo 'W'
        self.longitude_value = longitude_value          # hodnota zemepisnej dĺžky
    def __str__(self):
        return f"{self.latitude_direction}{self.latitude_value}, {self.longitude_direction}{self.longitude_value}"