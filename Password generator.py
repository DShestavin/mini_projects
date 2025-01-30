import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
exception_characters = "il1Lo0O"

chars = ""


def is_valid_num(num):  # проверка введения положительного числа
    if num.isdigit() and int(num) > 0:
        return True
    else:
        return False


def is_valid_yes_or_not(str):  # проверка введения да или нет
    if str == "да" or str == "нет":
        return True
    else:
        return False


print("Какое количетсво паролей необходимо?")
while True:
    password_count = input()
    if is_valid_num(password_count):
        password_count = int(password_count)
        break
    else:
        print("Введите число")

print("Какая длина?")
while True:
    len_password = input()
    if is_valid_num(len_password):
        len_password = int(len_password)
        break
    else:
        print("Введите число")

print("Включать цифры? (Введите 'да' или 'нет')")
while True:
    symbols_one = input()
    if is_valid_yes_or_not(symbols_one) and symbols_one == "да":
        chars += digits
        break
    elif is_valid_yes_or_not(symbols_one) and symbols_one == "нет":
        break
    else:
        print("Введите 'да' или 'нет'")

print("Включать прописные буквы? (Введите 'да' или 'нет')")
while True:
    symbols_two = input()
    if is_valid_yes_or_not(symbols_two) and symbols_two == "да":
        chars += uppercase_letters
        break
    elif is_valid_yes_or_not(symbols_two) and symbols_two == "нет":
        break
    else:
        print("Введите 'да' или 'нет'")

print("Включать строчные буквы? (Введите 'да' или 'нет')")
while True:
    symbols_three = input()
    if is_valid_yes_or_not(symbols_three) and symbols_three == "да":
        chars += lowercase_letters
        break
    elif is_valid_yes_or_not(symbols_three) and symbols_three == "нет":
        break
    else:
        print("Введите 'да' или 'нет'")

print("Включать символы? (Введите 'да' или 'нет')")
while True:
    symbols_four = input()
    if is_valid_yes_or_not(symbols_four) and symbols_four == "да":
        chars += punctuation
        break
    elif is_valid_yes_or_not(symbols_four) and symbols_four == "нет":
        break
    else:
        print("Введите 'да' или 'нет'")

print("Исключать однозначные символы: 'il1Lo0O'? (Введите 'да' или 'нет')")
while True:
    symbols_five = input()
    if is_valid_yes_or_not(symbols_five) and symbols_five == "да":
        for i in exception_characters:
            if i in chars:
                chars = chars.replace(i, "")
        break
    elif is_valid_yes_or_not(symbols_five) and symbols_five == "нет":
        break
    else:
        print("Введите 'да' или 'нет'")

print(chars)


def generate_password(length, chars):  # функция создания пароля
    password = str()
    for _ in range(length):
        password += random.choice(chars)
    return password


for i in range(password_count):  # вывод паролей
    print(generate_password(len_password, chars))
