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
    name = user_input.split()[1]
    phone = user_input.split()[2]
    if name == "":
        return 'Give me name and number, please!'
    contact_dict[name] = phone
    return f'Contact with name {name} and phone {phone} was added'
    

@input_error
def change(user_input):
    name = user_input.split()[1]
    phone = user_input.split()[2]
    
    for contact in contact_dict.keys():
        if contact == name :
            contact_dict[name] = phone
        else:
            return "Name not found"
    return f'Contact with name {name} changed phone to {phone}'


@input_error
def get_options_handler(option):
    if not OPTIONS_BOT.get(option):
        return except_key
    return OPTIONS_BOT[option]



@input_error
def phone(user_input):

    name = user_input.split()[1]

    if len(contact_dict) == 0:
        return "The List contacts is empty"
    else:
        for contact in contact_dict.keys():
            if contact == name:
                return contact_dict[name]
            
    return "Name and phone not found"



def show_all(user_input):

    contact_list = list()
    if len(contact_dict) > 0:
        for name, value in contact_dict.items():
            contact_list.append(f"{name}: {value}")
    else:
        return "The dictionary is empty"
    
    return '\n'.join(contact_list)



def ext_bot(user_input):
    global flag_end
    flag_end = True
    return "Good Bye!"



def hello(user_input):
    return "How can I help you?"


OPTIONS_BOT = { "add": add,
                "change": change,
                "phone": phone, 
                "show": show_all, 
                ".": ext_bot, 
                "good": ext_bot,
                "close": ext_bot, 
                "exit": ext_bot, 
                "hello": hello
              }

except_key = lambda user_input: "Wrong command! Try again, please!"
contact_dict = dict()
flag_end = False

def main():
    print("Hi I am a BoT ClI")
    while True:
        user_input = input("Enter command:\n" )
        option = user_input.split()[0].casefold()
        if option == ".":
            break
        option_handler = get_options_handler(option)
        answer = option_handler(user_input)
        print(answer)
        if flag_end:
            break

if __name__=="__main__":
    main()