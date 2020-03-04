def main():
    raw_input = data_in()
    time = 0
    SWV = raw_to_SWV(time, raw_input)
    rig = SWV_to_rig(time, SWV)
    return rig


def data_in():
    # this is where we get input
    raw_input = 0
    return raw_input


def raw_to_SWV(raw_input):
    SWV = 0
    return SWV


def SWV_to_rig(SWV):
    rho = 1000  # kg/m^3
    rig = 3*rho*(SWV**2)
    # rig = []
    # for i in SWV:
    #     hold = 3*rho*(SWV**2)
    #     rig.append(hold)
    # return time, rig


if __name__ == '__main__':
    main()
