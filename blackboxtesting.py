# Module 1: find_season
def find_season(country, month):
    seasons = {
        "USA": {
            (1, 2, 3): "Winter",
            (4, 5, 6): "Spring",
            (7, 8, 9): "Summer",
            (10, 11, 12): "Autumn"
        },
        "Australia": {
            (1, 2, 12): "Summer",
            (3, 4, 5): "Autumn",
            (6, 7, 8): "Winter",
            (9, 10, 11): "Spring"
        }
    }
    
    if country in seasons:
        for season_months, season_name in seasons[country].items():
            if month in season_months:
                return season_name
    return None


# Module 2: validate_country
def validate_country(country):
    valid_countries = ["USA", "Australia", "Germany", "France"]
    return country in valid_countries


# Module 3: validate_month
def validate_month(month):
    return month in range(1, 13)


# Module 4: display_season
def display_season(season):
    season_symbols = {
        "Winter": "❄️",
        "Spring": "🌸",
        "Summer": "☀️",
        "Autumn": "🍂"
    }
    
    symbol = season_symbols.get(season)
    if symbol:
        print(f"The symbol for {season} is {symbol}")
    else:
        print("Invalid season")


# Module 5: get_input_country
def get_input_country():
    country = input("Enter a country: ")
    return country


# Module 6: get_input_month
def get_input_month():
    while True:
        try:
            month = int(input("Enter a month (1-12): "))
            if validate_month(month):
                return month
            else:
                print("Invalid month. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid month.")


# Module 7: save_output_to_file
def save_output_to_file(country, month, season, filename):
    with open(filename, "w") as file:
        file.write(f"Country: {country}\nMonth: {month}\nSeason: {season}")
    print(f"Output saved to {filename}")


# Module 8: read_input_from_file
def read_input_from_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            country = lines[0].strip().split(":")[1].strip()
            month = int(lines[1].strip().split(":")[1].strip())
            return country, month
    except FileNotFoundError:
        print("File not found.")
        return None, None


# Module 9: print_output
def print_output(country, month, season):
    print(f"Country: {country}")
    print(f"Month: {month}")
    print(f"Season: {season}")


# Test Cases

# Module 1: find_season
country = "USA"
month = 6
season = find_season(country, month)
print(f"Season for {country} in month {month} is {season}")  # Output: Season for USA in month 6 is Summer

# Module 2: validate_country
country = "Germany"
valid = validate_country(country)
print(f"Is {country} a valid country? {valid}")  # Output: Is Germany a valid country? True

# Module 3: validate_month
month = 13
valid = validate_month(month)
print(f"Is {month} a valid month? {valid}")  # Output: Is 13 a valid month? False

# Module 4: display_season
season = "Spring"
display_season(season)  # Output: The symbol for Spring is 🌸

# Module 5: get_input_country
country = get_input_country()
print(f"Input country: {country}")  # Output: Input country: <user input>

# Module 6: get_input_month
month = get_input_month()
print(f"Input month: {month}")  # Output: Input month: <user input>

# Module 7: save_output_to_file
country = "USA"
month = 6
season = "Summer"
filename = "output.txt"
save_output_to_file(country, month, season, filename)
# Output: Output saved to output.txt

# Module 8: read_input_from_file
filename = "input.txt"
country, month = read_input_from_file(filename)
print(f"Read country: {country}, month: {month}")  # Output: Read country: USA, month: 6

# Module 9: print_output
country = "USA"
month = 6
season = "Summer"
print_output(country, month, season)
# Output:
# Country: USA
# Month: 6
# Season: Summer
