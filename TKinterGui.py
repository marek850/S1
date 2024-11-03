import tkinter as tk
from tkinter import ttk
from GeoApp import GeoApp
from Locations.GpsPosition import GPSPosition as Gps
class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200")
        self.root.title("S1 - Menu")
        self.geo_app = GeoApp()

        # Menu setup
        menu = tk.Menu(self.root)
        insert = tk.Menu(menu, tearoff=0)
        insert.add_command(label="Nová nehnuteľnosť", command=self.open_new_property_form)
        menu.add_cascade(label="Pridaj", menu=insert)
        find = tk.Menu(menu, tearoff=0)
        find.add_command(label="Vyhľadať nehnuteľnosť", command=self.open_search_property_form)
        menu.add_cascade(label="Najdi", menu=insert)
        self.root.config(menu=menu)

    def open_new_property_form(self):
        new_window = tk.Toplevel(self.root)
        PropertyForm(new_window, self.geo_app)

    def open_search_property_form(self):
        new_window = tk.Toplevel(self.root)
        PropertySearchForm(new_window, self.geo_app)


class PropertyForm:
    def __init__(self, root, geo_app):
        self.geo_app = geo_app
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Nová nehnuteľnosť")

        # Main frame where form widgets will be displayed
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill="both", expand=True)

        # Create new instances of StringVar each time to avoid conflicts
        self.supisne_cislo = ttk.Entry(self.main_frame)
        self.popis = ttk.Entry(self.main_frame)
        self.sirka_1_value = tk.StringVar()
        self.hodnota_sirka_1 = ttk.Entry(self.main_frame)
        self.dlzka_1_value = tk.StringVar()
        self.hodnota_dlzka_1 = ttk.Entry(self.main_frame)
        self.sirka_2_value = tk.StringVar()
        self.hodnota_sirka_2 = ttk.Entry(self.main_frame)
        self.dlzka_2_value = tk.StringVar()
        self.hodnota_dlzka_2 = ttk.Entry(self.main_frame)

        ttk.Label(self.main_frame, text="Súpisné číslo:").grid(row=0, column=0, sticky='w', pady=5)
        self.supisne_cislo.grid(row=0, column=1, columnspan=3, sticky='we', pady=5)

        ttk.Label(self.main_frame, text="Popis:").grid(row=1, column=0, sticky='w', pady=5)
        self.popis.grid(row=1, column=1, columnspan=3, sticky='we', pady=5)

        # Zemepisná šírka 1
        ttk.Label(self.main_frame, text="Zemepisná šírka 1:").grid(row=2, column=0, sticky='w', pady=5)
        ttk.Radiobutton(self.main_frame, text="North", variable=self.sirka_1_value, value="N").grid(row=2, column=1, sticky='w')
        ttk.Radiobutton(self.main_frame, text="South", variable=self.sirka_1_value, value="S").grid(row=2, column=2, sticky='w')

        ttk.Label(self.main_frame, text="Hodnota zemepisnej šírky 1:").grid(row=3, column=0, sticky='w', pady=5)
        self.hodnota_sirka_1.grid(row=3, column=1, columnspan=3, sticky='we', pady=5)

        # Zemepisná dĺžka 1
        ttk.Label(self.main_frame, text="Zemepisná dĺžka 1:").grid(row=4, column=0, sticky='w', pady=5)
        ttk.Radiobutton(self.main_frame, text="East", variable=self.dlzka_1_value, value="E").grid(row=4, column=1, sticky='w')
        ttk.Radiobutton(self.main_frame, text="West", variable=self.dlzka_1_value, value="W").grid(row=4, column=2, sticky='w')

        ttk.Label(self.main_frame, text="Hodnota zemepisnej dĺžky 1:").grid(row=5, column=0, sticky='w', pady=5)
        self.hodnota_dlzka_1.grid(row=5, column=1, columnspan=3, sticky='we', pady=5)

        # Zemepisná šírka 2
        ttk.Label(self.main_frame, text="Zemepisná šírka 2:").grid(row=6, column=0, sticky='w', pady=5)
        ttk.Radiobutton(self.main_frame, text="North", variable=self.sirka_2_value, value="N").grid(row=6, column=1, sticky='w')
        ttk.Radiobutton(self.main_frame, text="South", variable=self.sirka_2_value, value="S").grid(row=6, column=2, sticky='w')

        ttk.Label(self.main_frame, text="Hodnota zemepisnej šírky 2:").grid(row=7, column=0, sticky='w', pady=5)
        self.hodnota_sirka_2.grid(row=7, column=1, columnspan=3, sticky='we', pady=5)

        # Zemepisná dĺžka 2
        ttk.Label(self.main_frame, text="Zemepisná dĺžka 2:").grid(row=8, column=0, sticky='w', pady=5)
        ttk.Radiobutton(self.main_frame, text="East", variable=self.dlzka_2_value, value="E").grid(row=8, column=1, sticky='w')
        ttk.Radiobutton(self.main_frame, text="West", variable=self.dlzka_2_value, value="W").grid(row=8, column=2, sticky='w')

        ttk.Label(self.main_frame, text="Hodnota zemepisnej dĺžky 2:").grid(row=9, column=0, sticky='w', pady=5)
        self.hodnota_dlzka_2.grid(row=9, column=1, columnspan=3, sticky='we', pady=5)

        # Add button to submit the form
        ttk.Button(self.main_frame, text="Pridať", command=self.submit_form).grid(row=10, column=1, columnspan=2, pady=20)

    def submit_form(self):
        # Close the form window after submission
        
        # Retrieve values from the form
        supisne_cislo_value = int(self.supisne_cislo.get())
        popis_value = self.popis.get()
        sirka_1 = self.sirka_1_value.get()
        hodnota_sirka_1_value = float(self.hodnota_sirka_1.get())
        dlzka_1 = self.dlzka_1_value.get()
        hodnota_dlzka_1_value = float(self.hodnota_dlzka_1.get())
        sirka_2 = self.sirka_2_value.get()
        hodnota_sirka_2_value = float(self.hodnota_sirka_2.get())
        dlzka_2 = self.dlzka_2_value.get()
        hodnota_dlzka_2_value = float(self.hodnota_dlzka_2.get())
        
        # Call the add_property method from GeoApp
        self.geo_app.add_property(supisne_cislo_value, popis_value, sirka_1, hodnota_sirka_1_value, dlzka_1, hodnota_dlzka_1_value, sirka_2, hodnota_sirka_2_value, dlzka_2, hodnota_dlzka_2_value)
        self.root.destroy()

