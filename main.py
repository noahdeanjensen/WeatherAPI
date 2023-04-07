
"""This program will go through and display the name of the states that 

begin with the same letter also then requests the name of a state that will

give back the abbreviation and nickname and capital state. """

# Noah Jensen
# 4/3/23
# CS 1300-01

import os
import json
import requests



def main():
    """Create a main method"""

    def same_beginings():

        """This function will break apart the lines of words and place them in 
        respective catagories."""

        # create a dictionary with four seperate lists for the seperate catagories

        dictionary_of_state = {"state": [],
                               "abbreviation": [],
                               "nickname": [],
                               "city": []}

        # copied the code to make for easier grading on different OS sytem.

        here = os.path.dirname(os.path.abspath(__file__))

        filename = os.path.join(here, 'StatesANC.txt')

        # open the file

        infile = open(filename, 'r', encoding="utf8")

        # for loop goes through each line splits then adds the values to lists

        for line in infile:
            data = line.split(",")
            dictionary_of_state["state"].append(data[0])
            dictionary_of_state["abbreviation"].append(data[1])
            dictionary_of_state["nickname"].append(data[2])
            dictionary_of_state["city"].append(data[3].strip("\n"))

        # Here we co through the city list and the state list to compare the first letters

        for city_name, state_name in zip(dictionary_of_state["city"], dictionary_of_state["state"]):
            first_letter_c = city_name[0].lower()
            first_letter_s = state_name[0].lower()
            if first_letter_c == first_letter_s:
                print(city_name, state_name)
        return dictionary_of_state


    def state_info():
        """Create a new function to get the information of the state"""

        dictionary_of_state = same_beginings()
        #get input from user

        chosen_state = input(
            "Please choose the state you want information on. ")

        #get index of the state we have chosen to select

        index = dictionary_of_state["state"].index(chosen_state)

        #print information via the index

        print("The abbrevation for the state is: ",

              dictionary_of_state["abbreviation"][index]+"\n")

        print("The nickname for the state is: ",

              dictionary_of_state["nickname"][index]+"\n")

        print("The capital for the state is: ",

              dictionary_of_state["city"][index]+"\n")

        return dictionary_of_state

    def api_weather_helper():
        """Created a function to get the weather information for the city via api"""

        dictionary_of_state = state_info()

        #print all the cities to choose from

        print(dictionary_of_state["city"])

        #get user input

        wanted_location = input(
            "Please enter the city you want to know the weather of from the list. ")

        #format the string correctly
        wanted_location.replace(" ", "%20")

        key = wanted_location

        #place key in get request to get specific city's weather

        response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" +
                                str(key) + "?unitGroup=us&key=A2VTZYV773ZSNZ8R457S6ZH3R&contentType=json")

        # create a formatted string of the Python JSON object
        text = json.dumps(response.json(), sort_keys=True, indent=4)

        print(text)

    api_weather_helper()


main()


"""Had a great time doing this program just stayed up too late doing it. 
Not super challenging dealt with a lot of syntax issues"""
