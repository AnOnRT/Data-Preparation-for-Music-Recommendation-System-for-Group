import json
import pandas as pd

data_path = "../Data/mpd.slice.0-999.json"
raw_json = json.loads(open(data_path).read())

playlists = raw_json["playlists"]
df = pd.json_normalize(playlists, record_path='tracks', meta=['name'])

df.to_csv("../Data/raw_data.csv")