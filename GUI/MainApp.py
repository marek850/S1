from tkinter import messagebox
import customtkinter as ctk
from Locations.GpsPosition import GPSPosition as Gps
class MainApp(ctk.CTk):
    def __init__(self, app):
        super().__init__()
        self.title("Magula S1")
        self.geometry("800x600")
        self.app = app

        # Configure the grid layout of the main window
        self.grid_columnconfigure(0, weight=1)  # Allow the first column (menu) to adjust its size
        self.grid_columnconfigure(1, weight=4)  # Allow the second column (container) to adjust more
        self.grid_rowconfigure(0, weight=1)     # Allow the single row to adjust its size

        # Create a menu frame
        self.menu_frame = MenuFrame(self, self.show_frame, self.app)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        # Create container for the frames
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew")
        
        # Configure container to allow the frames to fill the entire space
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        # Initialize frames
        self.frames = {}
        for F in (PropertyInsert, PropertySearch, SearchAll, Tester):
            frame = F(parent=self.container, controller=self, app=self.app)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        self.show_frame(PropertyInsert)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback, app):
        super().__init__(parent)
        self.app = app
        self.show_frame_callback = show_frame_callback

        # Set up the layout to occupy the entire available space
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add buttons for navigation
        insert_button = ctk.CTkButton(self, text="Pridat Nehnutelnost", command=lambda: self.show_frame_callback(PropertyInsert))
        insert_button.pack(pady=10, padx=10)

        search_button = ctk.CTkButton(self, text="Nehnutelnosti", command=lambda: self.show_frame_callback(PropertySearch))
        search_button.pack(pady=10, padx=10)

        search_all_button = ctk.CTkButton(self, text="Nehnutelnosti a Parcely", command=lambda: self.show_frame_callback(SearchAll))
        search_all_button.pack(pady=10, padx=10)

        tester_button = ctk.CTkButton(self, text="Tester", command=lambda: self.show_frame_callback(Tester))
        tester_button.pack(pady=10, padx=10)

# Property Insert Frame
class PropertyInsert(ctk.CTkFrame):
    def __init__(self, parent, controller, app):
        super().__init__(parent)
        self.controller = controller
        self.app = app

        # Add widgets to create a form for adding a new property
        label = ctk.CTkLabel(self, text="Pridanie Nehnutelnosti", font=("Arial", 20))
        label.grid(row=0, column=0, columnspan=4, pady=20, sticky="w")

        # Property Number
        property_number_label = ctk.CTkLabel(self, text="Supisne cislo:")
        property_number_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.property_number_entry = ctk.CTkEntry(self)
        self.property_number_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Description
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

        # Add Property Button
        add_property_button = ctk.CTkButton(self, text="Pridat", command=self.add_property)
        add_property_button.grid(row=11, column=0, columnspan=3, pady=20, sticky="w", padx=100)

    def add_property(self):
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
        self.clear_form()
        self.show_success_message()
        
    def show_success_message(self):
        messagebox.showinfo("Pridane", "Nehnuteľnosť bola úspešne pridaná.")
    def show_alert(self, message):
        # Show alert box with the provided message
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

        # Text box for displaying results
        self.results_textbox = ctk.CTkTextbox(self, width=600, height=200)
        self.results_textbox.configure(state="disabled")
        self.results_textbox.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        
    def search_properties(self):
        # Retrieve values from input fields
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
        # Call the search method in the app with the collected values
        results = self.app.search_properties_by_gps(gps_pos)

        # Display the results in the textbox
        self.display_results(results)

    def display_results(self, results):
        # Clear the previous results
        self.results_textbox.configure(state="normal")
        self.results_textbox.delete("1.0", "end")
        if not results:
            self.results_textbox.insert("1.0", "No properties found.\n")
            return
        
        # Insert each result into the textbox
        for property in results:
            self.results_textbox.insert("end", f"{property}\n")
        self.results_textbox.configure(state="disabled")

    def show_alert(self, message):
        # Show alert box with the provided message
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

        # Search Button
        search_button = ctk.CTkButton(self, text="Hladaj", command=self.search_all_properties)
        search_button.grid(row=9, column=0, columnspan=3, pady=20, sticky="ew", padx=10)

        # Scrollable Box for Results
        results_label = ctk.CTkLabel(self, text="Vysledky vyhladavania:")
        results_label.grid(row=10, column=0, columnspan=4, pady=10, sticky="w")
        # Text box for displaying results
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

        # Create GPS objects or pass directly to the search method
        gps_1 = Gps(latitude_direction_1, float(latitude_value_1), longitude_direction_1, float(longitude_value_1))
        gps_2 = Gps(latitude_direction_2, float(latitude_value_2), longitude_direction_2, float(longitude_value_2))

        # Call the search method in the app with the collected values
        results = self.app.search_all_by_gps(gps_1, gps_2)

        # Display the results in the scrollable frame
        self.display_results(results)

    def display_results(self, results):
        # Clear the previous results
        self.results_textbox.configure(state="normal")
        self.results_textbox.delete("1.0", "end")
        if not results:
            self.results_textbox.insert("1.0", "No properties or parcels found.\n")
            return
        
        # Insert each result into the textbox
        for property in results:
            self.results_textbox.insert("end", f"{property}\n")
        self.results_textbox.configure(state="disabled")

    def show_alert(self, message):
        # Show alert box with the provided message
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

        # Menu for selecting action
        self.selected_option = ctk.StringVar(value='Pridanie')
        action_menu = ctk.CTkOptionMenu(self, variable=self.selected_option, values=['Pridanie', 'Vyhladanie', 'Mazanie'], command=self.update_action_view)
        action_menu.grid(row=1, column=0, columnspan=3, pady=10, padx=10, sticky="w")

        # Frame for displaying action-specific content
        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")
        self.update_action_view('Pridanie')

    def update_action_view(self, selection):
        # Clear the action frame
        for widget in self.action_frame.winfo_children():
            widget.destroy()

        if selection == 'Pridanie':
            # Widgets for adding a property
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
            add_button = ctk.CTkButton(self.action_frame, text="Pridat")
            add_button.pack(pady=10)
        elif selection == 'Vyhladanie':
            # Widgets for searching a property
            search_label = ctk.CTkLabel(self.action_frame, text="Test vyhladavania", font=("Arial", 16))
            search_label.pack(pady=10)
            search_button = ctk.CTkButton(self.action_frame, text="Test Vyhladavania")
            search_button.pack(pady=10)
        elif selection == 'Mazanie':
            # Widgets for deleting a property
            delete_label = ctk.CTkLabel(self.action_frame, text="Test Mazania", font=("Arial", 16))
            delete_label.pack(pady=10)
            delete_button = ctk.CTkButton(self.action_frame, text="Test Mazania")
            delete_button.pack(pady=10)


        # Console for displaying test results
        console_label = ctk.CTkLabel(self.action_frame, text="Konzola na vypis vysledkov:")
        console_label.pack(pady=10)
        console_text = ctk.CTkTextbox(self.action_frame, width=400, height=100)
        console_text.configure(state='disabled')
        console_text.pack(pady=10)
       
        
