import urllib.request
from bs4 import BeautifulSoup
import win32com.client

NBA_result = [[0]*14 for i in range(30)]
team_value = 0
attr_value = 0

excel = win32com.client.Dispatch("Excel.Application")
wb = excel.Workbooks.open("C:/Users/user/Documents/NBA_Result_Predictor/Crawler/Data.xlsx")
ws = wb.ActiveSheet

req = urllib.request.Request('http://www.espn.com/nba/standings')
data = urllib.request.urlopen(req).read()
soup = BeautifulSoup(data, 'html.parser')

teams = soup.select('#main-container > div > section > div.tab-content > div > div > table > tr > td')

for team in teams:
    attr = team.text
    if attr_value == 0 and attr[-1].isdigit() == False and attr[-1] != '-':
        if(attr[0].isdigit() == True):
            NBA_result[team_value][attr_value] = attr[1:]

        else:
            NBA_result[team_value][attr_value] = attr

        attr_value += 1

    else:
            if attr.find('-') > 0:
                i = attr.find('-')
                attr = attr[0:i] + ',' + attr[i+1:]
            NBA_result[team_value][attr_value] = attr
            if attr_value != 13:
                attr_value += 1
            else:
                attr_value = 0
                team_value += 1

for x in range(30):
    for y in range(14):
        ws.Cells(x+2,y+1).Value = NBA_result[x][y]

wb.Save()
excel.Quit()
