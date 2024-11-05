import threading
from tkinter import messagebox
import customtkinter as ctk
import tkinter
from Locations.GpsPosition import GPSPosition as Gps

class MainApp(ctk.CTk):
    def __init__(self, app):
        super().__init__()
        self.title("Magula S1")
        self.geometry("1280x720")
        self.app = app

        
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=4)  
        self.grid_rowconfigure(0, weight=1)     

       
        self.menu_frame = MenuFrame(self, self.show_frame, self.app)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew")
        
        
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (PropertyInsert, ParcelInsert,  PropertySearch,  ParcelSearch, SearchAll, Tester):
            frame = F(parent=self.container, controller=self, app=self.app)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        
        self.show_frame(PropertyInsert)
        self.update()
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        self.update()
        frame.tkraise()
        self.update()
        


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback, app):
        super().__init__(parent)
        self.app = app
        self.show_frame_callback = show_frame_callback
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        
        insert_button = ctk.CTkButton(self, text="Pridat Nehnutelnost", command=lambda: self.show_frame_callback(PropertyInsert))
        insert_button.pack(pady=10, padx=10)
        
        insert_parcel_button = ctk.CTkButton(self, text="Pridat Parcelu", command=lambda: self.show_frame_callback(ParcelInsert))
        insert_parcel_button.pack(pady=10, padx=10)

        search_button = ctk.CTkButton(self, text="Nehnutelnosti", command=lambda: self.show_frame_callback(PropertySearch))
        search_button.pack(pady=10, padx=10)

        search_button = ctk.CTkButton(self, text="Parcely", command=lambda: self.show_frame_callback(ParcelSearch))
        search_button.pack(pady=10, padx=10)

        search_all_button = ctk.CTkButton(self, text="Nehnutelnosti a Parcely", command=lambda: self.show_frame_callback(SearchAll))
        search_all_button.pack(pady=10, padx=10)

        tester_button = ctk.CTkButton(self, text="Generovanie Dat", command=lambda: self.show_frame_callback(Tester))
        tester_button.pack(pady=10, padx=10)

