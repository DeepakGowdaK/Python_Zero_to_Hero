class Fullname:
    def __init__(self, Fname:str, Lname:str):
        self.Fname = Fname
        self.Lname = Lname

    def userID(self):
        return f'{self.Fname}.{self.Lname}@companyName.com'

name = Fullname('hai', 'dude')

print(name.userID())