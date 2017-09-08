import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd

NBA_result = [[0]*14 for i in range(30)]
team_value = 0
attr_value = 0
nba_teams = "bos bkn cle cha gs chi dal den det hou ind lac lal mem mia mil min no ny okc orl phi phx por sac sa tor utah wsh".split(" ")

dfs = []
n = 0

for team in nba_teams:
    req = "http://www.espn.com/nba/team/stats/_/name/{}".format(team)
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data, 'html.parser')
    players = soup.select(".tablehead > tr")

    dfn = []

    for player in players:
        if player['class'][0] == 'stathead':
            continue

        elem = player.find_all('td')

        if player['class'][0] == 'colhead':
            head = [nm.text for nm in elem]
            continue

        if player['class'][0] == 'total':
            break

        dfn.append([nm.text for nm in elem])

    df = DataFrame(dfn, columns=head)
    df.to_csv("..\\Data\\{}_stats.csv".format(team), index=False)
    dfs.append(df)
