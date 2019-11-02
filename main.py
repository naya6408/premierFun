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
figDimensions = (8.5, 6.5)

eplTable = json_normalize(response)

columnTitles= ["position", "teamname", "wins", "losses", "draws", "goalsscored", "goalsreceived", "matchesplayed"]

print("type of the epltable is ", type(eplTable))
sns.set(style="darkgrid") # adding dark theme
eplTable = eplTable.reindex(columns = columnTitles) # re grouping the columns 
print("Repositioned table looks like: \n", eplTable) # print what it looks like 

fig,ax = plt.subplots(figsize=figDimensions) #rescale the plot size

sns_plot = sns.scatterplot(ax=ax, x='wins', y='losses',legend="brief" ,hue = 'teamname', data = eplTable) # create a seaborn scatterplot
pos = sns_plot.get_position() # get current position 
sns_plot.set_position([pos.x0, pos.y0, pos.width * 0.85, pos.height]) #set new ploistion 

plt.legend(loc=1, prop={'size':7.5}) # legend location 
plt.savefig("output.png") # output into a file 
plt.show() # show the plot 
















