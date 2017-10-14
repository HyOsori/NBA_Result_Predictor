from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


html = urlopen("http://www.espn.com/nba/statistics/team/_/stat/team-comparison-per-game")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.find('table')
extract = table.find_all('tr',{'class':'colhead'})
rows = list(set(table) - set(extract))

table_rows = []

for row in rows:
    if row != "\n":
        each_row = []
        for cell in row:
            each_row.append(cell.get_text())
        table_rows.append(each_row)


df=pd.DataFrame(table_rows,columns=['RANK','TEAM','POINTS_OWN','POINTS_OPP','POINTS_DIFF','FG PCT_OWN','FG PCT_OPP',
'3PT PCT_OWN','3PT PCT_OPP','3PT PCT_FT%','REBOUND PCT_OFF','REBOUND PCT_DEF','REBOUND PCT_TOT','TURNOVERS_OWN','TURNOVERS_OPP'])
print(df)
df.to_csv("..\\Data\\teams\\team_stats", index=False)