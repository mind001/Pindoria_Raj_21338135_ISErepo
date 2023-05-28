def season_display(season):
    if season == "Spring":
        print("🌸")  # Symbol for Spring
    elif season == "Summer":
        print("☀️")  # Symbol for Summer
    elif season == "Autumn":
        print("🍂")  # Symbol for Autumn
    elif season == "Winter":
        print("❄️")  # Symbol for Winter
    else:
        print("Invalid season!")

# Test case
season = "Spring"
season_display(season)
