from tkinter import messagebox
from UserInterface.UserInterface import IUserInterface


class MainAppMediator(IUserInterface):
    def __init__(self, app):
        self.app = app  

    def notify(self, event_type: str, *args):
        if event_type == "add_property":
            self.handle_add_property(*args)
        elif event_type == "add_parcel":
            self.handle_add_parcel(*args)
        elif event_type == "update_property":
            self.handle_update_property(*args)
        elif event_type == "update_parcel":
            self.handle_update_parcel(*args)
        elif event_type == "property_delete":
            self.handle_delete_property(*args)
        elif event_type == "parcel_delete":
            self.handle_delete_parcel(*args)
        elif event_type == "save_to_file":
            self.handle_file_save(*args)  
        elif event_type == "load_from_file":
            self.handle_file_load(*args)   
        else:
            print(f"Unknown event type: {event_type}")
    def request(self, event_type: str, *args):
        if event_type == "search_properties":
            return self.handle_search_properties_by_gps(*args)
        elif event_type == "search_parcels":
            return self.handle_search_parcels_by_gps(*args)
        elif event_type == "search_all_properties":
            return self.handle_search_all_by_gps(*args)
        elif event_type == "test_add":
            return self.handle_test_add(*args)
        else:
            print(f"Unknown request: {event_type}")
            return None
    # Methods to forward actions to GeoApp
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