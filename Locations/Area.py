from abc import ABC, abstractmethod
from typing import Tuple

from Locations import GpsPosition

class Area(ABC):
    def __init__(self, unique_id: int, boundary: tuple, description: str):
        self.__unique_id = unique_id
        self.__boundary = boundary
        self.__description = description
    @property
    def unique_id(self):
        return self.__unique_id

    @property
    def boundary(self):
        return self.__boundary

    @property
    def description(self):
        return self.__description

    @property
    def start_lat(self): 
        return self.boundary[0].latitude_value
    @property
    def start_lon(self): 
        return self.boundary[0].longitude_value
    @property
    def end_lat(self): 
        return self.boundary[1].latitude_value
    @property
    def end_lon(self): 
        return self.boundary[1].longitude_value
    @property
    def start_lat_dir(self): 
        return self.boundary[0].latitude_direction
    @property
    def start_lon_dir(self): 
        return self.boundary[0].longitude_direction
    @property
    def end_lat_dir(self): 
        return self.boundary[1].latitude_direction
    @property
    def end_lon_dir(self): 
        return self.boundary[1].longitude_direction
    @property
    def number(self):
        return self.__number   
    @unique_id.setter
    def unique_id(self, value):
        self.__unique_id = value
    
    @boundary.setter
    def boundary(self, value):
        if isinstance(value, tuple) and len(value) == 2 and all(isinstance(pos, GpsPosition) for pos in value):
            self.__boundary = value
        else:
            raise ValueError("Boundary must be a tuple of size 2 with both elements being instances of GpsPosition")

    @description.setter
    def description(self, value):
        self.__description = value

    @number.setter
    def number(self, value):
        self.__number = value