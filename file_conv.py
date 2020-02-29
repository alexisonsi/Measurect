def main():
    x = "CSV" # this will receive input from GUI
    data = [] # receive from GUI code or local computer
    if x == "CSV":
        to_csv(data)
    else:
        to_LabChart(data)


def to_csv(data):
    print("Convert to csv")


def to_LabChart(data):
    print("Access LabChart")


if __name__ == '__main__':
    main()
