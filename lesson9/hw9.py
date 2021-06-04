
def main():
    def input_error(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except IndexError:
                print("Give me name and phone please")
                users_input()
            except KeyError:
                print("Enter user name")
                users_input()
            except ValueError:
                print("Enter phone number")
                users_input()
        return wrapper

    def add(user_input):
        contact_dict[user_input.split()[1]] = user_input.split()[2]
        users_input()

    def change(user_input):
        for name, phone in contact_dict.items():
            if name == user_input.split()[1]:
                contact_dict[user_input.split()[1]] = user_input.split()[2]
            else:
                print("Name not found")
        users_input()

    def get_options_handler(user_input):
        return(OPTIONS_BOT[user_input])

    def phone(user_input):

        if len(contact_dict) == 0:
            print("The dictionary is empty")
        else:
            for name, value in contact_dict.items():
                if name == user_input.split()[1]:
                    print(value)
                else:
                    print("Name and phone not found")
        users_input()

    def show_all(user_input):

        if len(contact_dict) > 0:
            for name, value in contact_dict.items():
                print(f"{name}-{value}")
        else:
            print("The dictionary is empty")
        
        users_input()

    def ext_bot(user_input):
        print("Good Bye!")

    def hello(user_input):
        print("How can I help you?")
        users_input()

    @input_error
    def users_input():
        user_input = input("Enter command:\n" )
        option_handler = get_options_handler(user_input.split()[0].casefold())
        option_handler(user_input)

    OPTIONS_BOT = {"add": add, "change": change, "phone": phone, "show":show_all, ".":ext_bot, "good":ext_bot,
                   "close":ext_bot, "exit":ext_bot, "hello":hello}

    contact_dict = {}

    print("Hi I am a BoT ClI")

    users_input()

if __name__=="__main__":
    main()