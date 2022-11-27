 # names = ["Ada", "Alan", "Bill", "John"]
# print(" , ".join(names))
# name_to_remove = input("Who do you want to remove? ")
#
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove)
#         print(" , ".join(names))
#
#     except ValueError:
#         print("There is no such name.")
#     name_to_remove = input("Who do you want to remove? ")
# print("Thank you for deleting")
# print("*".join([len(word) for word in "one*two*three".split('*')]))

def main():
 for i in range(5):
  print(do_thing(i))
def do_thing(number):
 return number * 2 * '*'

if __name__ == '__main__':
    main()