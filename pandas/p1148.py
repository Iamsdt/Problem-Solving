import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views.author_id == views.viewer_id]
    views = views.drop_duplicates(['author_id'])
    views.sort_values(by='author_id', inplace=True, ascending=True)
    views.rename(columns={'author_id': 'id'}, inplace=True)
    return views[['id']].reset_index(drop=True)


if __name__ == "__main__":
    views = pd.DataFrame({'article_id': [1, 1, 2, 2, 4, 3, 3],
                          'author_id': [3, 3, 7, 7, 7, 4, 4],
                          'viewer_id': [5, 6, 7, 6, 1, 4, 4],
                          'date': ['2018-01-01', '2018-01-01', '2018-01-01',
                                   '2018-01-02', '2018-01-02', '2018-01-03', '2018-01-03']})
    res = article_views(views)
    print(res)
