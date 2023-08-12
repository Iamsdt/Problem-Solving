import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.sort_values(by='salary', ascending=False)
    employee.drop_duplicates(subset=['salary'], inplace=True)
    employee.rename(columns={'salary': 'SecondHighestSalary'}, inplace=True)
    # if not exits second-highest salary, return null
    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    employee = employee.iloc[1:2]
    return employee[['SecondHighestSalary']]