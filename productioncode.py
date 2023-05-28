# Module 1: find_season
def find_season(country, month):
    seasons = {
        'USA': ['Winter', 'Spring', 'Summer', 'Fall'],
        'Australia': ['Summer', 'Autumn', 'Winter', 'Spring'],
        'India': ['Winter', 'Summer', 'Monsoon', 'Autumn']
    }
    
    if country in seasons:
        season_index = (month - 1) // 3
        season = seasons[country][season_index]
        return season
    else:
        return None


# Module 2: validate_country
def validate_country(country):
    valid_countries = ['USA', 'Australia', 'India']
    return country in valid_countries


# Module 3: validate_month
def validate_month(month):
    return 1 <= month <= 12


# Module 4: display_season
def display_season(season):
    symbols = {
        'Winter': '❄️',
        'Spring': '🌸',
        'Summer': '☀️',
        'Fall': '🍂',
        'Autumn': '🍁',
        'Monsoon': '💧'
    }
    
    if season in symbols:
        print(symbols[season])
    else:
        print("Invalid season")


# Module 5: get_input_country
def get_input_country():
    return input("Enter the name of the country: ")


# Module 6: get_input_month
def get_input_month():
    return int(input("Enter the month (1-12): "))


# Module 7: save_output_to_file
def save_output_to_file(country, month, season, filename):
    with open(filename, 'w') as file:
        file.write(f"Country: {country}\n")
        file.write(f"Month: {month}\n")
        file.write(f"Season: {season}\n")
    print("Output saved to file.")


# Module 8: read_input_from_file
def read_input_from_file(filename):
    with open(filename, 'r') as file:
        country = file.readline().strip().split(':')[1].strip()
        month = int(file.readline().strip().split(':')[1].strip())
    return country, month


# Module 9: print_output
def print_output(country, month, season):
    print(f"Country: {country}")
    print(f"Month: {month}")
    print(f"Season: {season}")


# Example usage
def main():
    country = get_input_country()
    month = get_input_month()

    if validate_country(country) and validate_month(month):
        season = find_season(country, month)
        if season is not None:
            print_output(country, month, season)
            display_season(season)
            save_output_to_file(country, month, season, "output.txt")
        else:
            print("Season not found for the given country.")
    else:
        print("Invalid country or month.")


if __name__ == "__main__":
    main()
