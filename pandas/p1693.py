import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales = daily_sales.groupby(['date_id', 'make_name'])[['lead_id', 'partner_id']].nunique().reset_index()
    daily_sales.rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'}, inplace=True)
    return daily_sales


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            'date_id': ['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-8', '2020-12-8',
                        '2020-12-7', '2020-12-7', '2020-12-7'],
            'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota', 'honda', 'honda', 'honda', 'honda',
                          'honda'],
            'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
            'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]
        }
    )
    print(daily_leads_and_partners(df))
