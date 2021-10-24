import time, os, sys, pymongo
from termcolor import colored
os.system('color')

print(colored("Author: *********************", 'white'))
print(colored("********** Database application.", 'white'))

menu = True
while menu:
    print(colored("#######################", 'green'))
    print(colored("#", 'green')+(colored("  Available Options  ", 'blue')+(colored("#", 'green'))))
    print(colored("#######################", 'green'))
    print(colored("#", 'green')+(colored(" 1. Drivers   ", 'blue')+(colored("#", 'green'))))
    print(colored("#", 'green')+(colored(" 2. Books        ", 'blue')+(colored("#", 'green'))))
    print(colored("#", 'green')+(colored(" 3. EXIT             ", 'blue')+(colored("#", 'green'))))
    print(colored("#######################", 'green'))
# Entering database number as input
    menu = input(colored("\nEnter database number: ", 'green'))
# Working in Drivers database
    if menu == "1":
        client = pymongo.MongoClient("mongodb+srv://yourURL")
        db = client.DB
        mycol = db["YourCollection"]

        print(colored("\nYou're working in '######' database\n", 'white'))

        def slowprint(s):
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1. / 20)
        print(colored("Loading...", 'white'))
        slowprint(colored("* * * * * * * * * * * * * * * * *\n", 'white'))

        ################################################################################################
        # Choices
        mychoice = True
        while mychoice:
            print(colored("#  Available Options  #\n", 'green'))
            print(colored("1. Add user to the database.", 'green'))
            print(colored("2. Look for a user in the database.", 'green'))
            print(colored("3. Show all users in database.", 'green'))
            print(colored("4. Delete user from database (Admin Access).", 'green'))
            print(colored("5. Exit.\n", 'green'))
            mychoice = input(colored("Choose your option: ", 'red'))
            print("")

            # Adding a user to the database
            if mychoice == "1":
                name = input(colored("Enter name (First and Last name): ", 'red'))
                adres = input(colored("Enter address (Street and number): ", 'red'))
                adres2 = input(colored("Enter address (Postal Code and City): ", 'red'))
                born = input(colored("Enter birth date (DD.MM.YYY): ", 'red'))
                bornin = input(colored("Enter birth place (City, Country): ", 'red'))
                mylist =[{"Name": name, "Address": adres, "Address2": adres2, "Born": born, "BornIn": bornin},]
                x = mycol.insert_many(mylist)
                print(colored("\nUser added succesfull!", 'green'))
                time.sleep(1)
                input(colored("\nPress ENTER to continue...\n", 'blue'))

            # Looking for specific user using his "Name" as the key
            if mychoice == "2":
                find = input(colored("\nEnter the name you are looking for: ", 'red'))
                myquery = {"Name": find}
                mydoc = mycol.find(myquery)
                for x in mydoc:
                    print(colored("Search results: \n", 'green'))
                    print(*[f'{k}: {v}' for k, v in x.items()], sep='\n')
                    time.sleep(1)
                    input(colored("\nPress ENTER to continue...\n", 'blue'))
                mychoice = True

            # Printing all records in the database
            if mychoice == "3":
                print(colored("\nAll results in database: \n", 'green'))
                for x in mycol.find():
                    print(*[f'{k}: {v}' for k, v in x.items()], )
                time.sleep(2)
                input(colored("\nPress ENTER to continue...\n", 'blue'))
                mychoice = True

            # Deleting user from database by using "Name" Key, ADMIN Access, PIN REQUIRED
            if mychoice == "4":
                x = True
                while x:
                    try:
                        x = int(input(colored("\nEnter PIN Code to access ADMIN Panel: ", 'red')))
                        if x == 7031:
                            print(colored("Access Granted!", 'green'))
                            delete = input(colored("\nEnter the name of the user you want to delete: ", 'red'))
                            myquery = {"Name": delete}
                            mycol.delete_one(myquery)
                            print(colored("\nUser deleted!", 'green'))
                            time.sleep(1)
                            input(colored("\nPress ENTER to leave...\n", 'red'))
                            x = False
                    except ValueError:
                        print(colored("\nWrong Value!", 'red'))


            if mychoice == "5":
                input(colored("Press ENTER to continue...\n", 'red'))
                break
                mychoice = False
                menu = True

            if mychoice == "":
                mychoice = True
