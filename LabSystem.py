import json
print("***Welcome to AIUB Computer Lab***")

Lab = {1: {'Pc_Name:': "Hp",
           'Operating_System:': 'Windows 10',
           'Status Of the PC:': 'OK'},
       2: {'Pc_Name:': "Dell",
           'Operating_System:': 'Windows 11',
           'Status Of the PC:': 'Problem'}
       }


def AddPc():
    """this function is for Adding new pc"""
    size = int(input("How Many New Pc You Want To Add: "))

    for i in range(size):
        Pc_Id = int(input("Enter the Id Number Of Pc: "))

        if Pc_Id in Lab:
            print("Pc Id Already Exist")
        else:
            Lab[Pc_Id] = {}
            N = input("Enter Name: ")
            Os = input("Enter Operating System: ")
            S = input("Enter Status: ")
            Lab[Pc_Id]["Pc_Name"] = N
            Lab[Pc_Id]["Operating_System:"] = Os
            Lab[Pc_Id]["Status Of the PC:"] = S
            print("*Successfully Added*")


def UpdateInfo():
    Pc_Id = int(input("Enter the Id Number Of Pc: "))

    if Pc_Id in Lab:
        Lab[Pc_Id] = {}
        N = input("Enter Name: ")
        Os = input("Enter Operating System: ")
        S = input("Enter Status: ")
        Lab[Pc_Id]["Pc_Name"] = N
        Lab[Pc_Id]["Operating_System:"] = Os
        Lab[Pc_Id]["Status Of the PC:"] = S
        print("*Successfully Updated*")
    else:
        print("Pc Id Not Found")


def RemovePc():
    """This Function is for Remove a Pc"""
    Pc_Id = int(input("Enter the Id Number Of Pc: "))

    if Pc_Id in Lab:
        del Lab[Pc_Id]
        print("*Successfully Removed*")
    else:
        print("Pc Id Not Found")


def IndividualPcInformation():
    Pc_Id = int(input("Enter the Id Number Of Pc: "))

    if Pc_Id in Lab:
        print('Pc_Name:', Lab[Pc_Id]["Pc_Name:"])
        print('Operating_System:', Lab[Pc_Id]["Operating_System:"])
        print('Status Of the PC:', Lab[Pc_Id]["Status Of the PC:"])
    else:
        print("Pc Id Not Found")

def StoreInfo():
    f = open("C:\\Users\\sswap\\Documents\\Mid_Project\\Save_All_Pc_Information.txt","w+")
    f.write(json.dumps(Lab, indent=3, sort_keys=True))
loop = True
while loop:
    print("_____________________________________________________")
    print("Press 1 For Add New Pc")
    print("Press 2 For Update Pc Information")
    print("Press 3 For Remove Pc")
    print("Press 4 For See All Pc Information")
    print("Press 5 For See Individual Pc Information")
    print("Press 6 For Search A Pc")
    print("Press 7 For Store all the PC information into a text file")
    print("Press 8 For Quit From The System")
    print("*****************************************************")
    print("")

    a = int(input("Enter Number :"))
    if a == 1:
        print('**For Adding New Pc**')
        AddPc()

    elif a == 2:
        print("**Update Pc Information**")
        UpdateInfo()

    elif a == 3:
        print("**Remove Pc**")
        RemovePc()
    elif a == 4:
        print("**All Pc Information**")
        print(Lab)
    elif a == 5:
        print("**Individual Pc Information**")
        IndividualPcInformation()

    elif a == 6:
        print("**Search A Pc**")
        IndividualPcInformation()
    elif a == 7:
        print("**Successfully Stored all the PC information into a text file**")
        StoreInfo()
    elif a == 8:
        print("**You Have Quited From The System**")
        loop = False
    else:
        print("**You Have Entered A Wrong Number**")
    continue
