import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.groupby('teacher_id')['subject_id'].unique().reset_index()
    teacher['cnt'] = teacher['subject_id'].apply(lambda x: len(x))
    return teacher[['teacher_id', 'cnt']]


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            'teacher_id': [1, 1, 1, 2, 2, 2, 2],
            'subject_id': [2, 2, 3, 1, 2, 3, 4],
            'dept_id': [3, 4, 3, 1, 1, 1, 1]
        }
    )
    print(count_unique_subjects(df))
