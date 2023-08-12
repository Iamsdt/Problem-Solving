import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(orders, company, on='com_id', how='inner')
    res = df[df['name'] == 'RED']['sales_id'].unique()
    return sales_person[~sales_person['sales_id'].isin(res)][['name']]


if __name__ == "__main__":
    sales_person_df = pd.DataFrame(
        {
            'sales_id': [1, 2, 3, 4, 5],
            'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'],
            'salary': [100000, 12000, 65000, 25000, 5000],
            'commission_rate': [6, 5, 12, 25, 10],
            'hire_date': ['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007']
        }
    )
    company_df = pd.DataFrame(
        {
            'com_id': [1, 2, 3, 4],
            'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'],
            'city': ['Boston', 'New York', 'Boston', 'Austin']
        }
    )
    orders_df = pd.DataFrame(
        {
            'order_id': [1, 2, 3, 4],
            'order_date': ['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014'],
            'com_id': [3, 4, 1, 1],
            'sales_id': [4, 5, 1, 4],
            'amount': [10000, 5000, 50000, 25000]
        }
    )
    print(sales_person(sales_person_df, company_df, orders_df))
