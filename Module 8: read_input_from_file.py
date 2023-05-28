def read_input_from_file(file_name):
    with open(file_name, "r") as file:
        country = file.readline().strip().split(": ")[1]
        month = int(file.readline().strip().split(": ")[1])
    return country, month

# Test case
input_data = read_input_from_file("input.txt")
print("Country:", input_data[0])
print("Month:", input_data[1])
