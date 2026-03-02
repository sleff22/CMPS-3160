# Simple parse of the 'games.json' file.
import os
import json
import pandas as pd

dataset = {}
if os.path.exists('games.json'):
  with open('games.json', 'r', encoding='utf-8') as fin:
    text = fin.read()
    if len(text) > 0:
      dataset = json.loads(text)


rows = []
for app in dataset:
    game = dataset[app]

    if game['price'] != 0:
       continue


    if 'English' not in game['supported_languages']:
       continue

    if game['metacritic_score'] == 0:
       continue
       


    rows.append({
        'appID': app,
        'name': game['name'],
        'release_date': game['release_date'],
        'price': game['price'],
        'supported_languages': game['supported_languages'],
        'developers': ', '.join(game['developers']),
        'publishers': ', '.join(game['publishers']),
        'categories': ', '.join(game['categories']),
        'genres': ', '.join(game['genres']),
        'tags': ', '.join(str(t) for t in game['tags']),
        'metacriticScore': game['metacritic_score']
    })

df = pd.DataFrame(rows)
df.to_csv('total_output.csv', index=False)