# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

for el in argv[1:]:
    if el.isdigit():
        argv[argv.index(el)] = int(el)
        # не совсем понимаю что означает данное предупреждение

_, per_hour, hours, bounty = argv

print(f'{(per_hour * hours) + bounty}')