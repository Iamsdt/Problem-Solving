import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    data = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    names = data[data['customerId'].isna()][['name']]
    names.columns = ['Customers']
    return names


if __name__ == "__main__":
    cu = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max']})
    ords = pd.DataFrame({'customerId': [3, 1], 'id': [1, 2]})
    res = find_customers(cu, ords)
    print(res)
