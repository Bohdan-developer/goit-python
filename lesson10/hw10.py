from collections import UserDict


class AddressBook(UserDict):
    
    data = dict()

    def add_record(self, record):
        self.data[f"{record.name.value}"] = record
        

class Record:
    
    record = dict()
    
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = Phone(phone)
    
    def add(self, phone):
        self.phone = Phone(phone)

    def deletion(self, phone):
        self.phones.phones.remove(phone)

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
    
    phones = list()
    
    def __init__(self, phone):
           
        if phone in self.phones:
            print("tel in list")
        else:
            self.phones.append(phone)