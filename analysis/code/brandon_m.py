def load_and_process(path_to_csv_file):
    
    df = (
        pd.read_csv('../data/raw/val_stats.csv', low_memory = False)
        .loc[:, ['name', 'rating', 'kills', 'deaths', 'kd_ratio', 'assists', 'headshots', 'headshot_percent', 'wins']]
        .rename(columns={'name': 'Gamertag','rating': 'Rank','kills': 'Kills','deaths': 'Deaths','kd_ratio': 'K/D_Ratio','assists': 'Assists','headshots': 'Headshots','headshot_percent': 'Headshot %','wins': 'Wins'})
        .sort_values('Rank', ascending=False)
        .loc[lambda x: ~x['Rank'].isin(['Unrated', 'Bronze 1', 'Bronze 2', 'Bronze 3', 'Silver 1', 'Silver 2', 'Silver 3'])]
        .dropna()
        .loc[lambda x: x['Gamertag'].str.match('^[a-zA-Z0-9]+')]
    )
    return df