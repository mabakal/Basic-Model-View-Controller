import csv

def main():

    # z will be the variable that ends the program.
    z = 2
    while z == 2:

        print('Project Running Now.')

        choice = input('\nEnter 1 to Display or 2 to not display.')

        if choice == "1":
            # Reading Information Now.
            with open('NAFO-4TVN-Atlantic-Cod-otoliths.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    print(line)

        else:

            print('2 was entered.')

        # Requesting user input now.
        t = int(input('\nEnter 9 to Terminate Program:'))

        if t == 9:
            print('Terminating Program.')

            #Changing z from 2 to 3.
            z += 1

        else:

            print('Looping Script.')

    print('We are done.')


# Practical Project Part 02  // due date Sep-23-2022
# Ali Al-Rawe 040982650 Alra0059@algonquinlive.com
main()
