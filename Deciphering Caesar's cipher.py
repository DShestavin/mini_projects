alphabet_upper_rus = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_lower_rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alphabet_upper_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower_en = "abcdefghijklmnopqrstuvwxyz"

print("Введите текст:")
text = input()


for j in range(32):
    txt = str()
    for i in text:
        if i in alphabet_upper_rus:
            if ord(i) - j < ord("А"):
                txt += chr(ord("Я") - (j - 1 - (ord(i) - ord("А"))))
            else:
                txt += chr(ord(i) - j)
        elif i in alphabet_lower_rus:
            if ord(i) - j < ord("а"):
                txt += chr(ord("я") - (j - 1 - (ord(i) - ord("а"))))
            else:
                txt += chr(ord(i) - j)
        elif i in alphabet_upper_en:
            if ord(i) - j < ord("A"):
                txt += chr(ord("Z") - (j - 1 - (ord(i) - ord("A"))))
            else:
                txt += chr(ord(i) - j)
        elif i in alphabet_lower_en:
            if ord(i) - j < ord("a"):
                txt += chr(ord("z") - (j - 1 - (ord(i) - ord("a"))))
            else:
                txt += chr(ord(i) - j)
        else:
            txt += i

    print(txt)
