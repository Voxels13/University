#

class Library:

    def __init__(self,title,author,availability = True):

        self.title = title
        self.author = author
        self.availability = availability

    #

    def check_out(self):

        if self.availability:
            print(f"{self.title} has been checked out")
            self.availability=False
        else:
            print(f"{self.title} is not available at the moment")

    #

    def return_book(self):

        if not self.availability:
            print(f"{self.title} has been returned")
            self.availability=True
        else:
            print(f"{self.title} has not been checked out")

    #

    def display_info(self):

        self.status = "Available" if self.availability else "Not Available"
        print(f"Book: {self.title} || Author: {self.author} || Status: {self.status}")

#Create objects -- books

book1 = Library("Metamorphosis","Kafka")

book1.display_info()

book1.check_out()
book1.display_info()

book1.return_book()
book1.display_info()

