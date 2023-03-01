from datetime import datetime,timedelta

users = [{"name": "Daniil", "birthday": datetime(1994, 3, 3)}, {"name": "Yelizaveta", "birthday": datetime(1995, 3, 4)},
         {"name": "Yelisey", "birthday": datetime(1995, 3, 2)}, {"name": "Igor", "birthday": datetime(1994, 3, 4)},
         {"name": "Timofiy", "birthday": datetime(1993, 3, 2)}]


def get_birthdays_per_week(users):

    current_date = datetime.now()
    one_week_interval = timedelta(weeks=1)
    first_day = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    last_day = current_date + one_week_interval
    dict_for_congrats = {'Monday': [], 'Tuesday':[], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    for entry in users:

        birthday_date = entry["birthday"].replace(year = current_date.year)
        if first_day <= birthday_date <= last_day:  # Перехоплення всіх днів народжень в цьому році зі списку

            if birthday_date.weekday() == 5:        # Перевірка на суботу

                birthday_date += timedelta(days=2)  

            if birthday_date.weekday() == 6:        # Перевірка на неділю

                birthday_date += timedelta(days=1)

            if birthday_date.strftime("%A") not in dict_for_congrats: # Заповнення словника з іменинниками

                dict_for_congrats[birthday_date.strftime("%A")] = [entry["name"]]
            
            else:

                dict_for_congrats[birthday_date.strftime("%A")].append(entry["name"])

    for key, values in dict_for_congrats.items():
        
        if len(values) == 0:    # Перевірка для невідображення пустого списка
            continue

        print(f'{key}: ', end='')

        for value in values[:]: # Перебирання елементів списку в копії списка для коректного видалення елементів з нього
            
            if len(values) == 1:

                print(value)

            elif len(values) >1:

                print(value, end=", ")
            
            values.remove(value)

    return

get_birthdays_per_week(users)