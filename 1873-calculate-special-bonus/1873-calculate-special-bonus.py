import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M'))
    employees['bonus'] = np.where(condition, employees['salary'], 0)
    result = employees[['employee_id', 'bonus']].sort_values(by='employee_id')
    return result