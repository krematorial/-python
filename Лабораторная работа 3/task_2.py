def find_common_participants(group1, group2, delimiter=','):
    participants_first_group = group1.split(delimiter)
    participants_second_group = group2.split(delimiter)

    common_participants = []

    for participant in participants_first_group:
        if participant in participants_second_group:
            common_participants.append(participant)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))