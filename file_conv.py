def import_SWV():
    # file = open(f'{cwd}/test_data/{csvname}.csv', 'r')
    # test_data_file = csv.reader(file, delimiter=",")
    # for row in test_data_file:
    #     rows.append(row)
    # file.close()
    # return rows
    data = [] # receive from GUI code or local computer
    return data

def export_data(data):
    x = "CSV" # this will receive input from GUI
    if x == "CSV":
        to_csv(data)
    else:
        to_LabChart(data)


def to_csv(data):
    if len(data) == 1:
        print("Convert to csv")
    else:
        for i in len(data):
            print("Convert to csv")
    return


def to_LabChart(data):
    if len(data) == 1:
        print("Export to LabChart")
    else:
        for i in len(data):
            print("Export to LabChart")
    return


if __name__ == '__main__':
    data = import_from_Matlab()
    export_data(data)
