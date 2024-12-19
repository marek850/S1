class FileHandler:
    def __init__(self, filename, app, strategy):
        
        self.__filename = filename
        self.__app = app
        self.__strategy = strategy  

    def save_to_file(self, data):
        """Save data using the provided strategy."""
        self.__strategy.save(self.__filename, data)

    def load_from_file(self):
        """Load data using the provided strategy."""
        self.__strategy.load(self.__filename, self.__app)