import sqlite3
import pandas as pd
import FootballAPIExtractor



#df = FootballAPIExtractor.extract_games_by_team_and_season(querystring={"team":"29", "season":"2022"})

df = FootballAPIExtractor.extract_NFL_teams()



print(df)
#print(df.iloc[0]['game.stage'])