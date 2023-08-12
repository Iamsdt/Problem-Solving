import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.title()
    users.sort_values(by='user_id', inplace=True, ascending=True)
    return users

if __name__ == "__main__":
    # Input:
    # Users table:
    # +---------+-------+
    # | user_id | name  |
    # +---------+-------+
    # | 1       | aLice |
    # | 2       | bOB   |
    # +---------+-------+

    users = pd.DataFrame({'user_id': [1, 2], 'name': ['aLice', 'bOB']})
    res = fix_names(users)
    print(res)