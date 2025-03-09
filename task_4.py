def get_upcoming_birthdays(users: dict) -> dict: 
    from datetime import datetime, timedelta 
    # визначаємо сьогоднішню дату
    today = datetime.today()
    # створюємо порожній список birthday_list, який згодом наповнимо парами значень словника 'name', 'congratulation date'
    birthday_list = []
    # для кожного елементу (словника) у списку users
    for user in users:
        # дату народження user переводимо в об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        # визначаємо дату народження user поточному році    
        birthday_this_year = datetime(year=today.year, month=birthday.month, day=birthday.day)
        # перевіряємо чи не пройшов день народження в поточному році, якщо пройшов - призначаємо день народження в наступному році
        if birthday_this_year.toordinal() - today.toordinal() < 0:
            birthday_this_year = datetime(year = birthday_this_year.year + 1, month=birthday.month, day=birthday.day)
        else: 
            birthday_this_year
        # шукаємо різницю кількості днів між датою народження в поточному році та сьогоднішньою датою
        diff = birthday_this_year.toordinal() - today.toordinal()
        # враховуємо перенесення святкування дня народження, якщо він випадає на вихідний день
        if birthday_this_year.weekday() >= 5:
           additional_days = 7 - birthday_this_year.weekday()
        else:
            additional_days = 0
        # перевіряємо чи день народження в поточному році буде протягом поточного тижня від сьогоднішньої дати
        if  diff < 0 or diff >= 7:
                birthday_list 
        else: 
            congratulation_date = birthday_this_year + timedelta(days=additional_days)    
        # додаємо у створений список словників пари 'name' , 'congratulation_date' для днів народжень, що мають святкуватися на поточному тижні      
            birthday_list.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )
    return birthday_list

users = [
    {"name": "John Doe", "birthday": "1985.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.15"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)