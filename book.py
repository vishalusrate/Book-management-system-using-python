class Library:

    # private variable here

    _list_book = {}

    _lend_book = {}

    # ye constructor hai

    def __init__(self,name,lname):

        self.name = name

        self.lname = lname

        if self.name != '' and self.lname != '':

            self.userInputcall()



    def check_whitch_book_add(self):

        print("Do you want to the the existing user as book name \n 1. Yes \n 2. No")

        existing_user = int(input())

       



        if(existing_user == 1):

            print("Please Enter Your Book name ")

            book_name = input()

            return book_name

        else:

            print("Please Enter the Person name here ....")

            name_of_the_person = input()

            print("Please Enter Your Book name ")

            book_name = input()

            return [book_name,name_of_the_person]

         

    def userInputcall(self):

        print("Please enter the what do you \n 1.Display book \n 2. Add book \n 3.Lend Book \n. 4.Return Lend book")

        user_input = int(input())

       



        if user_input == 1:

            self.displayBook()

        elif user_input == 2:

            book_name = self.check_whitch_book_add()

            # print(type(book_name) == '')

            if type(book_name) is list:

                self.addBook(book_name[0],book_name[1])

            else:

                self.addBook(book_name,self.name)

        elif user_input == 3:

            self.lend_book()

        elif user_input == 4:

            self.return_lend_book()



    def displayBook(self):

        print(f"This is the book list Here \n {self._list_book}")

        self.userInputcall()

   

    def addBook(self,book_name,person_name,lended=False):

        # print(self._list_book[self.name])

        if person_name == '':

            self.name = self.name

        else:

            self.name = person_name



        if self.name in self._list_book:

            self._list_book[self.name]+= [book_name]

        else:

            self._list_book[self.name] = [book_name]    

        if lended == False:

            print("Do you want to add another book \n 1.Yes \n 2.NO")

            repeat_add = int(input())

        else:

            repeat_add = 0



           



        if(repeat_add == 1):

            book_name = self.check_whitch_book_add()

            self.addBook(book_name,self.name)

        else:

            print("Your book is added on our library ....")

            self.userInputcall()





    def lend_book(self):

        print("Please Enter Which book do you want to lend")

        lend_book = input()

        for item,book in self._list_book.items():

            if lend_book in book:

                self._lend_book[lend_book] = "The book is lended by the :- "+ self.name +" Author of the Book is "+item

                key =f'{item}'

                items = self._list_book[key]

                items.remove(f'{lend_book}')

                print("Entry added by your against your rollnumber")

            else:

                for item,book in self._lend_book.items():

                    print("test")

                    if lend_book in item:

                        print(self._lend_book[f'{item}'])

                    else:

                        print("Book is not avaiable now")

            self.userInputcall()

   

    def return_lend_book(self):

        print("Please Enter Which book do you want to lend")

        lend_book = input()

        for item,book in self._lend_book.items():

            if lend_book == item:

                bok_details = self._lend_book[f'{item}']

                bok_details = list(bok_details.split(" "))

                author = bok_details[13]

                print("Entry remove by your against your rollnumber")

                del self._lend_book[f'{item}']

                # print(self._lend_book.remove(f'item'))

                print(self._lend_book)

                self.addBook(item,author,True)

            # def addBook(self,book_name,person_name):

           









# pass karna hoga constructor so pass the  name and last name



print("Please enter the Name please")

name = input()

print("Please enter your last name ")

lname = input()



library = Library(name,lname)



print(library)