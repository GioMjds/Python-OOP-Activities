from collections import namedtuple, Counter
import datetime

today = datetime.date.today()
birthday = datetime.date(2003, 4, 5)
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

info = namedtuple("Student", ['fullName', 'birthday', 'age', 'schedule', 'totalHours'])

schedule = {
    'Monday': {
        "IT2104": "9:00 - 10:00",
        "IT2102": "10:00 - 11:00",
        "CC2103": "11:00 - 12:00",
        "IT2104": "13:00 - 14:00",
        "IT2102": "14:00 - 15:00",
        "PATHFIT3": "15:00 - 16:00"
    },
    'Tuesday': {
        "PATHFIT3": "7:00 - 8:00",
        "IT2105": "9:00 - 11:00",
        "IT2103": "11:00 - 13:00",
        "CC2104": "15:00 - 17:00",
        "CC2103": "17:00 - 19:00"
    },
    'Wednesday': {
        "IT2104": "9:00 - 10:00",
        "IT2102": "10:00 - 11:00",
        "IT2103": "13:00 - 14:00",
        "IT2105": "13:00 - 14:00",
        "CC2104": "14:00 - 15:00",
        "CC2103": "15:00 - 16:00",
        "SSP04": "16:00 - 18:00"
    },
    'Thursday': {
        "SSP04": "11:00 - 12:00",
        "IT2104": "13:00 - 15:00"
    },
    "Friday": {
        "IT2105": "9:00 - 11:00",
        "IT2102": "11:30 - 13:30",
        "CC2103": "14:00 - 15:00",
        "CC2104": "15:00 - 17:00"
    }
}

mondaySched = schedule['Monday']
tuesdaySched = schedule['Tuesday']
wednesdaySched = schedule['Wednesday']
thursdaySched = schedule['Thursday']
fridaySched = schedule['Friday']

mondayOutput = f"""
Monday Schedule:
IT 2104: {mondaySched['IT2104']}
IT 2102: {mondaySched['IT2102']}
CC 2103: {mondaySched['CC2103']}
IT 2104: {mondaySched['IT2104']}
IT 2102: {mondaySched['IT2102']}
PATHfit 3: {mondaySched['PATHFIT3']}
"""
tuesdayOutput = f"""
Tuesday Schedule:
PATHFIT 3: {tuesdaySched['PATHFIT3']}
IT 2105: {tuesdaySched['IT2105']}
IT 2103: {tuesdaySched['IT2103']}
CC 2104: {tuesdaySched['CC2104']}
CC 2103: {tuesdaySched['CC2103']}
"""
wednesdayOutput = f""" 
Wednesday Schedule: (Online Class) 
IT 2104: {wednesdaySched['IT2104']}
IT 2102: {wednesdaySched['IT2102']}
IT 2103: {wednesdaySched['IT2103']}
IT 2105: {wednesdaySched['IT2105']}
CC 2104: {wednesdaySched['CC2104']}
CC 2103: {wednesdaySched['CC2103']}
SSP 04: {wednesdaySched['SSP04']}
"""
thursdayOutput = f""" 
Thursday Schedule:
SSP 04: {thursdaySched['SSP04']}
IT 2104: {thursdaySched['IT2104']}
"""
fridayOutput = f""" 
Friday Schedule:
IT 2105: {fridaySched['IT2105']}
IT 2102: {fridaySched['IT2102']}
CC 2103: {fridaySched['CC2103']}
CC 2104: {fridaySched['CC2104']}
"""
totalHours = {
    'Monday': 5,
    'Tuesday': 8,
    'Wednesday': 8,
    'Thursday': 3,
    'Friday': 7
}

weeklyTotalHours = sum(totalHours.values())

self = info(fullName='Gio Majadas', birthday=birthday, age=age, schedule=schedule, totalHours=weeklyTotalHours)

output = f"""
Name: {self.fullName}
Birthday: {self.birthday}
Age: {self.age}
My Schedule:
{mondayOutput}
{tuesdayOutput}
{wednesdayOutput}
{thursdayOutput}
{fridayOutput}
Total hrs per week: {self.totalHours} hrs.
"""

clean_output = output.replace('{', '').replace('}', '').replace("'", '').replace(",", '').replace('.', '')
word_counts = Counter(clean_output.split())

print(output)
print("\nWord count:")
print(word_counts)