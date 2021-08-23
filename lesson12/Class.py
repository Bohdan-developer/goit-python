from collections import UserDict
from datetime import datetime, date
import re
import copy

corect_phone = '\d{3,}'

class AddressBook(UserDict):

    def __getstate__(self):
        atr = copy.deepcopy(self.__dict__)
        return atr
    
    def __setstate__(self, atr):
        self.__dict__ = atr

    def add_record(self, record):
        self[record.name.value] = record

    def search(self, name_or_phone):
        res = ""

        for rec in self.data.values():
            if name_or_phone in rec.name.value:
                res += "\n" + str(rec)
            num_name_or_phone = re.sub(r"[\D]", "", name_or_phone)
            if len(num_name_or_phone) > 3:
                for phone in rec.phones:
                    if num_name_or_phone in phone.value:
                        res += "\n" + str(rec)
        return res

    def iterator(self, N):
        count = 0
        self.N = N
        self.i = 0
        new_iter = self
        while self.i < len(self.data):
            x = next(new_iter)
            lst = []
            for name, rec in x.items():
                count +=1
                lst.append(
                    f'{count}. Name: {rec.name.value} ; Birthday: {rec.birthday.value if rec.birthday != None else "" }; Phone - {", ".join([phone.value for phone in rec.phones]) if rec.phones != None else "" }')
            yield '\n'.join(lst)

    def __next__(self):
        if self.i >= len(self):
            raise StopIteration
        
        lst_items = list(self.data.items())
        cuter_items = dict(lst_items[self.i: self.i + self.N])
        self.i += self.N
        return cuter_items

    def __iter__(self, N=1):
        self.i = 0
        return self


class Record():
            
    def __init__(self, name, phone=None, birthday = None):
        self.name = name
        self.birthday = birthday
        self.phones = [phone]
    
    def __str__(self):
        res = ""
        res += f"Name - {self.name.value} "
        if self.birthday:
            res += f"Birthday - {str(self.birthday.value)} "
        res += f"Phones - {', '.join([phone.value for phone in self.phones]) if len(self.phones) != 0  else ''}" 
        return res

    def add_phone(self, phone):
        self.phones.append(phone)

        
    def deletion(self, phone):
        self.phones.remove(phone)

    def editing_ph(self, phone, new_phone):
        # i = self.phones.index(phone)
        # self.phones.pop(i)
        # self.phones.insert(i, new_phone)
        for i, el in enumerate(self.phones):
            if phone.value == el.value:
                self.phones[i] = new_phone
                break
    
    def editing_bd(self, new_birthday):
        if new_birthday.value != None:
            self.birthday = new_birthday
        else:
            return "New birthday is not correct"

    def days_to_birthday(self) :
        
        now = datetime.today().date()

        if (self.birthday.value.day, self.birthday.value.month) == (29, 2):
            bd = self.birthday.value + datetime.timedelta(days=1)
        else:
            bd = self.birthday.value

        bd_that_year = bd.replace(year=now.year)
        delta = bd_that_year - now

        if delta.days <= 0:
            bd_that_year = bd_that_year.replace(year=now.year+1)
            delta = bd_that_year - now

        if (self.birthday.value.day, self.birthday.value.month) == (29, 2):
            return delta.days - 1
        return delta.days


class Filed():
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Filed):
    
    def __init__(self, name):
        self.__value = None
        self.value = name

    @property
    def name(self):
        return self.__value
    
    @name.setter
    def name(self, name):
        self.__value = name


class Phone(Filed):
    
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        new_value = re.sub(r'[^\d]', '', new_value)
        if len(new_value) > 6:
            self.__value = new_value

        else:
            print('Phone number so short')
            self.__value = None
             
class Birthday(Filed):
    
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        
        try:
            date_birthday = datetime.strptime(new_value, "%d-%m-%Y").date()
            if date_birthday >= datetime.today().date():
                print('Date from future')
                self.__value = None
            else:
                self.__value = date_birthday

        except:
            print('Date is wrong, format dd-mm-yyyy')
            self.__value = None