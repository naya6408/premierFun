import requests as re 
import seaborn as sb 
import json
import pandas as pd 

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

for i in range(len(response)):
	for key,value in response[i].items():
		if(key == "teamname"):
			teamList.append(value)

print(json.dumps(response, sort_keys=True, indent=4))


df = pd.DataFrame(teamList)
print("data is:", data)
print("Data Frame containing list of teams is", df)



























