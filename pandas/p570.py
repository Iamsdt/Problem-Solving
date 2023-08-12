import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    direct_reports_count = employee.groupby('managerId')['id'].count()
    res = direct_reports_count[direct_reports_count >= 5].index.tolist()
    return employee[employee['id'].isin(res)][['name']]
