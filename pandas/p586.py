import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number')['order_number'].count()
    return pd.DataFrame(
        {
            'customer_number': [orders.idxmax()] if len(orders) > 0 else [],
        }
    )


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            'order_number': [],
            'customer_number': []
        }
    )
    print(largest_orders(df))
