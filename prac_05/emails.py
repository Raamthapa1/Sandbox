def main():
    """creates ductionary, fills it with proper key and value and prints result"""
    email_and_name = {}  # empty dictionary for emails and names
    email = input("Email: ")
    while email != "":
        full_name = convert_email_to_name(email)
        question = input(f"Is your name {full_name}? (Y/n)").upper()
        if question != "Y" and question != "":
            full_name = input("Name: ")
        email_and_name[email] = full_name  # storing email as key & name as value
        email = input("email")

    for email, full_name in email_and_name.items():
        print(f"{email} {full_name}")


def convert_email_to_name(email):
    """removes @ and . from email and joins to form full name"""
    portion_email = email.split('@')
    front_email = portion_email[0]
    names = front_email.split('.')
    full_name = " ".join(names).title()
    return full_name


main()
