def validate_country(country):
    recognized_countries = ['USA', 'Germany', 'Australia', 'France', 'Canada']
    if country in recognized_countries:
        return True
    else:
        return False

# Test case
country = "France"
result = validate_country(country)
print(f"The country '{country}' is recognized: {result}")
