from UserInterface.Command import Command


class PropertyEdit(Command):
    
    def __init__(self, app=None, 
                 property_id = None,
                 property_number=None, 
                 description=None, 
                 latitude_direction_1=None, 
                 latitude_value_1=None, 
                 longitude_direction_1=None, 
                 longitude_value_1=None, 
                 latitude_direction_2=None, 
                 latitude_value_2=None, 
                 longitude_direction_2=None, 
                 longitude_value_2=None, 
                 initial_property_number=None, 
                 initial_description=None,
                 initial_latitude_direction_1=None, 
                 initial_latitude_value_1=None, 
                 initial_longitude_direction_1=None, 
                 initial_longitude_value_1=None, 
                 initial_latitude_direction_2=None, 
                 initial_latitude_value_2=None, 
                 initial_longitude_direction_2=None, 
                 initial_longitude_value_2=None):
        self.app = app
        self.property_id = property_id
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
        self.initial_property_number = initial_property_number
        self.initial_description = initial_description
        self.initial_latitude_direction_1 = initial_latitude_direction_1
        self.initial_latitude_value_1 = initial_latitude_value_1
        self.initial_longitude_direction_1 = initial_longitude_direction_1
        self.initial_longitude_value_1 = initial_longitude_value_1
        self.initial_latitude_direction_2 = initial_latitude_direction_2
        self.initial_latitude_value_2 = initial_latitude_value_2
        self.initial_longitude_direction_2 = initial_longitude_direction_2
        self.initial_longitude_value_2 = initial_longitude_value_2

    def execute(self):
        self.app.edit_property(
            self.property_id,
            self.property_number,
            self.description,
            self.latitude_direction_1,
            self.latitude_value_1,
            self.longitude_direction_1,
            self.longitude_value_1,
            self.latitude_direction_2,
            self.latitude_value_2,
            self.longitude_direction_2,
            self.longitude_value_2,
            self.initial_property_number,
            self.initial_description,
            self.initial_latitude_direction_1,
            self.initial_latitude_value_1,
            self.initial_longitude_direction_1,
            self.initial_longitude_value_1,
            self.initial_latitude_direction_2,
            self.initial_latitude_value_2,
            self.initial_longitude_direction_2,
            self.initial_longitude_value_2
        )