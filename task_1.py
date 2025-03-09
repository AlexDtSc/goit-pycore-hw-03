def get_days_from_today(date: str) -> int: 
    from datetime import datetime
    # перевіряємо чи дата введена в коректному форматі
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"date \"{date}\" is not in correct format. It should be string format like \"%Y-%m-%d\" (\"Year-Month-Day\") ")
    else:
    # перетворюємо дати з формату 'str' у формат 'datetime'
        # input_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
    # перетворюємо дати у формат кількості днів з початку ери
        input_date_in_days = date.toordinal()
        current_date_in_days = current_date.toordinal() 
    # шукаємо різницю між поточною датою та заданою датою
        diff = int(current_date_in_days - input_date_in_days)
        print(diff)
    
get_days_from_today("2025-03-")
get_days_from_today("2025-03-12")