# Property Insert Frame
class PropertyInsert(ctk.CTkFrame):
    def __init__(self, parent, controller, app):
        super().__init__(parent)
        self.controller = controller
        self.app = app
        
        label = ctk.CTkLabel(self, text="Pridanie Nehnutelnosti", font=("Arial", 20))
        label.grid(row=0, column=0, columnspan=4, pady=20, sticky="w")

        
        property_number_label = ctk.CTkLabel(self, text="Supisne cislo:")
        property_number_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.property_number_entry = ctk.CTkEntry(self)
        self.property_number_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        
        description_label = ctk.CTkLabel(self, text="Popis:")
        description_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.description_entry = ctk.CTkEntry(self)
        self.description_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Latitude Direction 1
        latitude_direction_label_1 = ctk.CTkLabel(self, text="Zemepisna sirka 1:")
        latitude_direction_label_1.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var_1 = ctk.StringVar()
        latitude_north_checkbox_1 = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var_1, value='North')
        latitude_north_checkbox_1.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox_1 = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var_1, value='South')
        latitude_south_checkbox_1.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        # Latitude Value 1
        latitude_value_label_1 = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky 1:")
        latitude_value_label_1.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry_1 = ctk.CTkEntry(self)
        self.latitude_value_entry_1.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Longitude Direction 1
        longitude_direction_label_1 = ctk.CTkLabel(self, text="Zemepisna dlzka 1:")
        longitude_direction_label_1.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var_1 = ctk.StringVar()
        longitude_east_checkbox_1 = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var_1, value='East')
        longitude_east_checkbox_1.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox_1 = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var_1, value='West')
        longitude_west_checkbox_1.grid(row=5, column=2, padx=5, pady=5, sticky="w")

        # Longitude Value 1
        longitude_value_label_1 = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky 1:")
        longitude_value_label_1.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry_1 = ctk.CTkEntry(self)
        self.longitude_value_entry_1.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # Latitude Direction 2
        latitude_direction_label_2 = ctk.CTkLabel(self, text="Zemepisna sirka 2:")
        latitude_direction_label_2.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var_2 = ctk.StringVar()
        latitude_north_checkbox_2 = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var_2, value='North')
        latitude_north_checkbox_2.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox_2 = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var_2, value='South')
        latitude_south_checkbox_2.grid(row=7, column=2, padx=5, pady=5, sticky="w")

        # Latitude Value 2
        latitude_value_label_2 = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky 2:")
        latitude_value_label_2.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry_2 = ctk.CTkEntry(self)
        self.latitude_value_entry_2.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        # Longitude Direction 2
        longitude_direction_label_2 = ctk.CTkLabel(self, text="Zemepisna dlzka 2:")
        longitude_direction_label_2.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var_2 = ctk.StringVar()
        longitude_east_checkbox_2 = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var_2, value='East')
        longitude_east_checkbox_2.grid(row=9, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox_2 = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var_2, value='West')
        longitude_west_checkbox_2.grid(row=9, column=2, padx=5, pady=5, sticky="w")

        # Longitude Value 2
        longitude_value_label_2 = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky 2:")
        longitude_value_label_2.grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry_2 = ctk.CTkEntry(self)
        self.longitude_value_entry_2.grid(row=10, column=1, padx=10, pady=5, sticky="w")

        self.update()
        add_property_button = ctk.CTkButton(self, text="Pridat", command=self.startAddProperty)
        add_property_button.grid(row=11, column=0, columnspan=3, pady=20, sticky="w", padx=100)
    

    def add_property(self):

        self.update()
        # Retrieve values from input fields
        property_number = self.property_number_entry.get().strip()
        description = self.description_entry.get().strip()

        # First GPS position
        latitude_direction_1 = self.latitude_direction_var_1.get()
        latitude_value_1 = float(self.latitude_value_entry_1.get().strip())
        longitude_direction_1 = self.longitude_direction_var_1.get()
        longitude_value_1 = float(self.longitude_value_entry_1.get().strip())

        # Second GPS position
        latitude_direction_2 = self.latitude_direction_var_2.get()
        latitude_value_2 = float(self.latitude_value_entry_2.get().strip())
        longitude_direction_2 = self.longitude_direction_var_2.get()
        longitude_value_2 = float(self.longitude_value_entry_2.get().strip())

        # Validate the input
        if not property_number:
            self.show_alert("Supisne cislo je povinne.")
            return
        if not description:
            self.show_alert("Popis je povinny.")
            return

        if latitude_direction_1 not in ['North', 'South']:
            self.show_alert("Vyberte smer pre prvu zemepisnu sirku (North/South).")
            return
        if not self.is_valid_number(latitude_value_1):
            self.show_alert("Hodnota prvej zemepisnej sirky musi byt cislo.")
            return
        if longitude_direction_1 not in ['East', 'West']:
            self.show_alert("Vyberte smer pre prvu zemepisnu dlzku (East/West).")
            return
        if not self.is_valid_number(longitude_value_1):
            self.show_alert("Hodnota prvej zemepisnej dlzky musi byt cislo.")
            return
        
        if latitude_direction_2 not in ['North', 'South']:
            self.show_alert("Vyberte smer pre druhu zemepisnu sirku (North/South).")
            return
        if not self.is_valid_number(latitude_value_2):
            self.show_alert("Hodnota druhej zemepisnej sirky musi byt cislo.")
            return
        if longitude_direction_2 not in ['East', 'West']:
            self.show_alert("Vyberte smer pre druhu zemepisnu dlzku (East/West).")
            return
        if not self.is_valid_number(longitude_value_2):
            self.show_alert("Hodnota druhej zemepisnej dlzky musi byt cislo.")
            return
        # Convert directions to single letters
        latitude_direction_1 = latitude_direction_1[0]  # "North" -> "N", "South" -> "S"
        longitude_direction_1 = longitude_direction_1[0]  # "East" -> "E", "West" -> "W"
        latitude_direction_2 = latitude_direction_2[0]
        longitude_direction_2 = longitude_direction_2[0]
        self.update()
        # Call the app method with the collected values
        self.app.add_property(
            property_number,
            description,
            latitude_direction_1,
            latitude_value_1, 
            longitude_direction_1,
            longitude_value_1,  
            latitude_direction_2,
            latitude_value_2, 
            longitude_direction_2,
            longitude_value_2
        )
        self.update()
        self.clear_form()
        self.update()
        self.show_success_message()
    def startAddProperty(self):
        threading.Thread(target=self.add_property).start()
        
    def show_success_message(self):
        messagebox.showinfo("Pridane", "Nehnuteľnosť bola úspešne pridaná.")
    def show_alert(self, message):
        
        messagebox.showerror("Chyba", message)
    def clear_form(self):
        # Clear all input fields
        self.property_number_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')
        self.latitude_value_entry_1.delete(0, 'end')
        self.longitude_value_entry_1.delete(0, 'end')
        self.latitude_value_entry_2.delete(0, 'end')
        self.longitude_value_entry_2.delete(0, 'end')

        # Reset the radio buttons
        self.latitude_direction_var_1.set('')
        self.longitude_direction_var_1.set('')
        self.latitude_direction_var_2.set('')
        self.longitude_direction_var_2.set('')

    def is_valid_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

