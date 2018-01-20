import urllib.request
import json

token = #Enter API Token Here

summonerName = input("What is your username? ")

with urllib.request.urlopen("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + token) as url:
	data = json.loads(url.read().decode())
	accountId = str(data['accountId'])

with urllib.request.urlopen("https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + accountId + "/recent?api_key=" + token) as url:
	data2 = json.loads(url.read().decode())
	for x in range(0, 10):
		gameID = str(data2['matches'][x]['gameId'])
		print("\n\n\nGame " + str(x + 1) + ": " + gameID)
		with urllib.request.urlopen("https://na1.api.riotgames.com/lol/match/v3/matches/" + gameID + "?api_key=" + token) as url:
			data3 = json.loads(url.read().decode())
			for x in range(0, 10):
				sumID = str(data3['participantIdentities'][x]['player']['summonerId'])
				playerName = str(data3['participantIdentities'][x]['player']['summonerName'])
				with urllib.request.urlopen("https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/" + sumID + "?api_key=" + token) as url:
					data4 = json.loads(url.read().decode())
					if (len(data4) == 0):
						print(playerName + " : Unranked")
					else:
						tier = (data4[0]['tier'] + " " + data4[0]['rank'])
						print(playerName + " : " + tier)