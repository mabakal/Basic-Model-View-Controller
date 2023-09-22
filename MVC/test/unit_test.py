from skeleton.Controler.controler import *

continuer = "Y"
while continuer == "Y":
    print("1: Reload the data from the dataset, replacing the in-memory data")
    print("2: Persist the data from memory to the disk as a comma-separated file, writing to a new file.")
    print("3: Select and display either one record, or display multiple records from the in-memory data")
    print("4: Create a new record and store it in the simple data structure in memory")
    print("5: Select and edit a record held in the simple data structure in memory")
    print("6: Select and delete a record from the simple data structure in memory")

    number = int(input("Enter the number:"))

    if number == 1:
        readData()
    elif number == 2:
        persitData()
    elif number == 3:
        n = int(input("Enter the number of record to be display:"))
        display(n)
    elif number == 4:
        createData()
    elif number == 5:
        editData()
    else:
        deleteDate()
    continuer = input("Do you want to continue?Y or N:")
    




