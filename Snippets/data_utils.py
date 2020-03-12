import os
import csv

#def create_file():

def demo_csv_writer(filename):
    data = [[1,2],[3,4],["a", "b"]]
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerows(data)
        csvfile.close()

def demo_csv_reader(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        data = [row for row in reader]
        print(data)
        csvfile.close()

if __name__ == "__main__":
    filename = 'sample.csv'
    #demo_csv_writer(filename)
    demo_csv_reader(filename)
