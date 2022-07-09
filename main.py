import string
from unicodedata import name
from faker import Faker

class Person:
    def __init__(self, name:string, job:string , email:string) -> None:
        self.name = name
        self.job = job
        self.email = email
    def __repr__(self) -> str:
        return f"Name: {self.name} \n Job : {self.job}\n E-mail : {self.email} \n"


def generateFakeData(qtd:int,fake:Faker):
    fakedata = []
    for x in range(5):
        person = Person(fakeGen.name(),fakeGen.job(),fakeGen.ascii_free_email())
        fakedata.append(person)
    return fakedata

fakeGen = Faker('pt_BR')
fakeData = generateFakeData(4,fakeGen)
print(fakeData)


