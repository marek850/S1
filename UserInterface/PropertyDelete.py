from UserInterface.Command import Command


class PropertyDelete(Command):
    
    def __init__(self, app=None, property = None):
        self.app = app
        self.property = property

    def execute(self):
        self.app.delete_property(self.property)