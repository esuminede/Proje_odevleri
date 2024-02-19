import os

class Library:
    def __init__(self):
    
        self.file = "books.txt"
        self.file = open(self.file, 'a+')
        
    def __del__(self):
        self.file.close()   
        print("\nFile is closed.\nIf you want to continue you have to restart the project.\n")
#-----------------------------------------------------------   

    def listBooks(self):
        file = open("/home/esa/Desktop/10MillionAi/Python/Proje_odevleri/books.txt", 'r+')
        data = file.read()
        line = data.splitlines()
        
        print("Titles\t\tAuthors")
        for i in range(len(line)):
            split_word = line[i].split(",")
            title = split_word[0] 
            author = split_word[1]

            print(f"{title}\t\t{author}")     
        
#-----------------------------------------------------------

    def addBook(self):
        title = input("Book Name: ")
        author = input("Author's Name: ")
        releasedDate = input("Year of Release: ")
        pages = input("Enter the page number: ")

        title = title.lower()
        title = title.capitalize()
        self.authors = author.lower()
        author = author.capitalize()
        
        self.file.write(f"{title}, {author}, {releasedDate}, {pages}\n")
        self.file.flush()

#------------------------------------------------------------
        
    def removeBook(self):
        
        file = open("/home/esa/Desktop/10MillionAi/Python/Proje_odevleri/books.txt", 'r+')
        data = file.read()
        line = data.splitlines()

        titles = []
        authors = []
        releasedDates = []
        pages = []

        for i in range(len(line)):
            split_word = line[i].split(",")
            titles.append(split_word[0]) 
            authors.append(split_word[1])
            releasedDates.append(split_word[2])
            pages.append(split_word[3])

        book = input("Enter the book's title you want to remove from file: ")
        book = book.lower()
        book = book.capitalize()
        file.close()

        count = 0
        
        for i in range(len(line)):
            if titles[i] == book:
                count = i
                file = open("/home/esa/Desktop/10MillionAi/Python/Proje_odevleri/books.txt", 'w+')
                break
                    
        if count != 0:
            titles.remove(titles[count])
            authors.remove(authors[count])
            releasedDates.remove(releasedDates[count])
            pages.remove(pages[count])

            print(f"\n{book} is removed from file.")

            for j in range(len(line)-1):
                file.write(f"{titles[j]}, {authors[j]}, {releasedDates[j]}, {pages[j]}\n")
                file.flush()
        else: 
            print(f"There is no such a book named '{book}'.\n
    
 #-----------------------------------------------------------------------------------
    
lib = Library()
while True:
    print("\n1. Add Book\n2. List Books\n3. Remove Book\nq. Quit")
    choice = input("Select an operation (q for quit): ")
    print("\n")
    if choice == '1':
        lib.addBook()
    elif choice == '2':
        lib.listBooks()
    elif choice == '3':
        lib.removeBook()
    elif choice == 'q':
        approve = input("Are you sure about exitting? y/n\n")
        if approve == 'y' or approve == 'Y':
            break
        elif approve == 'n' or approve == 'N': 
            continue
    
    else:
        print("Please enter a right command: ")

    
