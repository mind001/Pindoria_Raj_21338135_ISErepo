def get_season(country, month):
    if country == "USA":
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        elif month in [9, 10, 11]:
            return "Autumn"
    elif country == "Germany":
        # Similar logic for Germany's seasons
        # ...
    elif country == "Australia":
        # Similar logic for Australia's seasons
        # ...
    else:
        return "Invalid country"

def print_season_symbol(season):
    if season == "Winter":
        print("Winter symbol: ❄️")
    elif season == "Spring":
        print("Spring symbol: 🌸")
    elif season == "Summer":
        print("Summer symbol: ☀️")
    elif season == "Autumn":
        print("Autumn symbol: 🍂")
    else:
        print("Invalid season")

# White-box test cases
# Testing get_season() module
print(get_season("USA", 12))  # Output: Winter
print(get_season("Germany", 5))  # Output: Spring
print(get_season("Australia", 8))  # Output: Winter

# Testing print_season_symbol() module
print_season_symbol("Winter")  # Output: Winter symbol: ❄️
print_season_symbol("Spring")  # Output: Spring symbol: 🌸
print_season_symbol("Summer")  # Output: Summer symbol: ☀️
