import random


def is_valid(num):
    if num.isdigit():
        if int(num) in range(1, n + 1):
            return True
    else:
        return False


def is_valid_yes_or_not(select):
    if select.lower() == "д" or select.lower() == "н":
        return True
    else:
        return False


print("Добро пожаловать в числовую угадайку")

while True:
    print("Введите диапазон загаданного числа")

    while True:
        n = input()
        if n.isdigit():
            n = int(n)
            break
        else:
            print("Введите число")

    numbers = random.randint(1, n)
    total = 0

    print("Угадайте число")
    while True:
        num = input()
        if not is_valid(num):
            print("А может быть все-таки введем целое число от 1 до ", n, "?", sep="")
        else:
            num = int(num)
            if num < numbers:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                total += 1
            elif num > numbers:
                print("Ваше число больше загаданного, попробуйте еще разок")
                total += 1
            else:
                total += 1
                print("Вы угадали, поздравляем!")
                print("Количество попыток:", total)
                break

    print("Хотите сыграть еще: д - да, н - нет")
    while True:
        select = input()
        if not is_valid_yes_or_not(select):
            print("Введите 'Д' или 'Н'")
        else:
            break
    if select.lower() == "д":
        continue
    else:
        break

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
