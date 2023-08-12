import pandas as pd


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store = store[store['amount'] > 500]
    return store[['customer_id']].drop_duplicates().count().to_frame('rich_count')

if __name__ == "__main__":
    # Input:
    # Store table:
    # +---------+-------------+--------+
    # | bill_id | customer_id | amount |
    # +---------+-------------+--------+
    # | 6       | 1           | 549    |
    # | 8       | 1           | 834    |
    # | 4       | 2           | 394    |
    # | 11      | 3           | 657    |
    # | 13      | 3           | 257    |
    # +---------+-------------+--------+
    # Output:
    # +------------+
    # | rich_count |
    # +------------+
    # | 2          |
    # +------------+
    store = pd.DataFrame({
        "customer_id": [1, 2, 3],
        "name": ["Alice", "Bob", "Cindy"],
        "amount": [100, 600, 800]
    })
    res = count_rich_customers(store)
    print(res)