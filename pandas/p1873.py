import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    def apply_bonus(row):
        if row.employee_id % 2 != 0 and str(row['name'])[0] != 'M':
            return row.salary
        return 0

    employees['bonus'] = employees.apply(apply_bonus, axis=1)
    employees.sort_values(by='employee_id', inplace=True, ascending=True)
    return employees[['employee_id', 'bonus']]


if __name__ == "__main__":
    df = pd.DataFrame({'employee_id': [2, 3, 7, 8, 9],
                       'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
                       'salary': [3000, 3800, 7400, 6100, 7700]})

    res = calculate_special_bonus(df)
    print(res)
