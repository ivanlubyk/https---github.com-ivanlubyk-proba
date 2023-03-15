
from collections import defaultdict
from datetime import datetime
from pprint import pprint


def get_birthdays_per_week(users):
    current_birthdays = defaultdict(list)
    for user in users:
        name  = user['name']
        birthday:datetime = user['birthday']
        if birthday.weekday() in (5, 6):
            current_birthdays['Monday'].append(name)
        else:
            current_birthdays[birthday.strftime("%A")].append(name)
        
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    for i in range(7):
        day = start_of_week + timedelta(days=i)
        day_name = day.strftime("%A")
        if day_name in current_birthdays:
            print(f"{day_name}: {', '.join(current_birthdays[day_name])}") 


if __name__ == "__main__":
    get_birthdays_per_week([{'name': 'Bill1', 'birthday': datetime(1999, 3, 17)},
                            {'name': 'Bill2', 'birthday': datetime(1985, 3, 19)},
                            {'name': 'Bill3', 'birthday': datetime(1990, 3, 20)},
                            {'name': 'Bill4', 'birthday': datetime(2001, 3, 21)},
                            {'name': 'Bill5', 'birthday': datetime(1995, 3, 22)},
                            {'name': 'Bill7', 'birthday': datetime(1985, 4, 19)}])
