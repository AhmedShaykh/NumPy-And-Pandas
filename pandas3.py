import pandera as pa;
import pandas as pd;
from pandera.typing import Series;
from datetime import datetime;

class StudentSchema(pa.SchemaModel):
    Roll_No: Series[int] = pa.Field(ge=1);
    Name: Series[str] = pa.Field(nullable=False);
    Father_Name: Series[str] = pa.Field(nullable=False);
    Course: Series[str] = pa.Field(nullable=False);
    Date_Of_Admission: Series[datetime] = pa.Field(le=datetime.now());
    Fee: Series[int] = pa.Field(ge=0);

studentsData = [
    {"Roll_No": 1, "Name": "Alice", "Father_Name": "Bob", "Course": "Physics", "Date_Of_Admission": "2023-01-10", "Fee": 10000},
    {"Roll_No": 2, "Name": "Brian", "Father_Name": "Steve", "Course": "Chemistry", "Date_Of_Admission": "2023-02-12", "Fee": 11000},
    {"Roll_No": 3, "Name": "Chloe", "Father_Name": "Tim", "Course": "Biology", "Date_Of_Admission": "2023-03-14", "Fee": 12000},
    {"Roll_No": 4, "Name": "David", "Father_Name": "Rick", "Course": "Mathematics", "Date_Of_Admission": "2023-04-10", "Fee": 13000},
    {"Roll_No": 5, "Name": "Eva", "Father_Name": "John", "Course": "Computer Science", "Date_Of_Admission": "2023-11-16", "Fee": 14000},
    {"Roll_No": 6, "Name": "Frank", "Father_Name": "Tom", "Course": "Economics", "Date_Of_Admission": "2023-06-21", "Fee": 15000},
    {"Roll_No": 7, "Name": "Grace", "Father_Name": "Harry", "Course": "History", "Date_Of_Admission": "2023-07-25", "Fee": 16000},
    {"Roll_No": 8, "Name": "Henry", "Father_Name": "Charles", "Course": "Geography", "Date_Of_Admission": "2023-08-17", "Fee": 17000},
    {"Roll_No": 9, "Name": "Isabel", "Father_Name": "Oliver", "Course": "English", "Date_Of_Admission": "2023-09-10", "Fee": 18000},
    {"Roll_No": 10, "Name": "Jack", "Father_Name": "Noah", "Course": "Art", "Date_Of_Admission": "2023-10-05", "Fee": 19000}
];

studentsDf : pd.DataFrame = pd.DataFrame(studentsData);

studentsDf["Date_Of_Admission"] = pd.to_datetime(studentsDf["Date_Of_Admission"]);

validatedDf = StudentSchema.validate(studentsDf);

print(studentsDf["Date_Of_Admission"].dt.year);

print(studentsDf["Date_Of_Admission"].dt.month);

print(studentsDf["Date_Of_Admission"].dt.day);

print(studentsDf["Date_Of_Admission"].dt.weekday);

print(studentsDf["Date_Of_Admission"].dt.day_of_week);

print(studentsDf["Date_Of_Admission"].dt.hour);

print(studentsDf["Date_Of_Admission"].dt.minute);

print(studentsDf["Date_Of_Admission"].dt.second);

print(studentsDf["Date_Of_Admission"].dt.microsecond);

print(studentsDf["Date_Of_Admission"].dt.tz); # Time Zone

print(studentsDf["Date_Of_Admission"].dt.tz_localize);

print(studentsDf["Date_Of_Admission"].dt.tz_convert);

print(studentsDf["Date_Of_Admission"].dt.tz_localize(None));