# Pindoria_Raj_21338135_ISErepo
# Seasons in Australia - Test cases Project

<img width="466" alt="ise1" src="https://github.com/mind001/Pindoria_Raj_21338135_ISErepo/assets/8244853/0ce2356f-8b56-44d5-af71-27807d877ba3">
<img width="436" alt="ise2" src="https://github.com/mind001/Pindoria_Raj_21338135_ISErepo/assets/8244853/16b7fd39-39e3-4da8-b30d-a98e5bfd42ee">


### Description

In this software project, the company aims to develop educational tools related to weather and its impact on learning. The project focuses on two specific scenarios: determining the season based on a given country name and month, and comparing a temperature reading with the average temperature of a city.

To handle the project effectively, version control using Git was employed to track changes and facilitate collaboration. Modularity principles were followed, resulting in well-defined modules with clear descriptions of their behavior, inputs, and outputs.

The production code was implemented in either Python or Java, ensuring adherence to modularity guidelines and resolving any syntax errors.

Black-box testing techniques, such as equivalence partitioning and boundary value analysis, were used to design comprehensive test cases for all modules. This approach covered a wide range of scenarios and data combinations, ensuring the software's usability and reliability.

For selected modules, white-box testing was conducted to examine the underlying structure and logic. Test cases were designed to verify the functionality and identify any potential issues.

The test cases were implemented and executed using Python or Java. Test results were analyzed, and any failures or issues were addressed by making necessary code modifications to ensure the intended functionality.

Ethical considerations and professionalism were also taken into account. The potential harmful effects of unethical behavior in using the code were discussed, and two suggestions based on ACS or IEEE-CS ethical guidelines were provided to avoid ethical and professional issues.

Overall, the project involved rigorous testing, adherence to modularity principles, version control, and ethical considerations to develop reliable and effective software tools for weather education

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
# Module 6: enter the month
The user of this module must input a month using the keyboard. With no parameters, it returns the month that was entered by the user as an integer.
# Module 7: save_output_to_file
The output (country, month, and selected season) is saved by this module to a text file. The nation, month, and season parameters are written to the designated file.
# Module 8: read_input_from_file
The input data (country and month) are read from a text file using this module. It asks for the file name as input and returns the country and month as a tuple.
# Module 9: print_output
The output (country, month, and selected season) is printed on the screen by this module. Before presenting them, it formats the country, month, and season parameters.
![image](https://github.com/mind001/Pindoria_Raj_21338135_ISErepo/assets/8244853/54d240b6-c46c-4e06-8738-936740fa2a70)

### APIs Used
[Open Weather APIs](https://openweathermap.org/)

https://openweathermap.org/current
