import csv
from FileProcessing.IFileStrategy import IFileStrategy

class CSVFileStrategy(IFileStrategy):
    def save(self, filename, data):
        """Save data to a CSV file."""
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for element in data:
                writer.writerow(element.get_data().split(","))

    def load(self, filename, app):
        """Load data from a CSV file."""
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "par":
                    app.add_parcel(row[2], row[3], 
                        row[4], abs(float(row[5])), row[6], abs(float(row[7])), row[8], abs(float(row[9])),
                        row[10], abs(float(row[11])))
                elif row[0] == "pro":
                    app.add_property(row[2], row[3], 
                        row[4], abs(float(row[5])), row[6], abs(float(row[7])), row[8], abs(float(row[9])),
                        row[10], abs(float(row[11])))