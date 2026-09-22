import meadow
import images
import random
import time

print('Это вы: ')
print(images.player)
time.sleep(3)
inventory = []
# 1-ая главная функция и локация
def street():
    print(images.street_and_forest)
    print("Ты на окраине города. Моросит мелкий дождь. Твои действия: 1 - Пойти в лес (странное предложение), 2 - пойти в заброшенный дом:  ")
    answer = input()
    if answer == '1':
        forest()
    elif answer == '2':
        empty_house()
    else:
        print('Ты неправильно написал ответ!')
        street()

# Функция для второстепенной локации
def forest():
    if 'фонарь' in inventory:
        time.sleep(3)
        print('Ты смог пройти через лес и ты вышел на поляну!')
        meadow.meadow()

    elif random.choice([1, 2, 3]) == 1:
        print('Ты в лесу...')
        time.sleep(3)
        print("Ты идёшь по тропинке, из темноты на тебя смотрят горящие глаза...")
        time.sleep(3)
        print('На тебя напали волки, это верная смерть. 💀💀')
        exit()
    else:
        print('Ты решил не ходить в лес ночью (и правильно).')
        street()

# Функция для второстепенной локации
def empty_house():
    print("Ты заходишь в дом, пахнет сыростью и гнилью. На полке лежит фонарь и ржавый нож. Выбери: 1 - забрать предметы и уйти или просто уйти - 2:  ")
    answer = input()
    if answer == "1" and not ('фонарь' in inventory):
        print("Ты забираешь вещи и быстро уходишь.")
        inventory.append('фонарь')
        inventory.append('ржавый нож')
        street()
    elif answer == "2":
        print("Ты решил не нагружать себя и ушёл.")
        street()
    elif 'фонарь' in inventory:
        print('Тебе нет смысла забирать предметы, они у тебя есть.')
        street()
    else:
        print('Ты неправильно ввёл ответ.')
        empty_house()
