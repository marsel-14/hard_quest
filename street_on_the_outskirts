import meadow
import images
import random
import time

print('Это вы: ')
print(images.player)
time.sleep(3)
inventory = []
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

def forest():
    if 'фонарь' in inventory:
        time.sleep(3)
        print('Ты смог пройти через лес и ты вышел на поляну!')
        meadow.meadow()

    elif random.choice([1, 2, 3]) == 1:
        print('Вы в лесу...')
        time.sleep(3)
        print("Ты идёшь по тропинке, из темноты на тебя смотрят горящие глаза...")
        time.sleep(3)
        print('На тебя напали волки, это верная смерть. 💀💀')
        exit()
    else:
        print('Ты решил не ходить в лес ночью (и правильно).')
        street()

def empty_house():
    print("Вы заходите в дом, пахнет сыростью и гнилью. На полке лежит фонарь и ржавый нож. Выберите: 1 - забрать предметы и уйти или просто уйти:  ")
    answer = input()
    if answer == "1" and not ('фонарь' in inventory):
        print("Вы забираете вещи и быстро уходите.")
        inventory.append('фонарь')
        inventory.append('ржавый нож')
        street()
    elif answer == "2":
        print("Вы просто валите отсюда.")
        street()
street()
