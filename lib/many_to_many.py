class Author:
    all =[]
    def __init__(self, name="Name"):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract( self, book, date, royalties):
        contract = Contract( self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        contract_royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        total_royalties = sum(contract_royalties)
        return total_royalties
        

class Book:
    all=[]
    def __init__(self, title="String"):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all=[]
    def __init__(self, author = "Author", book = "Book", date="01/01/2001", royalties=0):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def get_author(self):
        return self._author

    def set_author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise Exception("Author must be an instance of the Author class")
        
    author = property(get_author, set_author)
        
    
    def get_book(self):
        return self._book
    
    def set_book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        else:
            raise Exception("Book must be an instance of the Book class")
        
    book = property(get_book, set_book)

    def get_date(self):
        return self._date
    
    def set_date(self, new_date):
        if type(new_date) == str:
            self._date = new_date
        else:
            raise Exception("Date must be of type String")
    
    date = property(get_date, set_date)

    def get_royalties(self):
        return self._royalties 
    
    def set_royalties(self, new_royalty):
        if isinstance(new_royalty, int):
            self._royalties = int(new_royalty)
        else:
            raise Exception("Royalty must be of type Float")
        
    royalties = property(get_royalties, set_royalties)

    @classmethod
    def contracts_by_date(cls, date=None):
        if date:
            return [contract for contract in Contract.all if contract.date == date]
        else:
            return sorted(Contract.all, key=lambda contract:contract.date)