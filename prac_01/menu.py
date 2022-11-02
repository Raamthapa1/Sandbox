"""Menu"""
MENU = """
(H) - Hello
(G)oodbye
(Q)uit
"""
name = input(" Enter Name: ").title()
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
        print(MENU)
        choice = input(">>> ").upper()
    elif choice == "G":
        print(f'Goodbye {name}')
        print(MENU)
        choice = input(">>> ").upper()
    else:
        print('Invalid choice')
        print(MENU)
        choice = input(">>> ").upper()
print('Finished.')
