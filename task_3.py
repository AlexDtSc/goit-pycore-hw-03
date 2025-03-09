raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

import re

def normalize_phone(phone_number: str) -> str:
    # видаляємо всі символи окрім чисел та "+"
    pattern = r"\D"
    replacement = ""
    formatted_number = re.sub(pattern, replacement, phone_number)
    # перевіряємо чи рядок починається з "+"
    if not formatted_number.startswith("+"):
        # якщо відсутній міжнародний код '+38' додаємо його
        formatted_number = "+38" + formatted_number.lstrip("38")
    return formatted_number


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)