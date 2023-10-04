import csv

class CSVORM:
    def __init__(self, filename):
        self.filename = filename
        self.fieldnames = []
        self.data = []
        with open(filename, "r") as f:
            reader = csv.reader(f)
            self.fieldnames = next(reader)
            for row in reader:
                self.data.append(dict(zip(self.fieldnames, row)))

    def list(self):
        return self.data

    def get(self, id):
        for row in self.data:
            if row["ID"] == id:
                return row
        return None

    def filter(self, column_name, value):
        filtered_data = []
        for row in self.data:
            if row[column_name] == value:
                filtered_data.append(row)
        return filtered_data

orm = CSVORM("Python/CSVORM.csv")

rows = orm.list()
print("All rows:")
for row in rows:
    print(row)
print('\n')

row = orm.get(2)
print(row,"\n")

print("Filtered Data:")
filtered_data = orm.filter("Name", "Alice")
for row in filtered_data:
        print(row)