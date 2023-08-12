import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities.sort_values(['product'], ascending=True, inplace=True)
    activities = activities.groupby('sell_date')['product'].unique().reset_index()
    activities['num_sold'] = activities['product'].apply(lambda x: len(x))
    activities['products'] = activities['product'].apply(lambda x: ','.join(x))
    activities.sort_values('sell_date', ascending=True, inplace=True)
    return activities[['sell_date','num_sold', 'products']]


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02',
                          '2020-05-30'],
            'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']
        }
    )
    print(categorize_products(df))
