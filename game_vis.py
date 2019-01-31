import random

MAX_ERRORS = 9


def print_users_word(arg):
    print(''.join(arg))


secret_word_masiv = ['андрей', 'мама', 'папа', 'автострада', 'бензин', 'инопланетянин', 'самолет',
                     'библиотека', 'шайба', 'олимпиада']

new_game = 'y'

user_name = input('введите имя: ')

print(user_name, ', правила игры просты: \n Нужно угадать загаданное услово. \n У тебя есть', MAX_ERRORS,
      ' попыток!!!\n')

# HW1 - Сделать возможность повтороной игры
while new_game in ('y', 'yes', 'д', 'да'):

    secret_word = random.choice(secret_word_masiv)
    users_word = ['*'] * len(secret_word)
    errors_count = 0
    print_users_word(users_word)

    while errors_count < MAX_ERRORS:

        letter = input('введите букву: ').lower()
        # HW2 Добавлена проверка на русские буквы
        if len(letter) != 1 \
                or not letter.isalpha() \
                or 1072 > ord(letter) \
                or (ord(letter) < 1103 and ord(letter) == 1105):
            continue
        if letter in secret_word:
            for idx, char in enumerate(secret_word):
                if char == letter:
                    users_word[idx] = letter
            if '*' not in users_word:
                print('вы выиграли!!!')
                print('\t\t\tбыло загадано слово:', secret_word)
                break
        else:
            errors_count += 1
            print('\tошибок допущено:', errors_count)
            if errors_count == MAX_ERRORS:
                print('\t\tвы проиграли :(')
                break

        print_users_word(users_word)
    # HOMEWORK1 - Сделать возможность повтороной игры
    new_game = input('Сыграем снова? (д/н) ').lower()

print('\n', user_name, ', пока!')
