users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
length = 0
unique = 0
visits = {"Общее количество": length, "Уникальные посещения":unique}
length = len(users)
unique = len(set(users))
visits = {"Общее количество": length, "Уникальные посещения":unique}
print(visits)