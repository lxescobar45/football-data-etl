#This component extracts data from American Football API (https://api-american-football.p.rapidapi.com)

import requests
import pandas as pd
import json


headers = {
	"X-RapidAPI-Key": "0e5908eb99msh64eed8352d2034fp1ee0a5jsnca34ecbe0ca8",
	"X-RapidAPI-Host": "api-american-football.p.rapidapi.com"
    }

#Takes in query string containing Team ID and Season Year
#Returns all games in Dataframe
def extract_games_by_team_and_season(querystring):

    url = "https://api-american-football.p.rapidapi.com/games"

    response = requests.get(url, headers=headers, params=querystring).json()

    df = pd.json_normalize(response, record_path = ['response'])

    return df

#This function sends a GET request to retrieve all NFL teams 
#Returns them in a Dataframe
def extract_NFL_teams():

    url = "https://api-american-football.p.rapidapi.com/teams"

    df = pd.DataFrame()

    teams = []
    for i in range(1,10):
        
        #Process GET requests to the URL with a different id each time
        response = requests.get(url, headers=headers, params={"id": i})

        data = response.json()
        print(data["response"])

        teams.append(data["response"])


    df = pd.DataFrame(teams)

    return df