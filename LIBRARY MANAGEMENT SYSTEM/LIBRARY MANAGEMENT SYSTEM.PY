import datetime
import os
# os.getcwd()
class LMS:
    """THIS CLASS IS USED TO KEEP RECORDS OF BOOK LIBRARY
    IT HAS TOTAL FOUR MODULE:"DISPLAY BOOKS","ISSUE BOOKS","RETURN BOOKS","ADD BOOKS"
    """
    def __init__(self,list_of_books,library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            print(line)
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
            "lender_name": "","Issue_data":",","Status":"Available"}})
            Id = Id+1

    def display_books(self):
        print("-------------------LIST OF BOOKS-------------------")
        print("BOOKS ID","\t","TITLE OF THE BOOK")
        print("---------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("Status"),"]")

    
    def Issue_books(self):
        books_id = input("Enter books ID: \n")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print (f"This Book is already issued to {self.books_dict[books_id]['lender_name']} \
                    on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                your_name = input("Enter Your Name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"
                print("Books Issued Succesfully !!!")
        else:
            print("Book Id Not Found !!!")

    def add_books(self):
        new_books = input("Enter Books Title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Books title length is too long!!!Title length should be 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':"",
                'Issue_date':"",'Status':"Available"}})
                print(f"This books '{new_books}' has been added succesfully !!!")

    def return_books(self):
        books_id = input("Enter books  ID :")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in library.please check your book ID.")
                return self.return_books()
            elif not self.books_dict[books_id]['Status'] == "Available": 
                self.books_dict[books_id]['lender_name'] = ""
                self.books_dict[books_id]['Issue_date'] = ""
                self.books_dict[books_id]['Status'] = "Available"
                print("Succesfully Updated !!!\n")
        else:
            print("Book Id is not found")

try:
    myLMS = LMS("List_of_books.txt","python's library")
    press_key_list ={"D": "Display Books","I":"Issue Books","A":"Add Books","R":"Return Books","Q":"Quit Operation"}
    key_press = False
    while not(key_press == "q"):
        print(f"\n--------------WELCOME TO {myLMS.library_name} LIBRARY MANAGEMENT SYSTEM-----------\n")
        for key,value in press_key_list.items():
            print("Press",key,"To",value)
        key_press = input("Press Key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection : Issue Books \n")
            myLMS.Issue_books()
        elif key_press =="a":
            print("\nCurrent Selection : Add Book \n")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection : Display Books\n")
            myLMS.display_books()
        elif key_press =="r":
            print("\nCurrent Selection : Return Books\n")
        elif key_press =="q":
            break
        else:
            continue
except Exception as e:
    print("Something went wrong!!Please check your input!!!")
                

l = LMS("List_of_books.txt","Python's Library")
print(l.display_books())

# print(LMS("List_of_books.txt","Python's Library"))



