team1_num = 5
team1_time = 18015.2
team2_time = 18020.3
score_2 = 42
score_1 = 40
team2_num = 6
total_task = 82
time_avg = 305.2
print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Команда Мастера кода продолжила работу: {} секунды!'.format(team1_time))
print(f'Сегодня было решено {total_task} задач, в среднем по {time_avg} секунды на задачу!')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "‘Ничья!’"
print(result)
