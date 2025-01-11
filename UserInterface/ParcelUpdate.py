from UserInterface.Command import Command


class ParcelEdit(Command):
    
    def __init__(self, app=None, parcel_id = None, parcel_number=None, description=None, latitude_direction_1=None, latitude_value_1=None, longitude_direction_1=None, longitude_value_1=None, latitude_direction_2=None, latitude_value_2=None, longitude_direction_2=None, longitude_value_2=None, initial_parcel_number=None, initial_description=None, initial_latitude_direction_1=None, initial_latitude_value_1=None, initial_longitude_direction_1=None, initial_longitude_value_1=None, initial_latitude_direction_2=None, initial_latitude_value_2=None, initial_longitude_direction_2=None, initial_longitude_value_2=None):
        self.app = app
        self.parcel_id = parcel_id
        self.parcel_number = parcel_number
        self.description = description
        self.latitude_direction_1 = latitude_direction_1
        self.latitude_value_1 = latitude_value_1
        self.longitude_direction_1 = longitude_direction_1
        self.longitude_value_1 = longitude_value_1
        self.latitude_direction_2 = latitude_direction_2
        self.latitude_value_2 = latitude_value_2
        self.longitude_direction_2 = longitude_direction_2
        self.longitude_value_2 = longitude_value_2
        self.initial_parcel_number = initial_parcel_number
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
        self.app.edit_parcel(
            self.parcel_id,
            self.parcel_number,
            self.description,
            self.latitude_direction_1,
            self.latitude_value_1,
            self.longitude_direction_1,
            self.longitude_value_1,
            self.latitude_direction_2,
            self.latitude_value_2,
            self.longitude_direction_2,
            self.longitude_value_2,
            self.initial_parcel_number,
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