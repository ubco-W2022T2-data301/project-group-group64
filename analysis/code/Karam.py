import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv('../data/raw/val_stats.csv', low_memory=False)
          .dropna()
          .drop(columns=['name', 'tag'])
          .reset_index(drop=True)
      )
    # Method Chain 2 (Create new columns, drop others, and do processing)
    value_counts = df1['rating'].value_counts()
    remove = value_counts[value_counts <= 1750].index
    df2 = (
          df1[~df1.rating.isin(remove)]
          .assign(num_games=lambda x: (x['wins'] / (x['win_percent'] / 100)).round())
          .rename(columns={
          'rating': 'Rank',
          'kills': 'Kills',
          'deaths': 'Deaths',
          'kd_ratio': 'K/D',
          'assists': 'Assists',
          'headshots': 'Headshots',
          'headshot_percent': 'Headshot %',
          'wins': 'Wins',
          'gun1_name': 'Main_Gun',
          'region': 'Region',
          'damage_round': 'Damage/Round',
          'kills_round': 'Kills/Round',
          'score_round': 'Score/Round',
          'win_percent': 'Win %',
          'first_bloods': 'First Bloods',
          'aces': 'Aces',
          'most_kills': 'Most Kills',
          'clutches': 'Clutches',
          'flawless': 'Flawless',
          'num_games': 'Games Played',
          'gun1_head': 'Headshots with Main Gun',
          'gun1_body': 'Bodyshots with Main Gun',
          'gun1_legs': 'Legshots with Main Gun',
          'gun1_kills': 'Kills with Main Gun',
          'gun2_name': 'Secondary_Gun',
          'gun2_head': 'Headshots with Secondary Gun',
          'gun2_body': 'Bodyshots with Secondary Gun',
          'gun2_legs': 'Legshots with Secondary Gun',
          'gun2_kills': 'Kills with Secondary Gun',
          'gun3_name': 'Tertiary_Gun',
          'gun3_head': 'Headshots with Tertiary Gun',
          'gun3_body': 'Bodyshots with Tertiary Gun',
          'gun3_legs': 'Legshots with Tertiary Gun',
          'gun3_kills': 'Kills with Tertiary Gun',
          'agent_1': 'Agent 1',
          'agent_2': 'Agent 2',
          'agent_3': 'Agent 3',
          }
      )
    )

    # Make sure to return the latest dataframe

    return df2 
