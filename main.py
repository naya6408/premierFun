import requests as re 
import seaborn as sb 
import json
import pandas as pd 
from pandas.io.json import json_normalize

# def compareStats(teamOne, teamTwo):

url = "https://sportdata.p.rapidapi.com/api/v1/free/soccer/standings/premier-league"

headers = {
	'x-rapidapi-host': "sportdata.p.rapidapi.com",
	'x-rapidapi-key': "8ed5762f77msh184b3093218aeddp1cd8a4jsn6c675ec1a175"
}

response = re.get(url, headers=headers)
response = response.json()

data = []
teamList = []
outputdict = {}

eplTable = json_normalize(response)

columnTitles= ["position", "teamname", "wins", "losses", "draws", "goalsscored", "goalsreceived", "matchesplayed"]

print("type of the epltable is ", type(eplTable))

eplTable = eplTable.reindex(columns = columnTitles)

print("Repositioned table looks like: \n", eplTable)
















