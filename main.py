import requests as re 
import seaborn as sb 
import json
import pandas as pd 

url = "https://sportdata.p.rapidapi.com/api/v1/free/soccer/standings/premier-league"

headers = {

}

response = re.get(url, headers=headers)
response = response.json()

print(json.dumps(response, sort_keys=True, indent=4))
print(type(response))
print(len(response))

data = []

for i in range(len(response)):
    for key,value in response[i].items():
        if(key != "teamname"):
            data.append([key,value])

print("data is:", data)























