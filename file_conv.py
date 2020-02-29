def import_from_Matlab():
    data = [] # receive from GUI code or local computer
    return data

def export_data(data):
    x = "CSV" # this will receive input from GUI
    if x == "CSV":
        to_csv(data)
    else:
        to_LabChart(data)


def to_csv(data):
    print("Convert to csv")


def to_LabChart(data):
    print("Access LabChart")


if __name__ == '__main__':
    data = import_from_Matlab()
    export_data(data)