class ParcelInsert(ctk.CTkFrame):
    def __init__(self, parent, controller, app):
        super().__init__(parent)
        self.controller = controller
        self.app = app

        
        label = ctk.CTkLabel(self, text="Pridanie Parcely", font=("Arial", 20))
        label.grid(row=0, column=0, columnspan=4, pady=20, sticky="w")

        
        parcel_number_label = ctk.CTkLabel(self, text="Cislo parcely:")
        parcel_number_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.parcel_number_entry = ctk.CTkEntry(self)
        self.parcel_number_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        
        description_label = ctk.CTkLabel(self, text="Popis:")
        description_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.description_entry = ctk.CTkEntry(self)
        self.description_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Latitude Direction 1
        latitude_direction_label_1 = ctk.CTkLabel(self, text="Zemepisna sirka 1:")
        latitude_direction_label_1.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var_1 = ctk.StringVar()
        latitude_north_checkbox_1 = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var_1, value='North')
        latitude_north_checkbox_1.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox_1 = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var_1, value='South')
        latitude_south_checkbox_1.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        # Latitude Value 1
        latitude_value_label_1 = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky 1:")
        latitude_value_label_1.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry_1 = ctk.CTkEntry(self)
        self.latitude_value_entry_1.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Longitude Direction 1
        longitude_direction_label_1 = ctk.CTkLabel(self, text="Zemepisna dlzka 1:")
        longitude_direction_label_1.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var_1 = ctk.StringVar()
        longitude_east_checkbox_1 = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var_1, value='East')
        longitude_east_checkbox_1.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox_1 = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var_1, value='West')
        longitude_west_checkbox_1.grid(row=5, column=2, padx=5, pady=5, sticky="w")

        # Longitude Value 1
        longitude_value_label_1 = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky 1:")
        longitude_value_label_1.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry_1 = ctk.CTkEntry(self)
        self.longitude_value_entry_1.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # Latitude Direction 2
        latitude_direction_label_2 = ctk.CTkLabel(self, text="Zemepisna sirka 2:")
        latitude_direction_label_2.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var_2 = ctk.StringVar()
        latitude_north_checkbox_2 = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var_2, value='North')
        latitude_north_checkbox_2.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox_2 = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var_2, value='South')
        latitude_south_checkbox_2.grid(row=7, column=2, padx=5, pady=5, sticky="w")

        # Latitude Value 2
        latitude_value_label_2 = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky 2:")
        latitude_value_label_2.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry_2 = ctk.CTkEntry(self)
        self.latitude_value_entry_2.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        # Longitude Direction 2
        longitude_direction_label_2 = ctk.CTkLabel(self, text="Zemepisna dlzka 2:")
        longitude_direction_label_2.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var_2 = ctk.StringVar()
        longitude_east_checkbox_2 = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var_2, value='East')
        longitude_east_checkbox_2.grid(row=9, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox_2 = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var_2, value='West')
        longitude_west_checkbox_2.grid(row=9, column=2, padx=5, pady=5, sticky="w")

        # Longitude Value 2
        longitude_value_label_2 = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky 2:")
        longitude_value_label_2.grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry_2 = ctk.CTkEntry(self)
        self.longitude_value_entry_2.grid(row=10, column=1, padx=10, pady=5, sticky="w")

        self.update()
        add_parcel_button = ctk.CTkButton(self, text="Pridat", command=self.startAddParcel)
        add_parcel_button.grid(row=11, column=0, columnspan=3, pady=20, sticky="w", padx=100)
    

    def add_parcel(self):

        self.update()
        # Retrieve values from input fields
        parcel_number = self.parcel_number_entry.get().strip()
        description = self.description_entry.get().strip()

        # First GPS position
        latitude_direction_1 = self.latitude_direction_var_1.get()
        latitude_value_1 = float(self.latitude_value_entry_1.get().strip())
        longitude_direction_1 = self.longitude_direction_var_1.get()
        longitude_value_1 = float(self.longitude_value_entry_1.get().strip())

        # Second GPS position
        latitude_direction_2 = self.latitude_direction_var_2.get()
        latitude_value_2 = float(self.latitude_value_entry_2.get().strip())
        longitude_direction_2 = self.longitude_direction_var_2.get()
        longitude_value_2 = float(self.longitude_value_entry_2.get().strip())

        # Validate the input
        if not parcel_number:
            self.show_alert("Parcelne cislo je povinne.")
            return
        if not description:
            self.show_alert("Popis je povinny.")
            return

        if latitude_direction_1 not in ['North', 'South']:
            self.show_alert("Vyberte smer pre prvu zemepisnu sirku (North/South).")
            return
        if not self.is_valid_number(latitude_value_1):
            self.show_alert("Hodnota prvej zemepisnej sirky musi byt cislo.")
            return
        if longitude_direction_1 not in ['East', 'West']:
            self.show_alert("Vyberte smer pre prvu zemepisnu dlzku (East/West).")
            return
        if not self.is_valid_number(longitude_value_1):
            self.show_alert("Hodnota prvej zemepisnej dlzky musi byt cislo.")
            return
        
        if latitude_direction_2 not in ['North', 'South']:
            self.show_alert("Vyberte smer pre druhu zemepisnu sirku (North/South).")
            return
        if not self.is_valid_number(latitude_value_2):
            self.show_alert("Hodnota druhej zemepisnej sirky musi byt cislo.")
            return
        if longitude_direction_2 not in ['East', 'West']:
            self.show_alert("Vyberte smer pre druhu zemepisnu dlzku (East/West).")
            return
        if not self.is_valid_number(longitude_value_2):
            self.show_alert("Hodnota druhej zemepisnej dlzky musi byt cislo.")
            return
        # Convert directions to single letters
        latitude_direction_1 = latitude_direction_1[0]  # "North" -> "N", "South" -> "S"
        longitude_direction_1 = longitude_direction_1[0]  # "East" -> "E", "West" -> "W"
        latitude_direction_2 = latitude_direction_2[0]
        longitude_direction_2 = longitude_direction_2[0]
        self.update()
        # Call the app method with the collected values
        self.app.add_parcel(
            parcel_number,
            description,
            latitude_direction_1,
            latitude_value_1, 
            longitude_direction_1,
            longitude_value_1,  
            latitude_direction_2,
            latitude_value_2, 
            longitude_direction_2,
            longitude_value_2
        )
        self.clear_form()
        self.update()
        self.show_success_message()
    def startAddParcel(self):
        threading.Thread(target=self.add_parcel).start()
        
    def show_success_message(self):
        messagebox.showinfo("Pridane", "Parcela bola úspešne pridaná.")
    def show_alert(self, message):
        
        messagebox.showerror("Chyba", message)
    def clear_form(self):
        # Clear all input fields
        self.parcel_number_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')
        self.latitude_value_entry_1.delete(0, 'end')
        self.longitude_value_entry_1.delete(0, 'end')
        self.latitude_value_entry_2.delete(0, 'end')
        self.longitude_value_entry_2.delete(0, 'end')

        # Reset the radio buttons
        self.latitude_direction_var_1.set('')
        self.longitude_direction_var_1.set('')
        self.latitude_direction_var_2.set('')
        self.longitude_direction_var_2.set('')

    def is_valid_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

