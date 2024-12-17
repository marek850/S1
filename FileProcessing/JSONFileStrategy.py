import json
from FileProcessing.IFileStrategy import IFileStrategy

class JSONFileStrategy(IFileStrategy):
    def save(self, filename, data):
        """Save data to a JSON file."""
        json_data = [element.get_data().split(",") for element in data]
        with open(filename, "w") as file:
            json.dump(json_data, file, indent=4)

    def load(self, filename, app):
        """Load data from a JSON file."""
        with open(filename, "r") as file:
            json_data = json.load(file)
            for row in json_data:
                if row[0] == "par":
                    app.add_parcel(row[2], row[3], 
                        row[4], abs(float(row[5])), row[6], abs(float(row[7])), row[8], abs(float(row[9])),
                        row[10], abs(float(row[11])))
                elif row[0] == "pro":
                    app.add_property(row[2], row[3], 
                        row[4], abs(float(row[5])), row[6], abs(float(row[7])), row[8], abs(float(row[9])),
                        row[10], abs(float(row[11])))
