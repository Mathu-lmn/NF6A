import requests
import json
import cv2
import sys
import numpy as np

response = requests.get('https://randomuser.me/api/?results=10')
repos = json.loads(response.text)

def display_user_info():
    for i in range(len(repos['results'])):
        print(f"{repos['results'][i]['name']['first']} {repos['results'][i]['name']['last']} \tGender : {repos['results'][i]['gender']} \tAge : {repos['results'][i]['dob']['age']} \tBirthdate :{repos['results'][i]['dob']['date']}")
        print(f"{repos['results'][i]['location']['street']['number']} {repos['results'][i]['location']['street']['name']} {repos['results'][i]['location']['city']} {repos['results'][i]['location']['state']} {repos['results'][i]['location']['country']} ")
        print(f"Email : {repos['results'][i]['email']} \tPhone : {repos['results'][i]['phone']}")
        print("")

display_user_info()

def get_oldest_user():
    oldest_user = 0
    for i in range(len(repos['results'])):
        if int(repos['results'][i]['dob']['age']) > oldest_user:
            oldest_user = int(repos['results'][i]['dob']['age'])
            oldest_user_name = f"{repos['results'][i]['name']['first']} {repos['results'][i]['name']['last']}"
    print(f"The oldest user is {oldest_user_name} with {oldest_user} years old")

# get_oldest_user()

def male_percentage():
    male_count = 0
    for i in range(len(repos['results'])):
        if repos['results'][i]['gender'] == "male":
            male_count += 1
    male_percentage = 100*(male_count / len(repos['results']))
    print(f"There are {male_percentage} % of males in the results")

male_percentage()

def get_list_countries():
    countries = []
    for i in range(len(repos['results'])):
        if repos['results'][i]['location']['country'] in countries:
            continue
        else : 
            countries.append(str(repos['results'][i]['location']['country']))
    print("Countries in the results : ",countries)

get_list_countries()

def younger_user_picture():
    youngest_user = 0
    youngest_user_name = ""
    for i in range(len(repos['results'])):
        if int(repos['results'][i]['dob']['age']) > youngest_user:
            youngest_user = int(repos['results'][i]['dob']['age'])
            youngest_user_name = f"{repos['results'][i]['name']['first']} {repos['results'][i]['name']['last']}"
    print(f"The youngest user is {youngest_user_name} with {youngest_user} years old")
    url = repos['results'][i]['picture']['large']
    response = requests.get(url)
    img = cv2.imdecode(np.frombuffer(response.content, np.uint8), -1)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

younger_user_picture()