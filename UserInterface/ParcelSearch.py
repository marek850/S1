from UserInterface.Command import Command


class ParcelSearch(Command):
    
    def __init__(self, app=None, gps_pos = None):
        self.app = app
        self.gps_pos = gps_pos

    def execute(self):
        return self.app.search_parcels_by_gps(self.gps_pos)