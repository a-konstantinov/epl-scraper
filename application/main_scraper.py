import requests
from json import loads

myurl = 'https://fantasy.premierleague.com/drf/bootstrap-static'
req = requests.get(myurl).json()

playerlist = (req['elements'])

gks = []   # lists for each position
defs = []
mids = []
fwds = []

def TopFormScore(pos, best_player, best_player_name, price): #calculates score
	for p in pos:
		if pos == fwds or pos == mids or pos == defs:		
			score = p['bps'] + (float(p['creativity']) + float(p['influence']) + float(p['threat'])) * (p['minutes'] / 1000)
		
		else:
			score = p['bps'] + (float(p['influence']) + p['saves']) * (p['minutes'] / 1000)

		if best_player < score and p['chance_of_playing_next_round'] != 0 and (p['now_cost'] * .1) <= price:
			best_player = score
			best_player_name = p['web_name']
			
	return best_player_name

def TopFormGoalkeeper(num): #functions for each position

	best_playername_gk =''
	best_player_gk = 0
	
	for p in playerlist:
		if p['element_type'] == 1:
			gks.append(p)
	
	pricegk = num

	best_goalie = TopFormScore(gks, best_player_gk, best_playername_gk, pricegk)
	return best_goalie						

def TopFormDefender(num):

	best_playername_def =''
	best_player_def = 0
	
	for p in playerlist:
		if p['element_type'] == 2:
			defs.append(p)
	
	pricedef = num

	best_defender = TopFormScore(defs, best_player_def, best_playername_def, pricedef)
	return best_defender

def TopFormMidfielder(num):

	best_playername_mid =''
	best_player_mid = 0
	
	for p in playerlist:
		if p['element_type'] == 3:
			mids.append(p)
	
	pricemid = num

	best_midfielder = TopFormScore(mids, best_player_mid, best_playername_mid, pricemid)
	return best_midfielder

def TopFormForward(num):

	best_playername_fwd =''
	best_player_fwd = 0
	
	for p in playerlist:
		if p['element_type'] == 4:
			fwds.append(p)
	
	pricefwd = num
	
	best_forward = TopFormScore(fwds, best_player_fwd, best_playername_fwd, pricefwd)
	return best_forward

def Differential(num):
	best_playername = ''
	best_player = 0
	
	for p in playerlist:
		if p['element_type'] == 2 or p['element_type'] == 3 or p['element_type'] == 4:		
			score = p['bps'] + (float(p['creativity']) + float(p['influence']) + float(p['threat'])) / (p['minutes'] + 1)
		
		else:
			score = p['bps'] + (float(p['influence']) + p['saves']) / (p['minutes'] + 1)
		
		price = num
		
		if best_player < score and p['chance_of_playing_next_round'] != 0 and float(p['selected_by_percent']) >= 3 and float(p['selected_by_percent']) <= 10 and (p['now_cost'] * .1) <= price:
			best_player = score
			best_playername = p['web_name']
	
	return best_playername
	
	
	
	
	

