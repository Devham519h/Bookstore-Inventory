#Devin Hamilton
#12/03/24
#Comp163 Section 002
#This program creates inventory display for each genre with the use of files and functions
#The user can see the book's title, genre, price, author, quantity, and publish year

import csv

options = [] #list to hold the genres
inventory = {} #dictionary to hold the genre:book info pairs

#Function takes the argument from options and makes list
def displayMenu(options):
    count = 0
    for i in options: #loop creates the menu
        print(f'{count+1}) {i}')
        count += 1
    print(f'{count+1}) Exit')

def readInv(file):
    with open(file) as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')  # splits the info in the file by ","
        for row in csvfile:
            Genre, firstName, middleName, lastName, Title, DOB, yearPublished, Cost, Quantity, ISBN = row
            if Genre in options:
                pass
            else:
                #Each genre in inventory will contain a list value with all of the book info
                inventory[Genre] = []
                options.append(Genre)

            inventory[Genre].append(row) #the book info will be added to its corresponding key
    return options

def displayGenreInv(genreOption,booksList):
    if genreOption in range(1,len(booksList)+1):
        invCount = 0  # This counter is used to keep track of how many books are in the genre inventory
        count = 0  # This counter is used for the total cost of all the genre's books
        print(booksList[genreOption - 1])  # prints the genre title by reading the genre list from indexes 0-4
        print(f'\t{'Author':<20}{"Title":<30}{"Published":9} {"QTY":5}{"Price":5}')  # Formatting for the Header
        for each in inventory[booksList[genreOption - 1]]:  # for each list (book info) in the genre key's list value
            wholeName = (f'{each[1]} {each[3]} {each[2]}')
            print(f'\t{wholeName:20}{each[4]:30}{"2024":9} {each[8]:5}{float(each[7]):<5}{" ":15}')
            invCount += int(each[8])
            count += float(each[7]) * int(each[8])  # add the book's cost to count
        print(f'\t{"=" * 33}')
        print(f'\tInventory count {invCount} : Total ${count:.2f}')


file = input("Enter inventory file: ")
displayMenu(readInv(file))

while True:
    choice = int(input("Enter your choice: "))
    #choice becomes the argument for displayGenreInv(), and prints the books and their information
    displayGenreInv(choice, options)
    # The program ends if choice is the exit number
    if choice == len(options)+1:
        print(f'\nAggie Book Store')
        print(f'Good Bye')
        break














