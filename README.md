# Pindoria_Raj_21338135_ISErepo
Design and develop code adhering to basic modularity concepts and verify whether code is following basic modularity concepts and refactor if not

# Module 1 : find_season
The find_season function has been implemented in Module 1. It requires two parameters: month (current month) and country (name of the nation). The function stores the seasonal variations for several nations in a dictionary called seasons.
The function looks up the specified nation in the seasons dictionary first. If yes, it uses integer division and modulo operations to determine the season index depending on the month. The appropriate season for the nation and index is then retrieved from the seasons dictionary. The test case in this code has the supplied data, with the nation set to "France" and the month set to 6. For France in June, the method returns "Summer" as the appropriate season.
# Module 2 : validate_country
The validate_country function in this code compares a country input to a predefined list of recognised nations. The function returns True, indicating that the specified nation is a recognised country, if it can be located in the list. Otherwise, False is returned. The test case determines if the nation of "France" is recognised and prints the affirmative when it does.
# Module 3 : Validate_month
The validate_month method in this code accepts a month parameter and determines if it is within the acceptable range of 1 to 12. The function returns True, indicating that the month is a legitimate month, if it falls inside this range. Otherwise, False is returned. If the month 6 is genuine, the test case verifies it and reports the result as True.
# Module 4: season_display
In this module, the season_display function takes a season parameter and checks the value of the season. Depending on the season, the corresponding visual symbol is printed on the screen. In the provided test case, the season is set to "Spring," and the symbol for Spring (🌸) is printed as the output.
# Module 5 : Get_input_country 
The input function is used by the get_input_country function in this code to ask the user to provide their country name. The nation name input is then given back as a string. The user enters "France" as their country name in the sample test case, and it prints as the output.
