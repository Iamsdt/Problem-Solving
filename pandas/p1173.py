import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['is_immediate'] = delivery.apply(
        lambda row: True if row['order_date'] == row['customer_pref_delivery_date'] else False, axis=1
    )
    values = delivery[delivery['is_immediate']]
    return pd.DataFrame({'immediate_percentage': [
        round((len(values) / len(delivery)) * 100, 2)
    ]})


if __name__ == "__main__":
    delivery = pd.DataFrame({
        "delivery_id": [1, 2, 3, 4, 5, 6],
        "customer_id": [1, 5, 1, 3, 4, 2],
        "order_date": ["2019-08-01", "2019-08-02", "2019-08-11", "2019-08-24", "2019-08-21", "2019-08-11"],
        "customer_pref_delivery_date": ["2019-08-02", "2019-08-02", "2019-08-11", "2019-08-26", "2019-08-22",
                                        "2019-08-13"]
    })
    res = food_delivery(delivery)
    print(res)
