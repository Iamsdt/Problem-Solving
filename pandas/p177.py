import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.sort_values(by='salary', ascending=False)
    employee.drop_duplicates(subset=['salary'], inplace=True)
    employee = employee.iloc[N - 1:N]
    return employee[['salary']]