def save_output_to_file(country, month, season):
    with open("output.txt", "w") as file:
        file.write(f"Country: {country}\n")
        file.write(f"Month: {month}\n")
        file.write(f"Season: {season}\n")
    print("Output saved to file.")

# Test case
country = "France"
month = 7
season = "Summer"
save_output_to_file(country, month, season)