# Working in Red Books database
    if menu == "2":
        client = pymongo.MongoClient("mongodb+srv://Yoururlhere")
        db = client.DB
        mycol = db["Collection"]

        print(colored("\nYou're working in '########' database\n", 'white'))

        def slowprint(s):
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1. / 20)
        print(colored("Loading...", 'white'))
        slowprint(colored("* * * * * * * * * * * * * * * * *\n", 'white'))

        ################################################################################################
        # Choices
        ans = True
        while ans:
            print(colored("#  Available Options  #\n", 'green'))
            print(colored("1. Add book to the database.", 'green'))
            print(colored("2. Show all Redbooks in database.", 'green'))
            print(colored("3. Update plates (Change red book number).", 'green'))
            print(colored("4. Delete Redbook from database (Admin Access).", 'green'))
            print(colored("5. Exit.\n", 'green'))
            ans = input(colored("Choose your option: ", 'red'))
            print("")

            # Adding a redbook to the database
            if ans == "1":
                NrBlach = input(colored("Enter plates: ", 'red'))
                NrDowodu = input(colored("Enter book number: ", 'red'))
                mylist = [
                    {"Plates": NrBlach, "Redbook number": NrDowodu},
                ]
                x = mycol.insert_many(mylist)
                print(colored("\nData added succesfully!", 'green'))
                time.sleep(1)
                input(colored("\nPress ENTER to continue...\n", 'blue'))

            # Printing all records in the database
            if ans == "2":
                print(colored("\nAll results in database: \n", 'green'))
                for x in mycol.find({},{"_id" : 0, "Plates" : 1, "book number" : 1}):
                    print(*[f'{k}: {v}' for k, v in x.items()], sep='\n')
                time.sleep(2)
                input(colored("\nPress ENTER to continue...\n", 'blue'))
                ans = True

            if ans == "3":
                change = input(colored("In which plates you want to change no. of book?: \n", 'red'))
                myquery = {"Plates": change}
                changefor = input(colored("Please enter new book number for " + change + " plates.\n", 'red'))
                newvalues = {"$set": {"Redbook number": changefor}}
                mycol.update_one(myquery, newvalues)
                print(colored("\nChange succesfull!", 'green'))
                time.sleep(1)
                ans = True

            # Deleting user from database by using "Name" Key, ADMIN Access, PIN REQUIRED
            if ans == "4":
                x = input(colored("\nEnter PIN Code to access ADMIN Panel: ", 'red'))
                while x not in ["8801"]:
                    if not x.isdigit():
                        print(colored("Enter PIN Code in digit format!", 'green'))
                        time.sleep(1)
                    x = input(colored("Enter PIN Code: ", 'red'))

                if x in ["8801"]:
                    print(colored("Access Granted!", 'green'))
                    delete = input(colored("\nEnter the plates number you want to delete book: ", 'red'))
                    myquery = {"Plates": delete}
                    newvalues = {"$set": {"book number": "None"}}
                    mycol.update_one(myquery, newvalues)
                    print(colored("\nDeleted!\n", 'green'))
                    time.sleep(1)
                    input(colored("\nPress ENTER to continue...\n", 'blue'))
                ans = True

            if ans == "5":
                input(colored("Press ENTER to continue...\n", 'red'))
                ans = False
                menu = True
                break

            if ans == "":
                ans = True
# Ending the program
    if menu == "3":
        print("Program is closing...")
        time.sleep(1)
        break
# If any wrong input, returning to start
    if menu == "":
        menu = True
