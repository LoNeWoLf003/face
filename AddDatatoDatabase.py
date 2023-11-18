import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-97d11-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "321654":
        {
            "Name": "Sayak",
            "Major": "AIML",
            "Starting_Year": 2021,
            "total_attendance": 6,
            "Standing": "g",
            "Year": 3,
            "Last_Attendance_time": "2023-21-10 00:54:34"
        },
        "852741":
        {
            "Name": "Emily Blunt",
            "Major": "Acting",
            "Starting_Year": 2010,
            "total_attendance": 10,
            "Standing": "g",
            "Year": 2,
            "Last_Attendance_time": "2023-21-10 00:54:34"
        },
        "963852":
        {
            "Name": "Elon Musk",
            "Major": "SpaceX",
            "Starting_Year": 1992,
            "total_attendance": 2,
            "Standing": "b",
            "Year": 1,
            "Last_Attendance_time": "2023-21-10 00:54:34"
        },
    "871098":
        {
            "Name": "Koushik",
            "Major": "RCS",
            "Starting_Year": 1972,
            "total_attendance": 2,
            "Standing": "b",
            "Year": 10,
            "Last_Attendance_time": "2023-21-10 00:54:34"
        },
    "761902":
        {
            "Name": "Sanchari",
            "Major": "Botany",
            "Starting_Year": 2015,
            "total_attendance": 2,
            "Standing": "g",
            "Year": 10,
            "Last_Attendance_time": "2023-21-10 00:54:34"
        },


}


for key, value in data.items():
    ref.child(key).set(value)
