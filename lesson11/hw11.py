from collections import UserDict
from datetime import datetime, date



class AddressBook(UserDict):
    
    data = dict()
    keys_dict = list()
    count = 0

    

    def add_record(self, record):
        self.data[f"{record.name.value}"] = record

    def iterator(self, N = None):
        self.N = N if N!=None else 10
        i_k = 1
        i_O = 1

        record_list_n = list()
        records = (i for i in self.data.values())
        for one_rec in records:
            record_list_n.append(one_rec)
            if i_k == N or i_O == len(self.data):
                yield record_list_n
                record_list_n = []
                i_O = 0
            i_k += 1
            i_O += 1


class Record:
            
    record = dict()
    
    def __init__(self, name, phone = None, birthday = None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)
        self.phones = list()
    
    def add(self, phone):
        self.phones.append(phone)

    def deletion(self, phone):
        self.phones.remove(phone)

    def editing(self, phone, new_phone):
        i = self.phones.index(phone)
        self.phones.pop(i)
        self.phones.insert(i, new_phone)

    def days_to_birthday(self) :
        
        if self.birthday != None:
            
            if datetime.today() > self.birthday.value.replace(year=date.today().year):
                return (self.birthday.value.replace(year=date.today().year + 1) - datetime.today()).days
            return (self.birthday.value.replace(year=date.today().year) - datetime.today()).days


class Filed():
    pass


class Name(Filed):
    
    def __init__(self, name):
        self.value = name


class Phone(Filed):
    
    def __init__(self, phone):
        if phone != None:

            self.__value = None
            self.value = phone


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone):
        if  "+"  in phone or "-" in phone or "("  in phone or ")"  in phone or " "  in phone:
            print( "Not correct phone number" )
        else :
            if phone.isdigit() == True:
                self.__value = phone

             
class Birthday(Filed):
    
    def __init__(self, birthday):
        if birthday != None:
            try:
                if datetime.strptime(birthday, "%Y-%m-%d") < datetime.now():
                    self.__value = datetime.strptime(birthday, "%Y-%m-%d")
                else:
                    print( "Not correct date birthday")
               
            except ValueError:
                self.__value = None
                print( "Not correct format date birthday. Date in format: yyyy-mm-dd")
       

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, birthday):
        try:
            value = datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            print("Not correct format date birthday. Date in format: yyyy-mm-dd")
        
