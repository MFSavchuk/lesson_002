#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['Лев', 'Кенгуру', 'Слон', 'Обезьяна', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(1, 'Медведь')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['Петух', 'Страус', 'Жаворонок', ]
#  и выведите список на консоль

zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль

del zoo[zoo.index('Слон')]
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

print('Лев сидит в клетке №', zoo.index('Лев') + 1)
print('Жаворонок сидит в клетке №', zoo.index('Жаворонок') + 1)

# Добавил кошку между льфом и медведем

zoo.insert(1, 'Кот')
print(zoo)

# Сортируем список по алфавиту

zoo.sort()
print('Сортировка...')
print('Результат сортировки:', zoo)

# Добавляем ввод номера клетки


print('\n')
while True:
    print('Введите 1 - отдать животное')
    print('Введите 2 - отпустить животное')
    print('Введите 3 - узнать кто в какой клетке')
    print('Введите "end" для окончания игры:')
    move = input()

    if move == 'end':
        print('Игра окончена!')
        exit()

    elif move.isnumeric() == False :
        print('Введите вариант дейстивия!')
        print('\n')

    elif move == '1':
        while True:
            animal = input('Напиши любое название живтного, даже если оно известно только тебе или "q" для возвращения назад: ')
            if animal == 'q':
                print('\n')
                break
            elif animal.isalpha() == False:
                print('Введено имя (без цифр)')
                print('\n')
            else:
                zoo.append(animal)
                print('Животное ','"' ,animal,'"', 'в клетке!')
                print('Теперь в зоопарке: ', zoo)
                print('Жаль!', 'Очень много животных =( Лучше отпустить')
                print('\n')

    elif move == '2':
        print('Обитали зоопарка: ', zoo)
        while True:
            free_animal = input('Кого отпустим?? или "q" для возвращения назад: ')
            if free_animal == 'q':
                print('\n')
                break

            elif free_animal in zoo:
                del zoo[zoo.index(free_animal)]
                print(free_animal, 'на свободе!')
                print('Оставшиеся обитали зоопарка: ', zoo)
                print('\n')

            if len(zoo) == 0:
                print('В зоопарке пусто! Ты выпустил всех! Ура!!!')
                exit()

    elif move == '3':
        print('Всего клеток:', len(zoo), 'шт.')
        while True:
            number = input('Введите номер клетки или "q" для озвращения назад: ')
            if number == 'q':
                print('\n')
                break
            elif number.isnumeric() == False:
                print('Введено число или "q"!')
            elif 0 < int(number) <= len(zoo):
                number_list_zoo = int(number) - 1
                print(zoo[int(number_list_zoo)], ' сидит в клетке №', number)
            else:
                print('Неправильный номер клетки!')
