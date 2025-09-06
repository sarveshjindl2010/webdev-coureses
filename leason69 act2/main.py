class Library:
    def __init__(self, list_of_books, name):
        self.booklist = list_of_books
        self.name = name
        self.lenDict = {}

    def displayBooks(self):
        print(f"we have the following books in our library: {self.name}") 
        for book in self.booksList:
            print(book)

    def lendbook(self, user, book):
        if book not in self.booksList:
            print("Sorry, we don't have that book.")
        elif book in self.lenDict:
            print("The book is already being used by {self.lenDict[book]}")               
        else:
            self.lenDict[book] = user
            print(
                "Lender-book datebase has been updated. You can take the book now."
            )
def addbook(self, book):
    self.booksList.append(book):
    print(f"{book} has been added to the book list.") 
def returnbook(self, book):
    if book in self.lenDict:
        del self.lenDict[book]
        print("Book has been returned.")
    else:
        print("This book wasn' borrowed from us .")
if __name__ == '__main__':
    books = Library({
        "Python",
        "Rich Dad Poor Dad",
        "Harry Potter",
        "C++",
        "Java",
        "Algorithms",
        "Data Structure",
    })                 
    user_name = input("Welecome to our library! Plese enter your name:")
    while True:
        print(
            f"\nHello {user_name}, welcome to the {books.name} lebrary. Please choose an option:"
        )
        print(
            "1. Display Books\n2. Lend  a book\n3. Add a book\n4. Return a book\5. Quit"
        )
        user_choice = input("Enter your choice to continue:")
        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option.")
            continue
        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you wanr to lend:")
            books.lendBook(user_name, book)
        elif user_choice == '3':
            book = input("Enter the name of book you want to add:")
            books.addBook(book)
        elif user_choice == '4':
            book = input("Enter the name of book you want to return:")
            books.returnBook(book)
        elif user_choice == '5':
            print(f"Thanks for using the library, {user_name}. Have a great day!")
            break