salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
money_capital += salary
money_capital -= spend
for i in range(months-1):
    money_capital += salary
    spend = spend * (1 + increase)
    money_capital -= spend

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(abs(money_capital), 2))
