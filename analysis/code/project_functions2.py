import pandas as pd
def load_and_process(url_or_path_to_csv_file):
    import pandas as pd
    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
        pd.read_csv(url_or_path_to_csv_file, low_memory=False)
        .dropna()
        .drop(columns=['name', 'tag'])
        .reset_index(drop=True)
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)
    value_counts = df1['rating'].value_counts()
    remove = value_counts[value_counts <= 1750].index
    df2 = (
        df1[~df1.rating.isin(remove)]
        .assign(total_games=(df1['wins'] / (df1['win_percent'] / 100)).round())
        .rename(columns={
            'region': 'Region',
            'rating': 'Rank',
            'damage_round': 'Damage/Round',
            'headshots': 'Headshots',
            'headshot_percent': 'Headshot %',
            'aces': 'Aces',
            'clutches': 'Clutches',
            'flawless': 'Flawless',
            'first_bloods': 'First Bloods',
            'kills': 'Kills',
            'deaths': 'Deaths',
            'assists': 'Assists',
            'kd_ratio': 'K/D',
            'kills_round': 'Kills/Round',
            'most_kills': 'Most Kills',
            'score_round': 'Score/Round',
            'wins': 'Wins',
            'win_percent': 'Win %',
            'agent_1': 'Most Used Agent',
            'agent_2': '2nd Most Used Agent',
            'agent_3': '3rd Most Used Agent',
            'gun1_name': 'Most Used Gun',
            'gun1_head': 'Headshots with Most Used Gun',
            'gun1_body': 'Bodyshots with Most Used Gun',
            'gun1_legs': 'Legshots with Most Usedin Gun',
            'gun1_kills': 'Kills with Most Used Gun',
            'gun2_name': '2nd Most Used Gun',
            'gun2_head': 'Headshots with 2nd Most Used Gun',
            'gun2_body': 'Bodyshots with 2nd Most Used Gun',
            'gun2_legs': 'Legshots with 2nd Most Used Gun',
            'gun2_kills': 'Kills with 2nd Most Used Gun',
            'gun3_name': '3rd Most Used Gun',
            'gun3_head': 'Headshots with 3rd Most Used Gun',
            'gun3_body': 'Bodyshots with 3rd Most Used Gun',
            'gun3_legs': 'Legshots with 3rd Most Used Gun',
            'gun3_kills': 'Kills with 3rd Most Used Gun',
            'total_games': 'Total Games Played'
        })
    )

    # return the final dataframe
    return df2