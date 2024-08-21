import pandas as pd
from datetime import datetime
import requests

url = 'https://raw.githubusercontent.com/mumoyarce96/tests/main/test.csv'
prev_df = pd.read_csv(url, index_col = False)

match_id = 12117188
dfs = []
response = requests.request("GET", f'https://api.sofascore.com/api/v1/event/{match_id}/lineups', headers={}, data = {})
#match_info = matches[matches['match_id'] == match_id].iloc[0]
#home_team = match_info['home_team']
#away_team = match_info['away_team']
if response.status_code == 200:
        home_players = response.json()['home']['players']
        away_players = response.json()['away']['players']
for i, player in enumerate(home_players):
  if 'statistics' in player.keys():
    stats = player['statistics']
    if 'minutesPlayed' in stats.keys() and stats['minutesPlayed'] >= 15:
      if 'ratingVersions' in stats.keys():
        stats.pop('ratingVersions')
      df = pd.DataFrame(stats, index = [i])
      df['player_name'] = player['player']['name']
      df['player_id'] = player['player']['id']
      df['player_position'] = player['position']
      df['home'] = True
      df['match_id'] = match_id
      #df['team'] = home_team
      dfs.append(df)

for i, player in enumerate(away_players):
  if 'statistics' in player.keys():
    stats = player['statistics']
    if 'minutesPlayed' in stats.keys() and stats['minutesPlayed'] >= 15:
      if 'ratingVersions' in stats.keys():
        stats.pop('ratingVersions')
      df = pd.DataFrame(stats, index = [i])
      df['player_name'] = player['player']['name']
      df['player_id'] = player['player']['id']
      df['player_position'] = player['position']
      df['home'] = False
      df['match_id'] = match_id
      #df['team'] = away_team
      dfs.append(df)

df = pd.concat(dfs).reset_index(drop = True)
cols = ['player_id', 'player_position', 'player_name']
for col in cols:
    first_column = df.pop(col)
    df.insert(0, col, first_column)
df = df.fillna(0)
df['datetime'] = datetime.now()
df.to_csv('test.csv', index = False)
