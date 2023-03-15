
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
        
        
    pprint(current_birthdays)  


if __name__ == "__main__":
    get_birthdays_per_week([{'name': 'Bill1', 'birthday': datetime(1999, 3, 17)},
                            {'name': 'Bill2', 'birthday': datetime(1985, 3, 19)},
                            {'name': 'Bill3', 'birthday': datetime(1990, 3, 20)},
                            {'name': 'Bill4', 'birthday': datetime(2001, 3, 21)},
                            {'name': 'Bill5', 'birthday': datetime(1995, 3, 22)},
                            {'name': 'Bill7', 'birthday': datetime(1985, 4, 19)}])