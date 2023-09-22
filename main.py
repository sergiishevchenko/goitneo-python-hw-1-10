from datetime import datetime

from faker import Faker

fake = Faker()

users = []
for i in range(500):
    users.append(
        {
            'name': fake.name(),
            'birthday': fake.date_between_dates(
                date_start=datetime(1960,1,1),
                date_end=datetime(2010,12,31)
            )
        }
    )


def get_birthdays_per_week(users):
    result = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    today = datetime.today().date()

    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year >= today:
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                if birthday.weekday() == 0:
                    result['Monday'].append(name)
                elif birthday.weekday() == 1:
                    result['Tuesday'].append(name)
                elif birthday.weekday() == 2:
                    result['Wednesday'].append(name)
                elif birthday.weekday() == 3:
                    result['Monday'].append(name)
                elif birthday.weekday() == 4:
                    result['Thursday'].append(name)
                else:
                    result['Friday'].append(name)

    for key, value in result.items():
        if value:
            print('{}: {}'.format(key, ', '.join(value)))


if __name__ == '__main__':
    get_birthdays_per_week(users)