class PropertyUpdate(ctk.CTkToplevel):
    def __init__(self, parent, controller, app, property_data):
        super().__init__(parent)
        self.controller = controller
        self.app = app
        # Extract data from property_data
        self.property_id = property_data.unique_id
        self.initial_property_number = property_data.property_number
        self.initial_description = property_data.description
        self.initial_latitude_direction_1 = property_data.boundary[0].latitude_direction
        self.initial_latitude_value_1 = abs(property_data.boundary[0].latitude_value)
        self.initial_longitude_direction_1 = property_data.boundary[0].longitude_direction
        self.initial_longitude_value_1 = abs(property_data.boundary[0].longitude_value)
        self.initial_latitude_direction_2 = property_data.boundary[1].latitude_direction
        self.initial_latitude_value_2 = abs(property_data.boundary[1].latitude_value)
        self.initial_longitude_direction_2 = property_data.boundary[1].longitude_direction
        self.initial_longitude_value_2 = abs(property_data.boundary[1].longitude_value)
        # Form fields with pre-filled values
        label = ctk.CTkLabel(self, text="Uprava Nehnutelnosti", font=("Arial", 20))
        label.grid(row=0, column=0, columnspan=4, pady=20, sticky="w")

        property_number_label = ctk.CTkLabel(self, text="Supisne cislo:")
        property_number_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.property_number_entry = ctk.CTkEntry(self)
        self.property_number_entry.insert(0, self.initial_property_number)
        self.property_number_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        description_label = ctk.CTkLabel(self, text="Popis:")
        description_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.description_entry = ctk.CTkEntry(self)
        self.description_entry.insert(0, self.initial_description)
        self.description_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Latitude Direction 1
        latitude_direction_label_1 = ctk.CTkLabel(self, text="Zemepisna sirka 1:")
        latitude_direction_label_1.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var_1 = ctk.StringVar(value=self.initial_latitude_direction_1)
        latitude_north_checkbox_1 = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var_1, value='N')
        latitude_north_checkbox_1.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox_1 = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var_1, value='S')
        latitude_south_checkbox_1.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        # Latitude Value 1
        latitude_value_label_1 = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky 1:")
        latitude_value_label_1.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry_1 = ctk.CTkEntry(self)
        self.latitude_value_entry_1.insert(0, self.initial_latitude_value_1)
        self.latitude_value_entry_1.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Longitude Direction 1
        longitude_direction_label_1 = ctk.CTkLabel(self, text="Zemepisna dlzka 1:")
        longitude_direction_label_1.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var_1 = ctk.StringVar(value=self.initial_longitude_direction_1)
        longitude_east_checkbox_1 = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var_1, value='E')
        longitude_east_checkbox_1.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox_1 = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var_1, value='W')
        longitude_west_checkbox_1.grid(row=5, column=2, padx=5, pady=5, sticky="w")

        # Longitude Value 1
        longitude_value_label_1 = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky 1:")
        longitude_value_label_1.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry_1 = ctk.CTkEntry(self)
        self.longitude_value_entry_1.insert(0, self.initial_longitude_value_1)
        self.longitude_value_entry_1.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # Latitude Direction 2
        latitude_direction_label_2 = ctk.CTkLabel(self, text="Zemepisna sirka 2:")
        latitude_direction_label_2.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var_2 = ctk.StringVar(value=self.initial_latitude_direction_2)
        latitude_north_checkbox_2 = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var_2, value='N')
        latitude_north_checkbox_2.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox_2 = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var_2, value='S')
        latitude_south_checkbox_2.grid(row=7, column=2, padx=5, pady=5, sticky="w")

        # Latitude Value 2
        latitude_value_label_2 = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky 2:")
        latitude_value_label_2.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry_2 = ctk.CTkEntry(self)
        self.latitude_value_entry_2.insert(0, self.initial_latitude_value_2)
        self.latitude_value_entry_2.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        # Longitude Direction 2
        longitude_direction_label_2 = ctk.CTkLabel(self, text="Zemepisna dlzka 2:")
        longitude_direction_label_2.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var_2 = ctk.StringVar(value=self.initial_longitude_direction_2)
        longitude_east_checkbox_2 = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var_2, value='E')
        longitude_east_checkbox_2.grid(row=9, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox_2 = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var_2, value='W')
        longitude_west_checkbox_2.grid(row=9, column=2, padx=5, pady=5, sticky="w")

        # Longitude Value 2
        longitude_value_label_2 = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky 2:")
        longitude_value_label_2.grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry_2 = ctk.CTkEntry(self)
        self.longitude_value_entry_2.insert(0, self.initial_longitude_value_2)
        self.longitude_value_entry_2.grid(row=10, column=1, padx=10, pady=5, sticky="w")

        # Update Property Button
        update_property_button = ctk.CTkButton(self, text="Upravit", command=self.update_property)
        update_property_button.grid(row=12, column=0, columnspan=3, pady=20, sticky="w", padx=100)
        

    def update_property(self):
        # Retrieve updated values from input fields
        property_number = self.property_number_entry.get().strip()
        description = self.description_entry.get().strip()
        latitude_direction_1 = self.latitude_direction_var_1.get()
        latitude_value_1 = float(self.latitude_value_entry_1.get().strip())
        longitude_direction_1 = self.longitude_direction_var_1.get()
        longitude_value_1 = float(self.longitude_value_entry_1.get().strip())
        latitude_direction_2 = self.latitude_direction_var_2.get()
        latitude_value_2 = float(self.latitude_value_entry_2.get().strip())
        longitude_direction_2 = self.longitude_direction_var_2.get()
        longitude_value_2 = float(self.longitude_value_entry_2.get().strip())


        # Update the property using the app method
        self.app.edit_property(
            self.property_id,
            property_number,
            description,
            latitude_direction_1,
            latitude_value_1,
            longitude_direction_1,
            longitude_value_1,
            latitude_direction_2,
            latitude_value_2,
            longitude_direction_2,
            longitude_value_2,
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
        self.show_success_message()
        self.destroy()

    def show_success_message(self):
        messagebox.showinfo("Upravene", "Nehnuteľnosť bola úspešne upravená.")

    def show_alert(self, message):
        messagebox.showerror("Chyba", message)
class ParcelSearch(ctk.CTkFrame):
    def __init__(self, parent, controller, app):
        super().__init__(parent)
        self.controller = controller
        self.app = app

        # Latitude Direction
        latitude_direction_label = ctk.CTkLabel(self, text="Zemepisna sirka:")
        latitude_direction_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var = ctk.StringVar()
        latitude_north_checkbox = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var, value='North')
        latitude_north_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var, value='South')
        latitude_south_checkbox.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Latitude Value
        latitude_value_label = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky:")
        latitude_value_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry = ctk.CTkEntry(self)
        self.latitude_value_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Longitude Direction
        longitude_direction_label = ctk.CTkLabel(self, text="Zemepisna dlzka:")
        longitude_direction_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var = ctk.StringVar()
        longitude_east_checkbox = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var, value='East')
        longitude_east_checkbox.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var, value='West')
        longitude_west_checkbox.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        # Longitude Value
        longitude_value_label = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky:")
        longitude_value_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry = ctk.CTkEntry(self)
        self.longitude_value_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Search Button
        search_button = ctk.CTkButton(self, text="Vyhladaj", command=self.search_parcels)
        search_button.grid(row=4, column=0, columnspan=3, pady=20, sticky="w", padx=100)

        # Results Container
        self.results_frame = ctk.CTkFrame(self, width=600, height=300)
        self.results_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
    
    def search_parcels(self):
        latitude_direction = self.latitude_direction_var.get()
        latitude_value = self.latitude_value_entry.get().strip()
        longitude_direction = self.longitude_direction_var.get()
        longitude_value = self.longitude_value_entry.get().strip()

        # Validate the input
        if latitude_direction not in ['North', 'South']:
            self.show_alert("Vyberte smer pre zemepisnu sirku (North/South).")
            return
        if not self.is_valid_number(latitude_value):
            self.show_alert("Hodnota zemepisnej sirky musi byt cislo.")
            return
        if longitude_direction not in ['East', 'West']:
            self.show_alert("Vyberte smer pre zemepisnu dlzku (East/West).")
            return
        if not self.is_valid_number(longitude_value):
            self.show_alert("Hodnota zemepisnej dlzky musi byt cislo.")
            return

        # Convert directions to single letters
        latitude_direction = latitude_direction[0]  # "North" -> "N", "South" -> "S"
        longitude_direction = longitude_direction[0]  # "East" -> "E", "West" -> "W"
        gps_pos = Gps(latitude_direction, float(latitude_value), longitude_direction, float(longitude_value))
        
        results = self.app.search_parcels_by_gps(gps_pos)
        self.display_results(results)
    
    def display_results(self, results):
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        if not results:
            no_results_label = ctk.CTkLabel(self.results_frame, text="No parcels found.")
            no_results_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
            return

        for idx, parcel in enumerate(results):
            parcel_label = ctk.CTkLabel(self.results_frame, text=str(parcel))
            parcel_label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

            edit_button = ctk.CTkButton(self.results_frame, text="Edit", command=lambda p=parcel: self.edit_parcel(p))
            edit_button.grid(row=idx, column=1, padx=5, pady=5)

            delete_button = ctk.CTkButton(self.results_frame, text="Delete", command=lambda p=parcel: self.delete_parcel(p))
            delete_button.grid(row=idx, column=2, padx=5, pady=5)

    def edit_parcel(self, parcel):
        # Implement logic to edit the parcel
        pass

    def delete_parcel(self, parcel):
        if messagebox.askyesno("Potvrdenie vymazania", "Naozaj chcete vymazat tuto parcelu?"):
            self.app.delete_parcel(parcel)
    
    def show_alert(self, message):
        messagebox.showerror("Chyba", message)
    
    def is_valid_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False



