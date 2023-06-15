import csv

def get_data(path):
    data = []
    with open(path, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return data[1::]
