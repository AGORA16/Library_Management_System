class library:
    books={'a':10,'b':5,'c':8,'d':16,'e':20}
    def __init__(self,cname):
        self.cname=cname
        self.nob=0
        self.books={}

    def main(self):
        print()
        op=int(input('Enter 1 to displya the library books \nEnter 2 to dosplay your details \nEnter 3 to borrow a book \nEnter 4 to return a book \nEnter 5 to exit \n-->'))
        if op==1:
            self.library_books()
            self.main()
        elif op==2:
            self.display_c_details()
            self.main()
        elif op==3:
            self.borrow_book()
            self.main()
        elif op==4:
            self.return_book()
            self.main()
        elif op==5:
            print('Thanks... Visit Again')
            return
        else:
            print('Invalid Input')
            self.main()

    @classmethod
    def library_books(cls):
        print ("Books in library are:")
        for i in library.books:
            print(f'{i}',f'{library.books[i]}',sep='\t')

    def display_c_details(self):
        print ('Name: (self.cname)')
        print (f'No. of books taken: {self.nob}')
        if self.books!={}:
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
                if library.books [bname]>0:
                    library.books [bname] -=1
                    print('Successfully borrowed')
                    self.nob+=1
                    self.books[bname]=1
                else:
                    print ('Book is not available.')
            else:
                print('No such book is available')
        else:
            print('Limit Exceeded')

    def return_book(self):
        if self.nob>0:
            bname=input('Enter a book name :')
            if bname in self.books:
                if bname in library.books:
                    print('Returned Successfully...')
                    self.nob-=1
                    library.books[bname]+=1
                    self.books.pop(bname)
                else:
                    print('This book is not belong to us..')
            else:
                print("You didn't take this book from our library..")
        else:
            print('No Books borrowed ... please borrow one to return')

l1=library('raj')
l1.main()



















 
