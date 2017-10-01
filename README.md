# NBA_Result_Predictor
NBA score prediction system via neural network.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/HyOsori/NBA_Result_Predictor/blob/master/LICENSE) file for details

## Develop environment
Python 3.5  
Django 1.10 for data crawling server. We use csv data files for learning during preseason.  
Tensorflow 1.2  

## Role
- Data crawling : Using django and beautifulsoup, all game data are stored in csv files.
- Learning : Using tensorflow, prediction will be executed.(Precisely we will use neural network) We won't use win-lose prediction, but score-to-score prediction.

## Data source
All learning data files are crawled in 3 sources. [16-17 season only]
1. Standings : http://www.espn.com/nba/standings
2. Each team stats : http://www.espn.com/nba/team/stats/_/name/team_name/
3. Team by team comparison per game statistics : http://www.espn.com/nba/statistics/team/_/stat/team-comparison-per-game

## Contributor
**Data crawling**  
[Park Seon Ha](https://github.com/CameliaOv) : Special Thanks  
[Yu Jeongmin](https://github.com/machenity)  
[Jung Jo Hyung](https://github.com/epikjjh)  

**Learning**
