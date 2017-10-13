import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

schedule_months = "october november december january february march april may june".split(" ")
table_rows = []
for month in schedule_months:
    req = "https://www.basketball-reference.com/leagues/NBA_2017_games-{}.html".format(month)
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data, 'html.parser')
    results = soup.find_all('td', {'class' : ['left', 'right']})
    each_row = []

    for result in results:
        text = result.get_text()
        if text.find('pm') != -1 or not text:
            continue
        each_row.append(text)
        if len(each_row) == 4:
            table_rows.append(each_row)
            each_row = []

data_frame = pd.DataFrame(table_rows,columns=['Visitor Team', 'Visitor Points', 'Home Team', 'Home Points'])
data_frame.to_csv("..\\Data\\results\\game_results", index=False)