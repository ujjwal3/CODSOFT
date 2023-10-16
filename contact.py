contacts = {}


def AddContact():
    contact_name = input("Enter Contact Name: ")
    userNumber = input("Enter Phone Number: ")
    userEmail = input("Enter E-mail: ")
    userAddress = input("Enter Address: ")
    contact_info = {"Phone No": userNumber, "E-Mail": userEmail, "Address": userAddress}
    contacts[contact_name] = contact_info


def ViewContact():
    print(contacts)


def SearchContact():
    SearchName = input("Enter Name for Information: ")
    if SearchName in contacts:
        print(f"----Details of user Named {SearchName}----")
        contact_info = contacts[SearchName]
        print("Contact Name: ", SearchName)
        print("Contact Number: ", contact_info["Phone No"])
        print("Contact E-mail: ", contact_info["E-Mail"])
        print("Contact Address: ", contact_info["Address"])
    else:
        print("Contact Is Not Present In DIctionary")


def UpdateContact():
    SearchName = input("Enter Name for Modification: ")
    if SearchName in contacts:
        print(f"----Choose The Information You Want to Modify For {SearchName}----")
        contact_info = contacts[SearchName]
        print("1. Number Modify")
        print("2. Email Modify")
        print("3. Address Modify")
        UpdateInput = int(input("Enter Option Which You Want to Perform: "))
        if UpdateInput == 1:
            newNNumber = str(input("Enter New Number: "))
            contact_info["Phone No"] = newNNumber
        elif UpdateInput == 2:
            newNEmail = str(input("Enter New Email: "))
            contact_info["E-Mail"] = newNEmail
        elif UpdateInput == 3:
            newNAddress = str(input("Enter New Address: "))
            contact_info["Address"] = newNAddress
        else:
            print("INVALID INPUT!")

    else:
        print("INVALID INPUT!")


def DeleteContact():
    SearchName = input("Enter Name for Delete: ")
    if SearchName in contacts:
        del contacts[SearchName]
        print(f"Information & Contact Deleted Successfully For {SearchName}")

    else:
        print("Name is Not Present")


print("Welcome To Contacts Book")
while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    userInput = int(input("Enter Option Which You Want to Perform: "))
    if userInput == 1:
        AddContact()
    elif userInput == 2:
        ViewContact()
    elif userInput == 3:
        SearchContact()
    elif userInput == 4:
        UpdateContact()
    elif userInput == 5:
        DeleteContact()
    else:
        print("INVALID INPUT!")
        break
