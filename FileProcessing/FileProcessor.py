class FileHandler:
    def __init__(self, filename, app):
        self.__filename = filename
        self.__app = app

    def save_to_file(self, data):
        
        with open(self.__filename, "w") as file:
            for element in data:
                line = element.get_data()  
                file.write(line + "\n")  

    def load_from_file(self):
        
        with open(self.__filename, "r") as file:
            for line in file:
                row = line.strip().split(",") 
                if row[0] == "par":
                    self.__app.add_parcel(row[2], row[3], \
                        row[4], abs(float(row[5])), row[6], abs(float(row[7])), row[8], abs(float(row[9])), \
                            row[10], abs(float(row[11])))
                elif row[0] == "pro":
                    self.__app.add_property(row[2], row[3], \
                        row[4], abs(float(row[5])), row[6], abs(float(row[7])), row[8], abs(float(row[9])), \
                            row[10], abs(float(row[11])))