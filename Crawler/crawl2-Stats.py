import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

nba_teams = "bos bkn cle cha gs chi dal den det hou ind lac lal mem mia mil min no ny okc orl phi phx por sac sa tor utah wsh".split(" ")

for team in nba_teams:
    req = "http://www.espn.com/nba/team/stats/_/name/{}".format(team)
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data, 'html.parser')
    players = soup.select(".tablehead > tr")

    game_stats = []
    game_head = []
    shooting_stats = []
    shooting_head = []
    dfn = game_stats
    head = game_head

    for player in players:
        if player['class'][0] == 'stathead':
            continue

        if player['class'][0] == 'total':
            dfn = shooting_stats
            head = shooting_head
            continue

        elem = player.find_all('td')
        row = [nm.text for nm in elem]

        if player['class'][0] == 'colhead':
            head += row
            continue

        dfn.append(row)

    df_game = DataFrame(game_stats, columns=game_head)
    df_shooting = DataFrame(shooting_stats, columns=shooting_head)
    df_game.to_csv("..\\Data\\players\\game\\{}_game_stats.csv".format(team), index=False)
    df_shooting.to_csv("..\\Data\\players\\shooting\\{}_shooting_stats.csv".format(team), index=False)

