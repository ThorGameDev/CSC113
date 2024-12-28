# December 1, 2023

# Used for accessing the Yelp API
import requests 
# Used to get the location of the user
import geocoder
# Used to format requests to and values received from the Yelp API
import json
# Used for showing http responses status codes.
from http.client import responses as get_status
# Used to check if the API key file exists
import os

# Checks if the API key file exists
if 'API_KEY' in os.listdir():
    # Stores the API key to be used with yelp
    with open('API_KEY', 'r') as file:
        API_KEY = file.read()
else:
    # Offers to create an API key. If declined, the program quits
    print("You are missing the 'API_KEY' file necissary for this project to work.")
    print("Create one automatically? y/n")
    if input() == 'y':
        API_KEY = input("Yelp API key: ")
        with open('API_KEY', 'w') as file:
            file.write(API_KEY) 
        print("Operation Successful")
    else:
        exit()

#API header used to identify you
headers = {'Authorization': 'Bearer %s' % API_KEY}

def get_location():
    # Gets the location the user is currently at 
    location = geocoder.ip('me').city
    location_good = False

    # Repetitively asks the user if the location is good until the user confirms
    while not location_good:
        print(f"Use the location '{location}'? y/n")
        choice = input()
        if choice == 'y':
            location_good = True
        elif choice == 'n':
            location = input("New location: ")
        else:
            print("Invalid option. Reverting to default location")
            location = geocoder.ip('me').city

    return location

location = get_location()

def buisness_search():
    # Requests the user to input a search request and formats it for Yelp
    search = input("Search: ")
    params = {'term':search, 'location':location}

    # calls the API request
    url = 'https://api.yelp.com/v3/businesses/search'
    req=requests.get(url, params=params, headers=headers)

    # Checks if the response is good, otherwise, returns the status code
    if req.status_code != 200:
        print(f"{req.status_code} {get_status[req.status_code]}")
        return

    # Reads the response
    parsed = json.loads(req.text)
    businesses = parsed["businesses"]
     
    # Iterates through each response and prints it's information
    for business in businesses:
        print("Name:", business["name"])
        print("Rating:", business["rating"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
        print("ID:", business["id"])
        print("\n")
     
        # Gets the businesses reviews and displays them
        buisness_review_search(business["id"])

def buisness_review_search(id):
    # calls the API request
    url = "https://api.yelp.com/v3/businesses/"+id+"/reviews"
    req=requests.get(url, headers=headers)

    # Checks if the response is good, otherwise, returns the status code
    if req.status_code != 200:
        print(f"{req.status_code} {get_status[req.status_code]}")
        return

    parsed = json.loads(req.text)
     
    reviews = parsed["reviews"]
     
    for review in reviews:
        print("User:", review["user"]["name"], "Rating:", review["rating"], "Review:", review["text"], "\n")

def buisness_phone_search():
    # Requests the user to input a search request and formats it for Yelp
    phone = input("Phone Number: ")
    params = {'phone':phone}

    # calls the API request
    url = 'https://api.yelp.com/v3/businesses/search/phone'
    req=requests.get(url, params=params, headers=headers)

    # Checks if the response is good, otherwise, returns the status code
    if req.status_code != 200:
        print(f"{req.status_code} {get_status[req.status_code]}")
        return

    # Reads the request
    parsed = json.loads(req.text)
    businesses = parsed["businesses"]
     
    # Extracts relevant information
    for business in businesses:
        print("Name:", business["name"])
        print("Rating:", business["rating"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("ID:", business["id"])
        print("\n")
     
        buisness_review_search(business["id"])

def buisness_info_search():
    # Requests the user to input a search request and formats it for Yelp
    search = input("Search: ")
    params = {'term':search, 'location':location}

    # calls the API request
    url = 'https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=1'
    req=requests.get(url, params=params, headers=headers)

    # Checks if the response is good, otherwise, returns the status code
    if req.status_code != 200:
        print(f"{req.status_code} {get_status[req.status_code]}")
        return

    # Reads the request
    parsed = json.loads(req.text)
    businesses = parsed["businesses"]
     
    # Extracts relevant information
    for business in businesses:
        print("Name:", business["name"])
        print("Rating:", business["rating"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
        print("ID:", business["id"])
        print("\n")
     
        buisness_review_search(business["id"])

# User interface
while True:
    print("1. Business Search")
    print("2. Business Review Search")
    print("3. Business Phone Search")
    print("4. Business info Search")
    print(f"5. Change the location from {location}")
    print("6. quit")
    choice = input()
    print("\n")
    if choice == '1':
        buisness_search()
    elif choice == '2':
        buisness_review_search(id=input("ID:"))
    elif choice == '3':
        buisness_phone_search()
    elif choice == '4':
        buisness_info_search()
    elif choice == '5':
        location = get_location()
    elif choice == '6':
        exit()
