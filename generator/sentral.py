from pandas import read_excel
from io import BytesIO

def get_student(students: list[dict], first: str, last: str) -> str:
    for student in students:
        if (student["first"] == first) and (student["last"] == last):
            return student
    
    student = {
        "first": first,
        "last": last,
        "activities": list(),
        "awards": list()
    }

    students.append(student)
    return student

def process_excel_files(activities_io: BytesIO, awards_io: BytesIO) -> list[dict]:
    students: list[dict] = list()

    activities = read_excel(activities_io)
    for i, series in activities.iterrows():
        last, first, activity = series
        student = get_student(students, first, last)
        student["activities"].append(activity)

    awards = read_excel(awards_io)
    for i, series in awards.iterrows():
        last, first, award = series
        student = get_student(students, first, last)
        student["awards"].append(award)

    return students