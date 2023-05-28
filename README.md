# Pindoria_Raj_21338135_ISErepo
Design and develop code adhering to basic modularity concepts and verify whether code is following basic modularity concepts and refactor if not

# Module 1 : find_season
The find_season function has been implemented in Module 1. It requires two parameters: month (current month) and country (name of the nation). The function stores the seasonal variations for several nations in a dictionary called seasons.
The function looks up the specified nation in the seasons dictionary first. If yes, it uses integer division and modulo operations to determine the season index depending on the month. The appropriate season for the nation and index is then retrieved from the seasons dictionary. The test case in this code has the supplied data, with the nation set to "France" and the month set to 6. For France in June, the method returns "Summer" as the appropriate season.
# Module 2 : validate_country
The validate_country function in this code compares a country input to a predefined list of recognised nations. The function returns True, indicating that the specified nation is a recognised country, if it can be located in the list. Otherwise, False is returned. The test case determines if the nation of "France" is recognised and prints the affirmative when it does.
