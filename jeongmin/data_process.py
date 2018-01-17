import csv
import pickle

team_stats, results = [], []

with open('../Data/teams/team_stats', 'r') as f:
    rdr = csv.reader(f);
    for line in rdr:
        team_stats.append(line)

with open('../Data/results/game_results', 'r') as f:
    rdr = csv.reader(f);
    for line in rdr:
        results.append(line)    

def find_stats_by_team(team_name):
    for row in team_stats:
        if row[1] == team_name:
            return row
    return []

x_data, y_data = [], []
count = 0

for game in results:
    if game == results[0]: continue
    A = find_stats_by_team(game[0])
    B = find_stats_by_team(game[2])
    res = []
    
    try:
        for i in range(2, len(A)):       
            res.append(float(A[i]) - float(B[i]))
    except IndexError:
        print("==IndexError==")
        print("A:", A)
        print("B:", B)
        continue
    else:
        if len(res) == 0:
            continue
        res.pop(10)
        res.pop(2)
        for i in [1, 3, 5, 9, 10]:
            res[i] *= -1
        x_data.append(res)
        count += 1
        print(count)
    
    try:
        y_data.append(list([(float(game[1]) - float(game[3])) / (float(game[1]) + float(game[3]))]))
    except ValueError:
        print("===ValueError==")
        print("game:", game)
        x_data.pop()
        
dumped = {
    "x": x_data,
    "y": y_data,
}

with open("./processed_data.txt", "wb") as f:
    pickle.dump(dumped, f)
