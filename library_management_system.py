class library:
    books={'python':10,'java':5,'webtech':8,'sql':16,'django':20}
    def __init__(self,cname):
        self.cname=cname
        self.nob=0
        self.books={}

    def main(self):
        print()
        op=input('Enter 1 to display the library books \nEnter 2 to display your details \nEnter 3 to borrow a book \nEnter 4 to return a book \nEnter 5 to exit \n-->')
        if op=='1':
            self.library_books()
            self.main()
        elif op=='2':
            self.display_c_details()
            self.main()
        elif op=='3':
            self.borrow_book()
            self.main()
        elif op=='4':
            self.return_book()
            self.main()
        elif op=='5':
            print('Thanks... Visit Again')
            return
        else:
            print('Invalid Input')
            self.main()

    @classmethod
    def library_books(cls):
        print ("Books in library are:")
        print("Book Name","No.of Books Available",sep="\t")
        for i in library.books:
            print(f'{i}',f'{library.books[i]}',sep='\t\t\t')

    def display_c_details(self):
        print (f'Name: {self.cname}')
        if self.books!={}:
            print (f'No. of books taken: {self.nob}')
            print('Your books are :')
            c=1
            for b in self.books:
                print(f'{c} : {b}')
                c+=1
        else:
            print('No Books Borrowed..')

    def borrow_book(self):
        if self.nob<4:
            bname=input('Enter the book name:')
            if bname in library.books:
                if bname not in self.books:
                    if library.books [bname]>0:
                        library.books [bname] -=1
                        print('Successfully borrowed')
                        self.nob+=1
                        self.books[bname]=1
                    else:
                        print ('Sorry... Currently This Book is not available.')
                else:
                    print('You are not supposed to take the same book more than once...')
            else:
                print('Sorry... No such book is available in our Library.')
        else:
            print('Limit Exceeded')

    def return_book(self):
        if self.nob>0:
            bname=input('Enter a book name :')
            if bname in library.books:
                if bname in self.books:
                    print('Returned Successfully...')
                    self.nob-=1
                    library.books[bname]+=1
                    self.books.pop(bname)
                else:
                    print("Sorry... You didn't take this book from our library..")   
            else:
                print('Sorry... This book is not belong to us..')
        else:
            print('No Books borrowed ... please borrow one to return')
            
print('*********************** WELCOME TO ADVANCED LIBRARY MANAGEMENT SYSTEM OF ABC COLLEGE ***********************')
l1=library('raj')
l1.main()



















 
