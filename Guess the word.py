import random

word_list_1 = ["кассир", "ребенок", "женщина", "мужчина", "парень", "хирург", "пекарь"]
word_list_2 = ["баобаб", "береза", "каштан", "рябина", "пальма", "акация", "сандал"]
word_list_3 = ["собака", "корова", "лошадь", "свинья", "кролик", "гепард", "суслик"]
word_list = word_list_1 + word_list_2 + word_list_3


def get_word():  # функция выдачи случчайных слов
    return random.choice(word_list)


def display_hangman_6(tries):  # функция отображение висельницы (6)
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |
                   |          
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |
                   |          
                   -
                """,
    ]
    return stages[tries]


def display_hangman_8(tries):  # функция отображение висельницы (8)
    stages = [  # финальное состояние: голова, торс, обе руки, обе ногиб обе стопы
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |    _/ \\_
                   -
                """,  #  голова, торс, обе руки, обе ноги, одная стопа
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |    _/ \\  
                   -
                """,  # голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |
                   |          
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |
                   |          
                   -
                """,
    ]
    return stages[tries]


def display_hangman_10(tries):  # функция отображение висельницы (10)
    stages = [  # финальное состояние: голова, торс, обе руки, обе ногиб обе стопы
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |    _/ \\_
                   -
                """,  #  голова, торс, обе руки, обе ноги, одная стопа
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |    _/ \\  
                   -
                """,  # голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |
                   |          
                   -
                """,
        # виселица готова
        """
                   --------
                   |      |
                   |      
                   |    
                   |
                   |          
                   -
                """,
        # начало виселенцы
        """
                   --------
                   |      
                   |      
                   |    
                   |
                   |          
                   -
                """,
        # начальное состояние
        """
                   -
                   |      
                   |    
                   |
                   |          
                   -
                """,
    ]
    return stages[tries]


def foolproof(input_word):  # функция проверки введеных букв русского алфавита
    alphabet = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    for i in input_word:
        if i not in alphabet:
            return False
    return True


def hint(word):
    podskazka = ["Первая буква " + word[0] + ", Последняя буква " + word[-1]]
    if word in word_list_1:
        podskazka.append("Это профессия")
    elif word in word_list_2:
        podskazka.append("Это расстение")
    elif word in word_list_3:
        podskazka.append("Это животное")
    print(random.choice(podskazka))


def play(word):  # функция игры
    word_completion = "_" * len(
        word
    )  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов

    print("Давайте играть в угадайку слов!")
    print("Выберете уровень сложности: 6, 8 или 10")

    while True:
        input_tries = input()
        if input_tries in ["6", "8", "10"]:
            input_tries = int(input_tries)
            break
        else:
            print("Введите 6, 8 или 10")
    tries = input_tries  # количество попыток
    if input_tries == 6:
        hangman = display_hangman_6(tries)
    elif input_tries == 8:
        hangman = display_hangman_8(tries)
    elif input_tries == 10:
        hangman = display_hangman_10(tries)
    print("У вас есть", tries, "попыток")
    print(hangman)
    print(word_completion)
    print("Введите букву или слово целиком")

    while True:

        input_word = input().upper()
        while True:  # проверка введеных букв
            if (
                input_word in guessed_letters or input_word in guessed_words
            ):  # проверка повторного ввода
                print("Это уже вводили, введите новую букву или слово")
                input_word = input().upper()
            else:
                if (
                    foolproof(input_word) == True
                ):  # проверка введени букв русского алфавита
                    if len(input_word) == 1:
                        guessed_letters.append(input_word)
                        break
                    else:
                        guessed_words.append(input_word)
                        break
                else:
                    print("Введите букву или слово на русском")
                    input_word = input().upper()

        if input_word == "ПОДСКАЗКА":
            hint(input_word)
            print("Введите букву или слово целиком")
            continue

        if input_word == word:  # проверка если угадали слово
            print("Поздравляем, вы угадали слово! Вы победили!")
            break
        elif len(input_word) > 1 and input_word != word:
            tries -= 1
            if input_tries == 6:
                hangman = display_hangman_6(tries)
            elif input_tries == 8:
                hangman = display_hangman_8(tries)
            elif input_tries == 10:
                hangman = display_hangman_10(tries)
            print("Не угадали! У вас осталось", tries, "попыток!")
            print(hangman)
            print(word_completion)
            print("Введите новую букву или слово")
            continue

        if (
            input_word in word
        ):  # проверка угаданной буквы (есть оно в слове или нет) и замена прочерка в строке
            for i in range(len(word)):
                if word[i] == input_word:
                    word_completion = (
                        word_completion[:i] + input_word + word_completion[i + 1 :]
                    )
            print("Угадали! У вас осталось", tries, "попыток!")
            print(hangman)
            print(word_completion)
            print("Введите новую букву или слово")
        else:
            tries -= 1
            if input_tries == 6:
                hangman = display_hangman_6(tries)
            elif input_tries == 8:
                hangman = display_hangman_8(tries)
            elif input_tries == 10:
                hangman = display_hangman_10(tries)
            print("Не угадали! У вас осталось", tries, "попыток!")
            print(hangman)
            print(word_completion)
            print("Введите новую букву или слово")
        if word_completion == word:  # условие победы
            print("Поздравляем, вы угадали слово! Вы победили!")
            break
        if tries == 0:  # условие поражения
            print("Вы проиграли. Загаданное слово:", word)
            break


def replay():
    while True:
        word = get_word().upper()
        play(word)
        print("Сыграем еще? (д - да/ н -нет)")
        while True:  # проверка на введение д или н
            respond = input()
            if respond not in "дн":
                print("Введите 'д' если хотите сыграть еще или 'н' чтобы завершить!!!")
            else:
                break
        if respond == "н":
            print("ВСЕГО ХОРОШЕГО")
            break
        else:
            continue


replay()
