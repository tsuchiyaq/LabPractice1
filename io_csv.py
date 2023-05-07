import csv

class IoCsv:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_csv(self):
        with open(self.file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)

    def write_csv(self, data):
        with open(self.file_name, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)