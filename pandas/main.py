import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    data = customers.merge(orders, on='customer_id', how='left')