# Property Search Frame
class PropertySearch(ctk.CTkFrame):
    def __init__(self, parent, controller, app):
        super().__init__(parent)
        self.controller = controller
        self.app = app

        # Latitude Direction
        latitude_direction_label = ctk.CTkLabel(self, text="Zemepisna sirka:")
        latitude_direction_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var = ctk.StringVar()
        latitude_north_checkbox = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var, value='North')
        latitude_north_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var, value='South')
        latitude_south_checkbox.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Latitude Value
        latitude_value_label = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky:")
        latitude_value_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry = ctk.CTkEntry(self)
        self.latitude_value_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Longitude Direction
        longitude_direction_label = ctk.CTkLabel(self, text="Zemepisna dlzka:")
        longitude_direction_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var = ctk.StringVar()
        longitude_east_checkbox = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var, value='East')
        longitude_east_checkbox.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var, value='West')
        longitude_west_checkbox.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        # Longitude Value
        longitude_value_label = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky:")
        longitude_value_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry = ctk.CTkEntry(self)
        self.longitude_value_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Search Button
        search_button = ctk.CTkButton(self, text="Vyhladaj", command=self.search_properties)
        search_button.grid(row=4, column=0, columnspan=3, pady=20, sticky="w", padx=100)

       
        # Results Container
        self.results_frame = ctk.CTkFrame(self, width=600, height=800)
        self.results_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        
    def search_properties(self):
       
        latitude_direction = self.latitude_direction_var.get()
        latitude_value = self.latitude_value_entry.get().strip()
        longitude_direction = self.longitude_direction_var.get()
        longitude_value = self.longitude_value_entry.get().strip()

        # Validate the input
        if latitude_direction not in ['North', 'South']:
            self.show_alert("Vyberte smer pre zemepisnu sirku (North/South).")
            return
        if not self.is_valid_number(latitude_value):
            self.show_alert("Hodnota zemepisnej sirky musi byt cislo.")
            return
        if longitude_direction not in ['East', 'West']:
            self.show_alert("Vyberte smer pre zemepisnu dlzku (East/West).")
            return
        if not self.is_valid_number(longitude_value):
            self.show_alert("Hodnota zemepisnej dlzky musi byt cislo.")
            return

        # Convert directions to single letters
        latitude_direction = latitude_direction[0]  # "North" -> "N", "South" -> "S"
        longitude_direction = longitude_direction[0]  # "East" -> "E", "West" -> "W"
        gps_pos = Gps(latitude_direction, float(latitude_value), longitude_direction, float(longitude_value))
        
        results = self.app.search_properties_by_gps(gps_pos)

        
        self.display_results(results)
    def display_results(self, results):
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        if not results:
            no_results_label = ctk.CTkLabel(self.results_frame, text="No properties found.")
            no_results_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
            return

        for idx, property in enumerate(results):
            property_label = ctk.CTkLabel(self.results_frame, text=str(property))
            property_label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

            edit_button = ctk.CTkButton(self.results_frame, text="Edit", command=lambda p=property: self.edit_property(p))
            edit_button.grid(row=idx, column=1, padx=5, pady=5)

            delete_button = ctk.CTkButton(self.results_frame, text="Delete", command=lambda p=property: self.delete_property(p))
            delete_button.grid(row=idx, column=2, padx=5, pady=5)

    def edit_property(self, property):
        PropertyUpdate(self, self.controller, self.app, property)
        

    def delete_property(self, property):
        #threading.Thread(target=self.delete_property, args=(property,)).start()
        if messagebox.askyesno("Potvrdenie vymazania", "Naozaj chcete vymazat tuto nehnutelnost?"):
            self.app.delete_property(property)

    def show_alert(self, message):
        
        messagebox.showerror("Chyba", message)

    def is_valid_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    
