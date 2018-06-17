from wit import Wit

def getMessage():
    # the Wit access token
    access_token = "IBRA2N7KIJLX5GUCSX64G3XE4U5VYM4A"

    client = Wit(access_token)

    response = client.message("what are the odds of England vs Germany?")

    entities = response["entities"]

    intent = entities["intent"][0]["value"]

    teams = entities["team"]

    teams_list = []

    for team in teams:
        teams_list.append(team["value"])

    print(intent)
    print(teams_list)


getMessage()
