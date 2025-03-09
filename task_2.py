def get_numbers_ticket(min: int, max: int, quantity: int):
    import random
    # перевіряємо функцію на коректність параметрів - всі 3 параметри цілі числа, min >= 1, max <= 1000
    try:
        int(min) and int(max) and int(quantity)
    except ValueError:
        print(f'Check whether {min}, {max}, {quantity} are integer digits')
    else:
            if min < 1 or max > 1000:
                 print(f"Check whether {min} is equal or bigger than 1 and {max} less or equal than 1000")
            else:
            # визначаємо максимальне та мінімальне значення діапазону чисел в лотореї
                lottery = range(min, max+1)
            # визначаємо кількість викликаних чисел у списку виведення, які при цьому мають бути унікальними
                numbers = random.sample(lottery, k = quantity)
            # сортуємо за зростанням список чисел у виведення
                numbers.sort()
                print(numbers)

get_numbers_ticket(1, 1000, 5)