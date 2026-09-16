import time
from images import castle
import street_on_the_outskirts
import castle_guard_and_questions

def meadow():
    print("Ты на поляне. Впереди ручей (КУПАТЬСЯ!!!) (1), рядом с ручьём - кусты (комары :( ) (2). Что выбираешь:  ")
    answer = input()
    if answer == '1':
        stream()
    elif answer == '2':
        bushes()
    else:
        print("Ошибка! Ты неправильно вписал ответ.")
        meadow()



def stream():
    print("Ты у реки. К берегу привязана лодка.")
    time.sleep(3)
    if 'вёсла' in street_on_the_outskirts.inventory:
        time.sleep(3)
        print("ВАУ! Ты переплыл реку и очутился у замка!")
        print(castle)
        castle_guard_and_questions.castle_guard_and_questions()
    else:
        print('Ты не можешь переплыть реку :( .')
        meadow()


def bushes():
    print('Ты пошарил по кустам...')
    time.sleep(3)
    print('И нашёл покрытые мхом вёсла, аккуратно закрытые травой!')
    print("Берёшь их (1) или нет (2)?")
    answer = input()
    if answer == '1':
        print('Ок, вёсла у тебя!')
        street_on_the_outskirts.inventory.append('вёсла')
        meadow()
    elif answer == '2':
        print('Ну ладно, наверно не хочешь таскать всякое барахло).')
        meadow()
