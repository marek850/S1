from UserInterface.Command import Command


class PropertyAdd(Command):
    
    def __init__(self, 
            app = None,
            property_number = None,
            description = None,
            latitude_direction_1 = None,
            latitude_value_1 = None, 
            longitude_direction_1 = None,
            longitude_value_1 = None,  
            latitude_direction_2 = None,
            latitude_value_2 = None, 
            longitude_direction_2 = None,
            longitude_value_2 = None):
        self.app = app
        self.property_number = property_number
        self.description = description
        self.latitude_direction_1 = latitude_direction_1
        self.latitude_value_1 = latitude_value_1
        self.longitude_direction_1 = longitude_direction_1
        self.longitude_value_1 = longitude_value_1
        self.latitude_direction_2 = latitude_direction_2
        self.latitude_value_2 = latitude_value_2
        self.longitude_direction_2 = longitude_direction_2
        self.longitude_value_2 = longitude_value_2

    def execute(self):
        self.app.add_property(
            self.property_number,
            self.description,
            self.latitude_direction_1,
            self.latitude_value_1,
            self.longitude_direction_1,
            self.longitude_value_1,
            self.latitude_direction_2,
            self.latitude_value_2,
            self.longitude_direction_2,
            self.longitude_value_2)