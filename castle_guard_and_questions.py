def castle_guard_and_questions():
    print('Твоя финальная локация - замок 🏰!!! :о')
    print('Ты идёшь к воротам замка. Но дорогу тебе преграждает стражник! Он говорит, что ты почему-то должен отгадывать какие-то загадки. Он говорит первую загадку...')
    print('Первая загадка: Что громче всего орёт утром в понедельник?')
    answer = input('Твой ответ:  ').strip().lower()
    if answer == "будильник":
        print('Верный ответ! Следующая загадка -> Что всегда заканчивается в самый нужный момент (связано с частями телефона) ?')
        answer = input('Твой ответ:  ').strip().lower()
    else:
        print('Неправильно! Хочешь пройти ещё раз (1) или сдаёшься (2)?')
        answer_2 = input()
        if answer_2 == '1':
            castle_guard_and_questions()
        elif answer_2 == '2':
            print("Ну ладно, желаю тебе удачи в следующий раз!")
            exit()
        else:
            print('Не понял тебя. Думаю, что ты хочешь пройти ещё раз.')
            castle_guard_and_questions()
    if answer == 'батарея':
        print('Хорош! Уже 2 загадки подряд! Следующая загадка -> Что лежит в портфеле и весит как кирпич, но по факту просто сборник ненужной инфы?')
        answer = input('Твой ответ:   ').strip().lower()
    else:
        print('Неправильно! Хочешь пройти ещё раз (1) или сдаёшься (2)?')
        answer_2 = input()
        if answer_2 == '1':
            castle_guard_and_questions()
        elif answer_2 == '2':
            print("Ну ладно, желаю тебе удачи в следующий раз!")
            exit()
        else:
            print('Не понял тебя. Думаю, что ты хочешь пройти ещё раз.')
            castle_guard_and_questions()
        exit()
    if answer == 'учебник':
        print("И опять правильно!")
        print('Что все обещают сделать днём или вечером, а делают в 23:59?')
        answer = input('Твой ответ:   ').strip().lower()
    else:
        print('Неправильно! Хочешь пройти ещё раз (1) или сдаёшься (2)?')
        answer_2 = input()
        if answer_2 == '1':
            castle_guard_and_questions()
        elif answer_2 == '2':
            print("Ну ладно, желаю тебе удачи в следующий раз!")
            exit()
        else:
            print('Не понял тебя. Думаю, что ты хочешь пройти ещё раз.')
            castle_guard_and_questions()
    if answer == 'домашка':
        print('Правильно! 4 вопроса подряд!')
        print('Когда это издаёт звук, значит: «ТЫ ОПОЗДАЛ, ЕСЛИ ТЫ НЕ В КЛАССЕ!!!» Что это?')
        answer = input('Твой ответ:   ').strip().lower()
    else:
        print('Неправильно! Хочешь пройти ещё раз (1) или сдаёшься (2)?')
        answer_2 = input()
        if answer_2 == '1':
            castle_guard_and_questions()
        elif answer_2 == '2':
            print("Ну ладно, желаю тебе удачи в следующий раз!")
            exit()
        else:
            print('Не понял тебя. Думаю, что ты хочешь пройти ещё раз.')
            castle_guard_and_questions()
    if answer == 'звонок':
        print('ТЫ УГАДАЛ ВСЕ ЗАГАДКИ!!! ТЫ ПРОШЁЛ В ЗАМОК И ВЫИГРАЛ КВЕСТ!!! 🎉🎉🎊🎊🥳🥳')
        exit()
    else:
        print('Неправильно! Хочешь пройти ещё раз (1) или сдаёшься (2)?')
        answer_2 = input()
        if answer_2 == '1':
            castle_guard_and_questions()
        elif answer_2 == '2':
            print("Ну ладно, желаю тебе удачи в следующий раз!")
            exit()
        else:
            print('Не понял тебя. Думаю, что ты хочешь пройти ещё раз.')
            castle_guard_and_questions()
