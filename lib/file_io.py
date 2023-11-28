def write_file(file_name, file_content):
    file_name_with_extension = file_name + ".txt"
    with open(file_name_with_extension, "w") as file:
        file.write(file_content)

def append_to_file(file_name, append_content):
    file_name_with_extension = file_name + ".txt"
    with open(file_name_with_extension, "a") as file:
        file.write("\n" + append_content)

def read_file(file_name):
    file_name_with_extension = file_name + ".txt"
    with open(file_name_with_extension, "r") as file:
        content = file.read()
    return content

# Example usage:
write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_to_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

result = read_file(file_name="logfile")
print(result)

# Output:
# Log 1: 5 bananas added
# Log 2: 3 bananas subtracted