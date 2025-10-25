MESSAGES = {
    ValueError: "Please provide 2 arguments: name and phone number",
    IndexError: "Please enter a name after the command. Usage: phone <name>",
    TypeError: "Invalid command format or wrong number of arguments",
}


# Decorator for exceptions
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as e:

            for e_type, msg in MESSAGES.items():
                if isinstance(e, e_type):
                    return msg
            return f"Unexpected error: {e}"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts.keys():
        contacts[name] = new_phone
        return "Contact updated"
    else:
        return "Contact was not found"


@input_error
def show_phone(args, contacts):

    name = args[0]
    if name in contacts.keys():
        return f"{contacts[name]}"
    else:
        return "Contact was not found"


@input_error
def show_all(contacts):
    return contacts


def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
