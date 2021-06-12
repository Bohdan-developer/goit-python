from collections import UserDict


class AddressBook(UserDict):
    
    data = dict()

    def add_record(self, record):
        self.data[f"{record.name.value}"] = record
        

class Record:
    
    record = dict()
    
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.phones = list()
        
    
    def add(self, phone):
        self.phones.append(phone)

    def deletion(self, phone):
        self.phones.remove(phone)

    def editing(self, phone, new_phone):
        i = self.phones.phones.index(phone)
        self.phones.phones.pop(i)
        self.phones.phones.insert(i, new_phone)
            
        

class Filed():
    pass

class Name(Filed):
    
    def __init__(self, name):
        self.value = name

class Phone(Filed):
    
    def __init__(self, phone):
        self.value = phone

