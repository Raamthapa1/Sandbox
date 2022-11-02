total = 0
error_line_numbers = []
filename = input("filename")
in_file = open(filename, "r")
line_number = 0
for line in enumerate(in_file, 1):
    line_number += 1
    try:
        total += float(line)
    except ValueError:

        error_line_numbers.append(line_number)

in_file.close()
print(total)
print(f"The following lines have error", end="")
print(error_line_numbers)
print(",")
