import urllib.request
from bs4 import BeautifulSoup
import win32com.client
from pandas import DataFrame

class Status:
    def __init__(self):
        self.TEAM = 0
        self.POINTS_OWN = 0
        self.POINTS_OPP = 0

req = urllib.request.Request('http://www.espn.com/nba/statistics/team/_/stat/team-comparison-per-game')
data = urllib.request.urlopen(req).read()
soup = BeautifulSoup(data, 'html.parser')

teams = soup.select('#my-teams-table > div > div.mod-content > table > tr > td')

status = {'TEAM' : [],
         'POINTS_OWN' : [],'POINTS_OPP' : [],'POINTS_DIFF' : [],
'FG PCT_OWN' : [],'FG PCT_OPP' : [],
'3PT PCT_OWN' : [],'3PT PCT_OPP' : [],'3PT PCT_FT%' : [],
'REBOUND PCT_OFF' : [],'REBOUND PCT_DEF' : [],'REBOUND PCT_TOT' : [],
'TURNOVERS_OWN' : [],'TURNOVERS_OPP' : [],}

#Irregular sequences...processing table one by one.
wanted = teams[22:172]

result_list = list()

while wanted is not None:
    result_list.append(wanted[:15])
    wanted = wanted[15:]

for i,team in enumerate(teams[22:172]):
    attr = team.text
    if(len(attr) > 2):
       if(i%15 == 0):
            status['TEAM'] = attr
       elif(i%15 == 1):
            status['POINTS_OWN'] = attr
       elif (i % 15 == 2):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 3):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 4):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 5):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 6):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 7):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 8):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 9):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 10):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 11):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 12):
           status['POINTS_OWN'] = attr
       elif (i % 15 == 13):
           status['POINTS_OWN'] = attr
#Table 1

for i,team in enumerate(teams[195:344]):
    attr = team.text
    if(len(attr) > 2):
        print(attr)
#Table 2

for i,team in enumerate(teams[367:]):
    attr = team.text
    if(len(attr) > 2):
        print(attr)
#Table 3