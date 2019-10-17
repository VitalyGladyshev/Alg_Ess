from collections import OrderedDict

organisations = {}
mean_profit = 0

try:
    number_of_orgs = int(input("Введите количество предприятий: "))
    for _ in range(number_of_orgs):
        name = input("Введите название организации: ")
        organisations[name] = float(input("Введите прибыль за четыре квартала: "))
        mean_profit += organisations[name]
except Exception:
    print("Некорректный ввод!")
    exit()

organisations_ordered = OrderedDict(sorted(organisations.items(), key=lambda x: x[1]))
print(organisations_ordered)

mean_profit /= number_of_orgs
print(f"Средняя прибыль {mean_profit:.4f}")

orgs_profit_less = [key for key, val in organisations.items() if val < mean_profit]
orgs_profit_above = [key for key, val in organisations.items() if val >= mean_profit]

print(f"Огранизации с прибылью ниже средней: {orgs_profit_less}")
print(f"Огранизации с прибылью ниже средней: {orgs_profit_above}")
