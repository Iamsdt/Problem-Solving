import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # this should be invalid
    # winston@leetcode?com
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    users = users[users['email'].str.match(pattern)]
    return users
