money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
i = 0

while True:
    money_capital = money_capital + salary - spend
    spend = spend + (spend * increase)
    if money_capital <= 0:
        break
    i+=1

print("Количество месяцев, которое можно протянуть без долгов:", i)
