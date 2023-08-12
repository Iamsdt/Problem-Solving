import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    data = employee.merge(department, how='left', left_on='departmentId', right_on='id')
    data.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'}, inplace=True)
    res = data.groupby('Department', as_index=False).apply(
        lambda x: x[x['Salary'] == x['Salary'].max()]).reset_index(drop=True)
    res = res[['Department', 'Employee', 'Salary']]
    return res



if __name__ == "__main__":
    employee = pd.DataFrame({'id': [1, 2, 3, 4, 5],
                                'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
                                'salary': [70000, 90000, 80000, 60000, 90000],
                                'departmentId': [1, 1, 2, 2, 1]})
    department = pd.DataFrame({'id': [1, 2], 'name': ['IT', 'Sales']})
    res = department_highest_salary(employee, department)
    print(res)