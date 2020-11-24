import requests

#method to call ballchasing api's GET /replays/{id} ie: EACH game's data
def apiCallByReplayId(replayId):
    url = 'https://ballchasing.com/api/replays/' + replayId
    auth = {'Authorization': '6LKHeGEtGRRIuLVdAk9xkMia5rKj3llZffKJyJYM'}
    r = requests.get(url, headers = auth)
    data =r.json()
    
    return data
#END apiCallByReplayId

#method to call ballchasing api's GET /replays/ returning list of game info
def apiCallReplays(steamID64arg, after, before):
    url = 'https://ballchasing.com/api/replays/'
    auth = {'Authorization': '6LKHeGEtGRRIuLVdAk9xkMia5rKj3llZffKJyJYM'}
    argsdict = {'uploader': steamID64,
            'created-after': after,
            'created-before': before}
    print(argsdict)
    
    #r = requests.get(url, headers = auth)
    #data =r.json()
    #print(data['blue']['players'][0]['id']['id'])
    #return data
#END apiCallByReplayId

#method to abstract out the player data for each team
def parsePlayerData(playerList):
    pass

#method to abstract out the team data
def parseTeamData(teamDict):
    pass
