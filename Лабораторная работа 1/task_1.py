numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
count = len(numbers)
totalSum = 0
for i in range(len(numbers)):
    if numbers[i] == None:
     k = i
    else:
     totalSum = totalSum + numbers[i]

numbers[k] = totalSum / count
print("Измененный список:", numbers)