class PropertySearchForm:
    def __init__(self, root, geo_app):
        self.geo_app = geo_app
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Vyhľadať nehnuteľnosť")

        # Main frame where form widgets will be displayed
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill="both", expand=True)

        # Create new instances of StringVar each time to avoid conflicts
        self.sirka_value = tk.StringVar()
        self.hodnota_sirka = ttk.Entry(self.main_frame)
        self.dlzka_value = tk.StringVar()
        self.hodnota_dlzka = ttk.Entry(self.main_frame)

        # Zemepisná šírka
        ttk.Label(self.main_frame, text="Zemepisná šírka:").grid(row=0, column=0, sticky='w', pady=5)
        ttk.Radiobutton(self.main_frame, text="North", variable=self.sirka_value, value="N").grid(row=0, column=1, sticky='w')
        ttk.Radiobutton(self.main_frame, text="South", variable=self.sirka_value, value="S").grid(row=0, column=2, sticky='w')

        ttk.Label(self.main_frame, text="Hodnota zemepisnej šírky:").grid(row=1, column=0, sticky='w', pady=5)
        self.hodnota_sirka.grid(row=1, column=1, columnspan=3, sticky='we', pady=5)

        # Zemepisná dĺžka
        ttk.Label(self.main_frame, text="Zemepisná dĺžka:").grid(row=2, column=0, sticky='w', pady=5)
        ttk.Radiobutton(self.main_frame, text="East", variable=self.dlzka_value, value="E").grid(row=2, column=1, sticky='w')
        ttk.Radiobutton(self.main_frame, text="West", variable=self.dlzka_value, value="W").grid(row=2, column=2, sticky='w')

        ttk.Label(self.main_frame, text="Hodnota zemepisnej dĺžky:").grid(row=3, column=0, sticky='w', pady=5)
        self.hodnota_dlzka.grid(row=3, column=1, columnspan=3, sticky='we', pady=5)

        # Add button to search
        ttk.Button(self.main_frame, text="Vyhľadať", command=self.submit_search).grid(row=4, column=1, columnspan=2, pady=20)

        # Results display
        self.results_textbox = tk.Text(self.main_frame, width=80, height=10, state='disabled')
        self.results_textbox.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    def submit_search(self):
        # Retrieve values from the form
        sirka = self.sirka_value.get()
        hodnota_sirka_value = float(self.hodnota_sirka.get())
        dlzka = self.dlzka_value.get()
        hodnota_dlzka_value = float(self.hodnota_dlzka.get())
        gps_pos = Gps(sirka, float(hodnota_sirka_value), dlzka, float(hodnota_dlzka_value))
        # Call the search_property method from GeoApp and display results
        results = self.geo_app.search_properties_by_gps(gps_pos)

        self.results_textbox.config(state='normal')
        self.results_textbox.delete(1.0, 'end')
        if not results:
            self.results_textbox.insert('end', 'No properties found.')
        else:
            for property in results:
                self.results_textbox.insert('end', f'{property}')
        self.results_textbox.config(state='disabled')
        


# Main window setup
root = tk.Tk()
menu_app = MenuApp(root)
root.mainloop()
