from interactive import Interactive
from input import File

if __name__ == "__main__":

    print("interactive or file")
    interaction = input("write interactive or file to choose from them :")
    print()
    manual = Interactive()
    auto = File()

    if interaction == "interactive":
        cnt = 0
        while cnt < 2:
            if cnt == 0:
                manual.Create_Parking()
                cnt += 1
            else:
                manual.Activities()
                cnt += 1
    elif interaction == "file":
        print("file input_instructions.txt")
        file_address = input("file location please :")
        f = open(file_address, "r")
        cnt = 0
        for row in f:
            if cnt == 0:
                auto.Create_Parking(row)
                cnt += 1
            else:
                auto.Activities(row)
    else:
        print("Please give a correct input sir/mam")