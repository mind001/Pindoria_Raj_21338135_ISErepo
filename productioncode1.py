# Module 7: save_output_to_file (Refactored)
def save_output_to_file(country, month, season, filename):
    try:
        with open(filename, 'w') as file:
            file.write(f"Country: {country}\n")
            file.write(f"Month: {month}\n")
            file.write(f"Season: {season}\n")
        print("Output saved to file.")
    except IOError:
        print("Error occurred while saving output to file.")


# Module 8: read_input_from_file (Refactored)
def read_input_from_file(filename):
    try:
        with open(filename, 'r') as file:
            country = file.readline().strip().split(':')[1].strip()
            month = int(file.readline().strip().split(':')[1].strip())
        return country, month
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error occurred while reading input from file.")


# Module 2: validate_country (Refactored)
def validate_country(country):
    valid_countries = ['USA', 'Australia', 'India']
    if country in valid_countries:
        return True
    else:
        print("Invalid country.")
        return False


# Module 3: validate_month (Refactored)
def validate_month(month):
    if 1 <= month <= 12:
        return True
    else:
        print("Invalid month.")
        return False
