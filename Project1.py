class Lms:
    book_dict = {}
    def add_books(self,new_book_dict):
        self.book_dict = new_book_dict

    def remove_books(self,title):
        self.book_dict = self.book_dict.pop(title)

    def update_book_info(self,title,new_tuple):
        new_dict = {title : new_tuple}
        self.book_dict.update(new_dict)

    def disp_avail_books(self):
        print(f"Available books : {self.book_dict}")

    def search_book_by_title(self, title):
        if self.book_dict.fromkeys(title):
            print(f"Book found! : {self.book_dict}")
        else:
            print("Book not found.")

operations = Lms()

class User(Lms):
    user = {}
    borrowed_dict = {}
    def add_user(self, user_dict):
        self.user = user_dict
    def borrow_books(self,b_dict):
        self.borrowed_dict = b_dict

class Options(Lms):
    @staticmethod
    def option_1():
        new_book_dict = {}
        title = input("Enter title of book : \n")
        author = input("Enter author of book : \n")
        quantity = int(input("Enter quantity : \n"))
        dict_tuple = (author,quantity)
        new_book_dict.update({title : dict_tuple})
        operations.add_books(new_book_dict)
        operations.disp_avail_books()

    @staticmethod
    def option_2():
        title = input("Enter title of book : \n")
        operations.remove_books(title)
        operations.disp_avail_books()

    @staticmethod
    def option_3():
        title = input("Enter title of book : \n")
        author = input("Enter new author of book : \n")
        quantity = int(input("Enter new quantity : \n"))
        new_tuple = (author,quantity)
        operations.update_book_info(title, new_tuple)
        operations.disp_avail_books()

    @staticmethod
    def option_4():
        operations.disp_avail_books()

    @staticmethod
    def option_5():
        title = input("Enter title of book : \n")
        operations.search_book_by_title(title)

options = Options()
print("Welcome to LMS! \n\n")

options_dict = {
    1:"Add user",
    2: "Add books to the library.",
    3: "Remove books from the library.",
    4: "Update book information (change quantity, update author).",
    5: "Display available books.",
    6: "Search for books by title.",
    7:"Borrow books.",
    8:"Return books.",
    9:"Display borrowed books.",
    10:"Display overdue books and penalty.",
    11:"Display past borrowed books."
}

flag = True

def check_option(n):
    match n :
        case 1 :
            Options.option_1()
        case 2:
            Options.option_2()
        case 3:
            Options.option_3()
        case 4:
            Options.option_4()
        case 5:
            Options.option_5()
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass

while flag:
    print(f"Available operations : \n {options_dict}")
    num = int(input("Enter your option number : \n"))
    check_option(num)
    res = input("Do you want to continue (y/n) : \n").lower()
    if res == 'y':
        flag = True
    else:
        flag = False


