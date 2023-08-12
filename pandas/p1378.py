import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employees, employee_uni, on='id', how='left')
    return df[['unique_id', 'name']]


if __name__ == "__main__":
    employees = pd.DataFrame(
        {
            'id': [1, 7, 11, 90, 3],
            'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
        }
    )
    employee_uni = pd.DataFrame(
        {
            'id': [3, 11, 90],
            'unique_id': [1, 2, 3]
        }
    )
    print(replace_employee_id(employees, employee_uni))
