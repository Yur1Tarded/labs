import csv


def check_rating(row):
    if answers['Rating Score'] != '':
        if row['Rating Score'] != 'Unknown':
            if float(row['Rating Score']) > float(answers['Rating Score']):
                return True
    else:
        return True
    return False


def check_votes(row):
    if answers['Number Votes'] == '':
        return True
    elif row['Number Votes'] == 'Unknown':
        return False
    else:
        return (float(row['Number Votes']) > float(answers['Number Votes']) or answers['Number Votes'] == '')


def check_genre(row):
    answer = answers['Tags']
    if answer == '':
        return True
    series = row['Tags']
    for i in range(len(series)):
        for j in range(len(answer)):
            if series[i] == answer[j] or answer[j] == '':
                return True
    return False


def check_content(row):
    series = row['Content Warning']
    answer = answers['Content Warning']
    if answer == '':
        return True
    for i in range(len(series)):
        for j in range(len(answer)):
            if series[i] == answer[j] or answer[j] == '' or (series[i] == 'Unknown' and answer[j] == ''):
                return True
    return False


def check_misc(row):
    k = 0
    for i in ['Type', 'Episodes', 'StartYear', 'EndYear', 'Season', 'Studios']:
        if row[i] == answers[i] or answers[i] == '' or (row[i] == 'Unknown' and answers[i] == ''):
            k += 1
    if k == 6:
        return True
    return False


def check(row):
    return(check_rating(row) and check_votes(row) and check_genre(row) and check_content(row) and check_misc(row))


keys = ['Rating Score', 'Number Votes', 'Tags',
        'Content Warning', 'Type', 'Episodes',
        'StartYear', 'EndYear', 'Season', 'Studios']

queries = ['Введите минимальный рейтинг (по пятибалльной шкале, отделяя дробную часть точкой)  ',
             'Введите минимальное количество голосов ',
             'Перечислите желаемые жанры, разделяя их запятыми ',
             'Перечислите неприемлимый контент, разделяя запятыми ',
             'Выберите формат (TV, Web, Movie, etc) ',
             'Количество эпизодов ',
             'Год начала показа ',
             'Год окончания показа ',
             'Количество сезонов ',
             'Студия ']

add_question = '!!! Нажмите "ENTER", если не хотите учитывать данный критерий !!!'

values = []

for query in queries:
    print(query + '\n' + add_question)
    values.append(input())

answers = dict(zip(keys, values))


csvfile = open('anime.csv', 'r', encoding='utf-8')
db = csv.DictReader(csvfile, delimiter=",")
suggestions = []
for row in db:
    if check(row):
        suggestions.append(row)
with open('final.txt', 'w', encoding='utf-8') as file:
    for anime in suggestions:
        file.write(anime['Name'] + '\n')


print('Названия подходящих аниме перечислены в файле "final.txt".')
csvfile.close()