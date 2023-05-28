import random

def get_temperature(city):
    # Replace this code with the actual implementation to fetch the temperature for the given city
    minimum_temperature = random.randint(-10, 5)
    maximum_temperature = random.randint(25, 40)
    mean_morning_temperature = random.randint(-5, 26)
    mean_afternoon_temperature = random.randint(15, 35)

    return {
        "minimum_temperature": minimum_temperature,
        "maximum_temperature": maximum_temperature,
        "mean_morning_temperature": mean_morning_temperature,
        "mean_afternoon_temperature": mean_afternoon_temperature
    }

# Test cases
cities = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Canberra", "Darwin", "Hobart"]

for city in cities:
    temperature = get_temperature(city)
    print(f"Temperature in {city}:")
    print(f"Possible Minimum Temperature: {temperature['minimum_temperature']} degrees Celsius")
    print(f"Possible Maximum Temperature: {temperature['maximum_temperature']} degrees Celsius")
    print(f"Mean Morning Temperature: {temperature['mean_morning_temperature']} degrees Celsius")
    print(f"Mean Afternoon Temperature: {temperature['mean_afternoon_temperature']} degrees Celsius")
