from tkinter import messagebox
from UserInterface.UserInterface import IUserInterface


class MainAppMediator():
    def __init__(self, app):
        self.app = app  

   
    
    def handle_add_property(self, *args):
        self.app.add_property(*args)
        messagebox.showinfo("Success", "Property added successfully!")

    def handle_add_parcel(self, *args):
        self.app.add_parcel(*args)
        messagebox.showinfo("Success", "Parcel added successfully!")

    def handle_update_property(self, *args):
        self.app.edit_property(*args)
        messagebox.showinfo("Success", "Property updated successfully!")

    def handle_update_parcel(self, *args):
        self.app.edit_parcel(*args)
        messagebox.showinfo("Success", "Parcel updated successfully!")

    def handle_delete_property(self, *args):
        self.app.delete_property(*args)
        messagebox.showinfo("Success", "Property deleted successfully!")

    def handle_delete_parcel(self, *args):
        self.app.delete_parcel(*args)
        messagebox.showinfo("Success", "Parcel deleted successfully!")

    def handle_file_save(self, *args):
        self.app.save_to_file(*args)
        messagebox.showinfo("Success", f"Data saved to file '{args[0]}' successfully!")

    def handle_file_load(self, *args):
        self.app.load_from_file(*args)
        messagebox.showinfo("Success", f"Data loaded from file '{args[0]}' successfully!")

    def handle_search_properties_by_gps(self, *args):
        return self.app.search_properties_by_gps(*args)

    def handle_search_parcels_by_gps(self, *args):
        return self.app.search_parcels_by_gps(*args)

    def handle_search_all_by_gps(self, *args):
        return self.app.search_all_by_gps(*args)

    def handle_test_add(self, *args):
        return self.app.test_add(*args)