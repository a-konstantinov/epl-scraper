import requests
from json import loads

myurl = 'https://fantasy.premierleague.com/drf/bootstrap-static'


def TopFormPlayer():

	req = requests.get(myurl).json()

	playerlist = (req['elements'])
	MAX_playername =''
	MAX_transfers = 0
	dream_team = ''

	for p in playerlist:
		net_transfers = p['transfers_in_event'] - p['transfers_out_event']
		
		if p['in_dreamteam']:
			dream_team = 'YES'
		
		if MAX_transfers < net_transfers:
			MAX_transfers = net_transfers
			MAX_playername = p['second_name']
		
	return ('Best Pickup: ' + MAX_playername + ' Net Transfers: +' + str(MAX_transfers) + ' In Dream Team: ' + dream_team)
	