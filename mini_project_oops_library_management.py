class Library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.landDict = {}

    def displayBook(self):
        print(f"We have following books in our Library {self.name}")
        for book in self.booklist:
            print(book)

    def landBook(self, user, book):
        if book not in self.landDict.keys():
            self.landDict.update({book:user})
            print("Lander-Book database has been updated. You can take the book Now!")
        else:
            print(f"Book is already taken by {self.landDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print('Book has been added to the book list')

    def returnBook(self, book):
        self.landDict.pop(book)

if __name__ == '__main__':
    hiren = Library(['Python', 'Java', 'PHP', 'Javascript'], "Coder's Library", )

while True:
    print(f'Welcome to the {hiren.name} Library. Enter Your choice to Continue')
    print("1. Display Books")
    print("2. Land A book")
    print("3. Add Book")
    print("4. Return a Book")
    user_choice = input()
    if user_choice not in ['1','2','3','4']:
        print("Please enter a valid Option")
        continue
    else:
        user_choice = int(user_choice)

    if user_choice == 1:
        hiren.displayBook()

    elif user_choice == 2:
        book = input("Enter the name of the book you want to land: ")
        user = input("Enter your Name: ")
        hiren.landBook(user, book)
    elif user_choice == 3:
        book = input('Enter the name of the book you want to add: ')
        hiren.addBook(book)

    elif user_choice == 4:
        book = input('Enter the name of the book you want to return: ')
        hiren.returnBook(book)
    else:
        print('Not a Valid Option')

    print("Press 'q' to Quit and 'c' to continue")
    user_choice2 = ""
    while(user_choice2 != 'c' and user_choice2 != 'q'):
        user_choice2 = input()
        if user_choice2 == 'q':
            exit()
        elif user_choice2 == 'c':
            continue


