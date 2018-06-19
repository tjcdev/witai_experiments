from wit import Wit
import urllib2, json

def addTeam():
    url = 'https://api.wit.ai/entities/team/values'
    data = {
        'value': 'Miami Heat',
        'expressions': ['miami heat', 'the heat']
    }

    req = urllib2.Request(url)
    req.add_header('Authorization', 'Bearer IBRA2N7KIJLX5GUCSX64G3XE4U5VYM4A')
    req.add_header('Content-Type', 'application/json')
    req.get_method = lambda: 'POST'

    try:
    	response = urllib2.urlopen(req, json.dumps(data))
    except urllib2.HTTPError as e:
    	print "Error occured while updating existing entity"
    	print e.code
    	print e.read()
    	sys.exit(1)

    print "Entity correctly updated :" + response.read()


addTeam()

def getMessage():
    # the Wit access token
    access_token = "IBRA2N7KIJLX5GUCSX64G3XE4U5VYM4A"

    client = Wit(access_token)

    response = client.message("what are the odds for celtic vs rangers?")

    entities = response["entities"]

    intent = entities["intent"][0]["value"]

    teams = entities["team"]

    teams_list = []

    for team in teams:
        teams_list.append(team["value"])

    print(intent)
    print(teams_list)