class ParcelSearch(ctk.CTkFrame):
    def __init__(self, parent, controller, app):
        super().__init__(parent)
        self.controller = controller
        self.app = app

        # Latitude Direction
        latitude_direction_label = ctk.CTkLabel(self, text="Zemepisna sirka:")
        latitude_direction_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var = ctk.StringVar()
        latitude_north_checkbox = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var, value='North')
        latitude_north_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var, value='South')
        latitude_south_checkbox.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Latitude Value
        latitude_value_label = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky:")
        latitude_value_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry = ctk.CTkEntry(self)
        self.latitude_value_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Longitude Direction
        longitude_direction_label = ctk.CTkLabel(self, text="Zemepisna dlzka:")
        longitude_direction_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var = ctk.StringVar()
        longitude_east_checkbox = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var, value='East')
        longitude_east_checkbox.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var, value='West')
        longitude_west_checkbox.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        # Longitude Value
        longitude_value_label = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky:")
        longitude_value_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry = ctk.CTkEntry(self)
        self.longitude_value_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Search Button
        search_button = ctk.CTkButton(self, text="Vyhladaj", command=self.search_parcels)
        search_button.grid(row=4, column=0, columnspan=3, pady=20, sticky="w", padx=100)

        # Results Container
        self.results_frame = ctk.CTkFrame(self, width=600, height=300)
        self.results_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
    
    def search_parcels(self):
        latitude_direction = self.latitude_direction_var.get()
        latitude_value = self.latitude_value_entry.get().strip()
        longitude_direction = self.longitude_direction_var.get()
        longitude_value = self.longitude_value_entry.get().strip()

        # Validate the input
        if latitude_direction not in ['North', 'South']:
            self.show_alert("Vyberte smer pre zemepisnu sirku (North/South).")
            return
        if not self.is_valid_number(latitude_value):
            self.show_alert("Hodnota zemepisnej sirky musi byt cislo.")
            return
        if longitude_direction not in ['East', 'West']:
            self.show_alert("Vyberte smer pre zemepisnu dlzku (East/West).")
            return
        if not self.is_valid_number(longitude_value):
            self.show_alert("Hodnota zemepisnej dlzky musi byt cislo.")
            return

        # Convert directions to single letters
        latitude_direction = latitude_direction[0]  # "North" -> "N", "South" -> "S"
        longitude_direction = longitude_direction[0]  # "East" -> "E", "West" -> "W"
        gps_pos = Gps(latitude_direction, float(latitude_value), longitude_direction, float(longitude_value))
        
        results = self.app.search_parcels_by_gps(gps_pos)
        self.display_results(results)
    
    def display_results(self, results):
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        if not results:
            no_results_label = ctk.CTkLabel(self.results_frame, text="No parcels found.")
            no_results_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
            return

        for idx, parcel in enumerate(results):
            parcel_label = ctk.CTkLabel(self.results_frame, text=str(parcel))
            parcel_label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

            edit_button = ctk.CTkButton(self.results_frame, text="Edit", command=lambda p=parcel: self.edit_parcel(p))
            edit_button.grid(row=idx, column=1, padx=5, pady=5)

            delete_button = ctk.CTkButton(self.results_frame, text="Delete", command=lambda p=parcel: self.delete_parcel(p))
            delete_button.grid(row=idx, column=2, padx=5, pady=5)

    def edit_parcel(self, parcel):
        # Implement logic to edit the parcel
        pass

    def delete_parcel(self, parcel):
        if messagebox.askyesno("Potvrdenie vymazania", "Naozaj chcete vymazat tuto parcelu?"):
            self.app.delete_parcel(parcel)
    
    def show_alert(self, message):
        messagebox.showerror("Chyba", message)
    
    def is_valid_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False


