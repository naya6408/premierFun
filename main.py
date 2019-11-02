import requests as re 
import matplotlib.pyplot as plt
import seaborn as sns
import json
import pandas as pd 
from pandas.io.json import json_normalize


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
figDimensions = (8.5, 8.5)

eplTable = json_normalize(response)

columnTitles= ["position", "teamname", "wins", "losses", "draws", "goalsscored", "goalsreceived", "matchesplayed"]

print("type of the epltable is ", type(eplTable))
sns.set(style="darkgrid")
eplTable = eplTable.reindex(columns = columnTitles)
print("Repositioned table looks like: \n", eplTable)

fig,ax = plt.subplots(figsize=figDimensions)

sns_plot = sns.scatterplot(ax=ax, x='wins', y='losses',legend="brief" ,hue = 'teamname', data = eplTable)
pos = sns_plot.get_position()
sns_plot.set_position([pos.x0, pos.y0, pos.width * 0.85, pos.height])

sns_plot.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1)

plt.savefig("output.png")
plt.show()
















