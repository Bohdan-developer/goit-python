import pickle
from Class import AddressBook, Record, Name, Phone, Birthday
import os

file = "Book.bin"

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "Enter user name"  
        except ValueError:
            return "Enter phone number"
    return wrapper


@input_error
def add(user_input):
    if len(user_input.split())==5:
        name = user_input.split()[2]
        phone = user_input.split()[3]
        birthday = user_input.split()[4]
        if name not in contact_dict:
            name = Name(name)
            phone = Phone(phone)
            birthday = Birthday(birthday)
            record = Record(name=name, phone=phone, birthday=birthday)
            contact_dict.add_record(record)
            return f'Contact with name {name.value}, birthday {birthday.value} and phone {phone.value} was added'
        else:
            phone = Phone(phone)
            contact_dict[name].add_phone(phone)
            return f'Contact with name {name} add new phone {phone.value}'
    
    if len(user_input.split())==4:
        name = user_input.split()[2]
        phone = user_input.split()[3]
        
        if name not in contact_dict:
            name = Name(name)
            phone = Phone(phone)
            
            record = Record(name=name, phone=phone)
            contact_dict.add_record(record)
            return f'Contact with name {name.value} and phone {phone.value} was added'
        else:
            phone = Phone(phone)
            contact_dict[name].add_phone(phone)
            return f'Contact with name {name} add new phone {phone.value}'

@input_error
def add_bd(user_input):
    name = user_input.split()[2]
    birthday = user_input.split()[3]
    birthday = Birthday(birthday)
    if name not in contact_dict:
        return  f'Contact with name {name} is not found'
    elif contact_dict[name].birthday == None:
        contact_dict[name].editing_bd(birthday)
        return f'Contact with name {name} add birthday {contact_dict[name].birthday.value}'
    else:
        return 'Abonent already has a birthday'



@input_error
def change(user_input):
    name = user_input.split()[1]
    phone = user_input.split()[2]
    n_phone = user_input.split()[3]
    phone = Phone(phone)
    n_phone = Phone(n_phone)
    if name in contact_dict:
        contact_dict[name].editing_ph(phone,n_phone)
        return f'Contact with name {name} changed phone number {phone.value} to phone number {n_phone.value}'
    else:
        return 'Name is not found'



@input_error
def change_bd(user_input):
    name = user_input.split()[1]
    new_birthday = user_input.split()[2]
    if name in contact_dict:
        new_birthday = Birthday(new_birthday)
        contact_dict[name].editing_bd(new_birthday)
        return f'Contact with name {name} changed birthday to  {new_birthday.value}'
    else:
        return "User is not found"


@input_error
def get_options_handler(user_input):
    for command in OPTIONS_BOT:
        if user_input.startswith(command):
            return OPTIONS_BOT[command]   
    return except_key
       
    
    



@input_error
def phone(user_input):

    name = user_input.split()[1]
    ls_number = list()
    if name in contact_dict:
        for i in contact_dict[name].phones:
            ls_number.append(i.value)
        return f"Contact with {name} has such phone numbers: {', '.join(ls_number)} "
    else:
        return "User is not found" 
    



def show_all(user_input, N = None):
    if len(user_input.split()) > 2:
        try:
            N = int(user_input.split()[2])
        except:
            N = 1
    else:
        N = len(contact_dict.data)

    for element in contact_dict.iterator(N):
        print(f'Number of contacts: {len(contact_dict)}')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------')
        print(element)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------')
    return 'it\'s all'

@input_error
def find(user_input):
    name_or_phone = user_input.split()[1]
    res = contact_dict.search(name_or_phone)
    return res

def ext_bot(user_input):
    global flag_end
    flag_end = True
    with open(file, "wb") as fh:
        pickle.dump(contact_dict, fh)
    return "Good Bye!"



def hello(user_input):
    return "How can I help you?"

def helps(user_input):
    help_text = ''' Basic commands:
        1. hello                                 - Greetings
        2. good bye, close, exit, .              - Closing
        3. add contact <name> <phone> <birthday> - Crating a contact, birthday is optional 
        4. add birthday <name> <birthday         - Adding date of birth to contact
        5. show all  <N>                         - Show all abonent, N - number abonents in page
        6. phone <name>                          - Show all phone this abonent
        7. change <name> <phone> <new_phone>     - Editing a contact phone number
        8. editing <name> <new_birthday>         - Editing date of birth to contact
        9. find <str>                            - Seek all records where is finding <str>
        10. days to birthday <name>              - Number of days before the birthday
        '''
    return help_text

def days_to_bd(user_input):
    name = user_input.split()[3]

    if name in contact_dict:
        days = contact_dict[name].days_to_birthday()
        return f'Contact with name {name} to birthday {days} days'
    else:
        return "User is not found"



OPTIONS_BOT = { "add contact": add,
                "add birthday": add_bd,
                "change": change,
                "editing": change_bd,
                "find": find,
                "phone": phone, 
                "show all": show_all, 
                ".": ext_bot, 
                "good": ext_bot,
                "close": ext_bot, 
                "exit": ext_bot, 
                "hello": hello,
                "help": helps,
                "days to birthday": days_to_bd,

              }

except_key = lambda user_input: "Wrong command! Try again, please!"

flag_end = False

if __name__=="__main__":
    print("Hi I am a BoT ClI")

    contact_dict = AddressBook()
    
    if  os.path.isfile(file):
        with open(file, "rb") as fh:
            contact_dict = pickle.load(fh)
    
       


    while True:
        user_input = input("'Help command will show basic commands'\nEnter command:\n" )
        option_handler = get_options_handler(user_input.casefold())
        answer = option_handler(user_input)
        if answer:
            print(answer)
        if flag_end:
            break


    