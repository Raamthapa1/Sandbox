COlOR_NAME_TO_CODE_CODE = {
    "Alice Blue": "#f0f8ff",
    "Absolute Zero": "#0048ba",
    "Baby Blue": "#89cff0",
    "Barn Red": "#7c0a02",
    "Blond	": "#faf0be",
    "Buff": "#f0dc82",
    "Canary": "#ffff99",
    "Citron": "#9fa91f",
    "Crimson": "#dc143c",
    "Denim": "#1560bd"
}

print(COlOR_NAME_TO_CODE_CODE)
color_name = input("Please enter the color name to convert to code: ").title()
while color_name != "":
    if color_name in COlOR_NAME_TO_CODE_CODE:
        print(color_name, "is", COlOR_NAME_TO_CODE_CODE[color_name])
    else:
        print("Invalid color name")
    color_name = input("Please enter the color name to convert to code: ").title()
print("Bye.. ")

