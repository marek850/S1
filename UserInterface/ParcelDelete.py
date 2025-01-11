from UserInterface.Command import Command


class ParcelDelete(Command):
    
    def __init__(self, app=None, parcel = None):
        self.app = app
        self.parcel = parcel

    def execute(self):
        self.app.delete_parcel(self.parcel)