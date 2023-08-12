import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class')['student'].count().reset_index()
    courses.sort_values(['student'], ascending=True, inplace=True)
    courses = courses[courses.student >= 5]
    return courses[['class']].reset_index(drop=True)


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
        }
    )
    print(find_classes(df))
