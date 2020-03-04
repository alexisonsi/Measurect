import json
import pytest
import csv
import os
cwd = os.getcwd()


def import_SWV():
    tSWVpairs = []
    file = open(f'{cwd}/test_csv.csv', 'r')
    test_data_file = csv.reader(file, delimiter=",")
    for row in test_data_file:
        tSWVpairs.append(row)
    file.close()
    return tSWVpairs
    return tSWVpairs


def export_data(data):
    x = "CSV"  # this will receive input from GUI
    if x == "CSV":
        to_csv(data)
    else:
        to_LabChart(data)


def to_csv(data):
    if data == 1:
        print("Convert to csv")
    else:
        for i in data:
            print("Convert to csv")
    return


def to_LabChart(data):
    if data == 1:
        print("Export to LabChart")
    else:
        for i in data:
            print("Export to LabChart")
    return


if __name__ == '__main__':
    data = import_SWV()
    export_data(data)
