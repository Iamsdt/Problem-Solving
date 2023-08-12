import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(['event_date'], inplace=True, ascending=True)
    activity.drop_duplicates(['player_id'], inplace=True, keep='first')
    activity.rename(columns={'event_date': 'first_login'}, inplace=True)
    return activity[['player_id', 'first_login']]


if __name__ == "__main__":
    activity = pd.DataFrame({'player_id': [1, 1, 2, 3, 3],
                             'device_id': [2, 2, 3, 1, 4],
                             'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
                             'games_played': [5, 6, 1, 0, 5]})
    res = game_analysis(activity)
    print(res)
