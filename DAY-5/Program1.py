#Create a phonebook(dict) : add , search , delete contacts
phonebook = {}
while True :
    print("---Phonebook Menu---")
    print("1. add contact.")
    print("2. search contact.")
    print("3. delete contact.")
    print("4. Print all contact.")
    print("5. exit.")
    choice = input("Enter your choice(1-5) :  ")
    if choice == "1" : 
        name = input("Enter contact name : ")
        number = input("Enter phone number  : ")
        phonebook[name] = number
        print("Contact added sucessfully!")
    elif choice == "2" :
       name = input("Enter contact name to search : ")
       if name in phonebook :
           print((name) , ":" , phonebook.get(name))
       else :
           print("Contact not found in phonebook.")
    elif choice == "3" :
        name = input("Enter contact name to delte : ")
        if name in phonebook :
            del phonebook[name]
            print("contact " , (name) , "is deleted sucessfully. ")
        else :
            print("Contact not found.")
    elif choice == "4" :
        if len(phonebook) == 0 :
             print("Phonebook is empty.")
        else :
             print("All contact in phonebook : ")
             for name , number in phonebook.items() :
                print((name) , ":" , (number))
             #phonebook.item()
    elif choice == "5" :
        print("Exiting Phonebook...")
        break
    else :
        print("Invalid Choice! Please try again. ")