team1_name = 'Мастера кода'
team1_num = 6
team1_score = 42
team1_time = 18000

team2_name = 'Волшебники данных'
team2_num = 6
team2_score = 42
team2_time = 18000


def teams_num(name1, num1, name2, num2):
    print('В команде "%s" участников: %d !' % (name1, num1))
    print('В команде "%s" участников: %d !' % (name2, num2))
    print('Итого сегодня в командах участников: %d и %d !' % (num1, num2))


def challenge_result(name1, score1, time1, name2, score2, time2):
    print('Команда "{name}" решила задач: {score} !'.format(name=name1, score=score1))
    print('{} решили задачи за {} с !'.format(name1, time1))
    print(f'В среднем, по {time1 / score1} секунды на задачу')
    print('\nКоманда "{name}" решила задач: {score} !'.format(name=name2, score=score2))
    print('{} решили задачи за {} с !'.format(name2, time2))
    print(f'В среднем, по {time2 / score2} секунды на задачу')
    print(f'Сегодня было решено {score1 + score2} задач, '
          f'в среднем по {(time1 + time2) / (score1 + score2)} секунды на задачу!')

    if score1 > score2 or score1 == score2 and time1 < time2:
        win = name1
    elif score1 < score2 or score1 == score2 and time1 > time2:
        win = name2
    else:
        win = 0
    print('\n\nРезультат битвы: {}'.format(f'{f'Победа команды: "{win}"' if win != 0 else 'Ничья!'}'))


teams_num(name1=team1_name, num1=team1_num, name2=team2_name, num2=team2_num)
print()
challenge_result(name1=team1_name, score1=team1_score, time1=team1_time,
                 name2=team2_name, score2=team2_score, time2=team2_time)