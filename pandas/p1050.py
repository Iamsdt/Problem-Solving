import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    actor_director = actor_director[actor_director.timestamp >= 3]
    return actor_director[['actor_id', 'director_id']].reset_index(drop=True)


# Input:
# ActorDirector table:
# +-------------+-------------+-------------+
# | actor_id    | director_id | timestamp   |
# +-------------+-------------+-------------+
# | 1           | 1           | 0           |
# | 1           | 1           | 1           |
# | 1           | 1           | 2           |
# | 1           | 2           | 3           |
# | 1           | 2           | 4           |
# | 2           | 1           | 5           |
# | 2           | 1           | 6           |
# +-------------+-------------+-------------+

if __name__ == "__main__":
    df = pd.DataFrame(
        {
            'actor_id': [1, 1, 1, 1, 1, 2, 2],
            'director_id': [1, 1, 1, 2, 2, 1, 1],
            'timestamp': [0, 1, 2, 3, 4, 5, 6]
        }
    )
    print(actors_and_directors(df))