import requests
import pandas as pd
from json import loads

myurl = 'https://fantasy.premierleague.com/drf/bootstrap-static'
req = requests.get(myurl).json()

playerlist = (req['elements'])

data = pd.DataFrame(playerlist)

outpath = "/Users/adriankonstantinov/Documents/Projects/epl-scraper/extra/epldatapy.xlsx"

datatoexcel = pd.ExcelWriter(outpath, engine ='xlsxwriter')

data.to_excel(datatoexcel, sheet_name ="MainIndex")

datatoexcel.save()