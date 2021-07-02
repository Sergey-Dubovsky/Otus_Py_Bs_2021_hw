class User:
    def __init__(self, name, surname, post_address, cell_phone_number):
        self.name = name
        self.surname = surname
        self.post_address = post_address
        self.cell_phone_number = cell_phone_number
        self._password = ""
        self.pets = []

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pass_string):
        self._password = pass_string

    def __iadd__(self, pet):
        self.pets.append(pet)
        return self

    def __len__(self):
        return len(self.pets)

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.surname}, {self.post_address}, {self.cell_phone_number}, {self.pets})"


class Pet:
    def __init__(self, name, breed, year_of_birth, owner):
        self.name = name
        self.breed = breed
        self.year_of_birth=year_of_birth
        self.owner = owner

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.breed}, {self.year_of_birth}, {self.owner})"
        
    
user1=User('Bob','Smith',"St'Petersburg, Russia",'+78122128506')
user2=User('Mary','Poppins','London, Britain','+78122128506')
user1.password='12345'
user2.password='qwerty'
print(user1) 
print(user1.password) 
print(user2) 
print(user2.password) 

pet1=Pet('Sharik','big dog',2015,user1)
pet2=Pet('Barbos','small dog',2020,user1)
pet3=Pet('Murka','cat',2020,user2)
pet4=Pet('Slow Stone','turtle',1900,user2)
pet5=Pet('Betsy','gold fish',2020,user2)

print(pet1) 
print(pet2) 
print(pet3) 
print(pet4) 
print(pet5) 

user1+=pet1
user1+=pet2

user2+=pet3
user2+=pet4
user2+=pet5

print(user1) 
print(len(user1)) 
print(user2) 
print(len(user2)) 
