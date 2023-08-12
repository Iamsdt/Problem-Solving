import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(id_vars=['product_id'], var_name='store', value_name='price')
    products = products.dropna()
    products.price = products.price.astype(int)
    return products


if __name__ == "__main__":
    products = pd.DataFrame({'product_id': [0, 1],
                                'store1': [95, 70],
                                'store2': [100, None],
                                'store3': [105, 80]})
    res = rearrange_products_table(products)
    print(res)