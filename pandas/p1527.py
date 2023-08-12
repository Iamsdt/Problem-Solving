import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # filter based on words
    def filter_words(x):
        words = x.split()
        for word in words:
            if word.startswith('DIAB1'):
                return True
        return False
    return patients[patients['conditions'].apply(filter_words)]

# Input:
# Patients table:
# +------------+--------------+--------------+
# | patient_id | patient_name | conditions   |
# +------------+--------------+--------------+
# | 1          | Daniel       | YFEV COUGH   |
# | 2          | Alice        |              |
# | 3          | Bob          | DIAB100 MYOP |
# | 4          | George       | ACNE DIAB100 |
# | 5          | Alain        | DIAB201      |
# +------------+--------------+--------------+
if __name__ == "__main__":
    patients = pd.DataFrame({'patient_id': [1, 2, 3, 4, 5],
                             'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
                             'conditions': ['YFEV COUGH', 'SADIAB100', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']})
    res = find_patients(patients)
    print(res)