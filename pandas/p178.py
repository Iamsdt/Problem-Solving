import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by='score', ascending=False)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    return scores[['score', 'rank']]


if __name__ == "__main__":
    # Input:
    # Scores table:
    # +-------------+--------+
    # | Id          | Score  |
    # +-------------+--------+
    # | 1           | 3.50   |
    # | 2           | 3.65   |
    # | 3           | 4.00   |
    # | 4           | 3.85   |
    # | 5           | 4.00   |
    # | 6           | 3.65   |
    # +-------------+--------+
    scores = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6, 7],
                           'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65, 4.00]})
    res = order_scores(scores)
    print(res)