# Search All Frame
class SearchAll(ctk.CTkFrame):
    def __init__(self, parent, controller, app):
        super().__init__(parent)
        self.controller = controller
        self.app = app
        label = ctk.CTkLabel(self, text="Nehnutelnosti a Parcely", font=("Arial", 20))
        label.grid(row=0, column=0, columnspan=4, pady=20, sticky="w")

        # First GPS Coordinates
        latitude_direction_label_1 = ctk.CTkLabel(self, text="Zemepisna sirka 1:")
        latitude_direction_label_1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var_1 = ctk.StringVar()
        latitude_north_checkbox_1 = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var_1, value='North')
        latitude_north_checkbox_1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox_1 = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var_1, value='South')
        latitude_south_checkbox_1.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        latitude_value_label_1 = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky 1:")
        latitude_value_label_1.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry_1 = ctk.CTkEntry(self)
        self.latitude_value_entry_1.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        longitude_direction_label_1 = ctk.CTkLabel(self, text="Zemepisna dlzka 1:")
        longitude_direction_label_1.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var_1 = ctk.StringVar()
        longitude_east_checkbox_1 = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var_1, value='East')
        longitude_east_checkbox_1.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox_1 = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var_1, value='West')
        longitude_west_checkbox_1.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        longitude_value_label_1 = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky 1:")
        longitude_value_label_1.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry_1 = ctk.CTkEntry(self)
        self.longitude_value_entry_1.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Second GPS Coordinates
        latitude_direction_label_2 = ctk.CTkLabel(self, text="Zemepisna sirka 2:")
        latitude_direction_label_2.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.latitude_direction_var_2 = ctk.StringVar()
        latitude_north_checkbox_2 = ctk.CTkRadioButton(self, text="North", variable=self.latitude_direction_var_2, value='North')
        latitude_north_checkbox_2.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        latitude_south_checkbox_2 = ctk.CTkRadioButton(self, text="South", variable=self.latitude_direction_var_2, value='South')
        latitude_south_checkbox_2.grid(row=5, column=2, padx=5, pady=5, sticky="w")

        latitude_value_label_2 = ctk.CTkLabel(self, text="Hodnota zemepisnej sirky 2:")
        latitude_value_label_2.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.latitude_value_entry_2 = ctk.CTkEntry(self)
        self.latitude_value_entry_2.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        longitude_direction_label_2 = ctk.CTkLabel(self, text="Zemepisna dlzka 2:")
        longitude_direction_label_2.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.longitude_direction_var_2 = ctk.StringVar()
        longitude_east_checkbox_2 = ctk.CTkRadioButton(self, text="East", variable=self.longitude_direction_var_2, value='East')
        longitude_east_checkbox_2.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        longitude_west_checkbox_2 = ctk.CTkRadioButton(self, text="West", variable=self.longitude_direction_var_2, value='West')
        longitude_west_checkbox_2.grid(row=7, column=2, padx=5, pady=5, sticky="w")

        longitude_value_label_2 = ctk.CTkLabel(self, text="Hodnota zemepisnej dlzky 2:")
        longitude_value_label_2.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.longitude_value_entry_2 = ctk.CTkEntry(self)
        self.longitude_value_entry_2.grid(row=8, column=1, padx=10, pady=5, sticky="w")

      
        search_button = ctk.CTkButton(self, text="Hladaj", command=self.search_all_properties)
        search_button.grid(row=9, column=0, columnspan=3, pady=20, sticky="ew", padx=10)

        
        results_label = ctk.CTkLabel(self, text="Vysledky vyhladavania:")
        results_label.grid(row=10, column=0, columnspan=4, pady=10, sticky="w")
        
        self.results_textbox = ctk.CTkTextbox(self, width=600, height=200)
        self.results_textbox.configure(state="disabled")
        self.results_textbox.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

    def search_all_properties(self):
        # Retrieve values from input fields for the first GPS
        latitude_direction_1 = self.latitude_direction_var_1.get()
        latitude_value_1 = self.latitude_value_entry_1.get().strip()
        longitude_direction_1 = self.longitude_direction_var_1.get()
        longitude_value_1 = self.longitude_value_entry_1.get().strip()

        # Retrieve values from input fields for the second GPS
        latitude_direction_2 = self.latitude_direction_var_2.get()
        latitude_value_2 = self.latitude_value_entry_2.get().strip()
        longitude_direction_2 = self.longitude_direction_var_2.get()
        longitude_value_2 = self.longitude_value_entry_2.get().strip()

        # Validate the input for both GPS points
        if latitude_direction_1 not in ['North', 'South']:
            self.show_alert("Vyberte smer pre prvu zemepisnu sirku (North/South).")
            return
        if not self.is_valid_number(latitude_value_1):
            self.show_alert("Hodnota prvej zemepisnej sirky musi byt cislo.")
            return
        if longitude_direction_1 not in ['East', 'West']:
            self.show_alert("Vyberte smer pre prvu zemepisnu dlzku (East/West).")
            return
        if not self.is_valid_number(longitude_value_1):
            self.show_alert("Hodnota prvej zemepisnej dlzky musi byt cislo.")
            return

        if latitude_direction_2 not in ['North', 'South']:
            self.show_alert("Vyberte smer pre druhu zemepisnu sirku (North/South).")
            return
        if not self.is_valid_number(latitude_value_2):
            self.show_alert("Hodnota druhej zemepisnej sirky musi byt cislo.")
            return
        if longitude_direction_2 not in ['East', 'West']:
            self.show_alert("Vyberte smer pre druhu zemepisnu dlzku (East/West).")
            return
        if not self.is_valid_number(longitude_value_2):
            self.show_alert("Hodnota druhej zemepisnej dlzky musi byt cislo.")
            return

        # Convert directions to single letters
        latitude_direction_1 = latitude_direction_1[0]  # "North" -> "N", "South" -> "S"
        longitude_direction_1 = longitude_direction_1[0]  # "East" -> "E", "West" -> "W"
        latitude_direction_2 = latitude_direction_2[0]  # "North" -> "N", "South" -> "S"
        longitude_direction_2 = longitude_direction_2[0]  # "East" -> "E", "West" -> "W"

       
        gps_1 = Gps(latitude_direction_1, float(latitude_value_1), longitude_direction_1, float(longitude_value_1))
        gps_2 = Gps(latitude_direction_2, float(latitude_value_2), longitude_direction_2, float(longitude_value_2))

      
        results = self.app.search_all_by_gps(gps_1, gps_2)

        
        self.display_results(results)

    def display_results(self, results):
        
        self.results_textbox.configure(state="normal")
        self.results_textbox.delete("1.0", "end")
        if not results:
            self.results_textbox.insert("1.0", "No properties or parcels found.\n")
            return   
        for property in results:
            self.results_textbox.insert("end", f"{property}\n")
        self.results_textbox.configure(state="disabled")

    def show_alert(self, message):
        
        messagebox.showerror("Chyba", message)

    def is_valid_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
