
import customtkinter as csc
from DataGeneration.Tester import OpGenerator
from DataStructure.KDNode import KDNode
from GUI.MainApp import MainApp
from GeoApp import GeoApp
from Locations.GpsPosition import GPSPosition
from Locations.Area import AreaUnit
from Locations.Parcel import Parcel


  

def main():
    
    operationGenerator = OpGenerator()
    #operationGenerator.generate_inserts(10000)
    #operationGenerator.generate_searches()
    #operationGenerator.generate_deletes() 
    #operationGenerator.test()

    
    geo_app = GeoApp()
    app = MainApp(geo_app)
    app.mainloop()
if __name__ == "__main__":  
    main()
   