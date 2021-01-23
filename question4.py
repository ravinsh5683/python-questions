"""Business Logic Layer"""

listID = []
listName = []
listAddress = []
listMob = []


def add_customer(id, name, address, mobile):
    listID.append(id)
    listName.append(name)
    listAddress.append(address)
    listMob.append(mobile)


def search_customer(id):
    if listID.__contains__(id):
        i = listID.index(id)
        print("Name = ", listName[i], "Address=", listAddress[i], "Mobile =",
              listMob[i])  # wrong line of code - will be solved with OOPS.
    else:
        print("Search not found")


def delete_customer(id):
    if listID.__contains__(id):
        i = listID.index(id)
        listID.pop(i)
        listName.pop(i)
        listAddress.pop(i)
        listAddress.pop(i)
        print("Delete successful")
    else:
        print("No such ID is present")


def modify_customer(id):
    if listID.__contains__(id):
        i = listID.index(id)
        while (True):
            print("What do you want to modify or update")
            print("""1. Name \n
                2. Address \n 
                3. Mobile no \n 
                4. Exit
                """)

            ch1 = input("Enter the option you want to update")

            if ch1 == '1':
                name = input("enter the new name")
                listName[i] = name
            elif ch1 == '2':
                address = input("enter the new address")
                listAddress[i] = address
            elif ch1 == '3':
                mobile = input("enter the new mobile no")
                listMob[i] = mobile
            elif ch == '4':
                break
            else:
                print("Wrong Option")

    else:
        print("No such ID is present")


def show_all():
    print("ID = ", listID, "\n", "Name = ", listName, "\n", "Address=", listAddress, "\n", "Mobile =",
          listMob)


"""Presentation Layer"""

while(True):
    print("""1. Add Customer \n
        2. Search Customer \n 
        3. Delete Customer \n 
        4. Modify Customer \n 
        5. Show All Customers \n  
        6. Exit """)

    ch = input("Enter your choice")

    if ch == '1':
        id = int(input("Enter ID"))
        name = input("Enter Name")
        address = input("Enter Address")
        mobile = input("Enter Mobile No")
        add_customer(id, name, address, mobile)
        print("Customer Added Successfully")

    elif ch == '2':
        id = int(input("enter your ID"))
        search_customer(id)

    elif ch == '3':
        id = int(input("enter the ID you want to delete"))
        delete_customer(id)

    elif ch == '4':
        id = int(input("enter the ID you want to modify"))
        modify_customer(id)
    elif ch == '5':
        print("Customer details:")
        show_all()

    elif ch == '6':
        exit()
    else:
        print("Please enter a valid option")