# Tester Frame
class Tester(ctk.CTkFrame):
    def __init__(self, parent, controller, app):
        super().__init__(parent)
        self.controller = controller
        self.app = app
        label = ctk.CTkLabel(self, text="Tester", font=("Arial", 20))
        label.grid(row=0, column=0, columnspan=3, pady=20, sticky="w")

              
        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")
        add_label = ctk.CTkLabel(self.action_frame, text="Otestuj pridavanie", font=("Arial", 16))
        add_label.pack(pady=10)
        operations_label = ctk.CTkLabel(self.action_frame, text="Pocet operacii na generovanie:")
        operations_label.pack(pady=5)
        operations_entry = ctk.CTkEntry(self.action_frame)
        operations_entry.pack(pady=5)
        overlap_label = ctk.CTkLabel(self.action_frame, text="Percento prekryvu:")
        overlap_label.pack(pady=5)
        overlap_entry = ctk.CTkEntry(self.action_frame)
        overlap_entry.pack(pady=5)
        add_button = ctk.CTkButton(self.action_frame, text="Pridat", \
            command=lambda: self.test_add(int(operations_entry.get()), int(overlap_entry.get())))
        add_button.pack(pady=10)

        console_label = ctk.CTkLabel(self.action_frame, text="Konzola na vypis vysledkov:")
        console_label.pack(pady=10)
        self.console_text = ctk.CTkTextbox(self.action_frame, width=500, height=300)
        self.console_text.configure(state='disabled')
        self.console_text.pack(pady=10) 
    def test_add(self, operations, overlap):
    
        results = self.app.test_add(operations, overlap)
        self.display_results(results)
    def display_results(self, results):
        self.console_text.configure(state='normal')
        self.console_text.delete("1.0", "end")
        self.console_text.insert("1.0", results)
        self.console_text.configure(state='disabled')