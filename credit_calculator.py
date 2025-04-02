import math
import argparse

# iмпортуємо модулі для математики та обробки аргументів командного рядка

# створюємо парсер для аргументів
parser = argparse.ArgumentParser(description="Кредитний калькулятор")
parser.add_argument("--type", choices=["annuity", "diff"], help="Тип виплати")
parser.add_argument("--payment", type=float, help="Сума щомісячного платежу")
parser.add_argument("--principal", type=float, help="Основна сума кредиту")
parser.add_argument("--periods", type=int, help="Кількість місяців")
parser.add_argument("--interest", type=float, help="Процентна ставка")
args = parser.parse_args()

# збираємо параметри в список для перевірки
params = [args.payment, args.principal, args.periods, args.interest]

# перевірка на валідність параметрів
if args.type not in ["annuity", "diff"] or args.interest is None:
    print("Incorrect parameters")
    exit()
if any(i is not None and i < 0 for i in params if isinstance(i, (int, float))):
    print("Incorrect parameters")
    exit()

# розрахунок номінальної місячної процентної ставки
# interest подається як річна, тому ділимо на 12 * 100
i = args.interest / (12 * 100)

# функція для обчислення переплати

def overpayment(total, principal):
    return int(total - principal)

# логіка для диференційованих платежів
if args.type == "diff":
    # не допускається параметр payment для диференційованих платежів
    if args.payment is not None or args.principal is None or args.periods is None:
        print("Incorrect parameters")
        exit()
    total = 0
    for m in range(1, args.periods + 1):
        # формула для диференційованого платежу
        d = math.ceil(args.principal / args.periods + i * (args.principal - (args.principal * (m - 1) / args.periods)))
        total += d
        print(f"Month {m}: payment is {d}")
    print(f"\nOverpayment = {overpayment(total, args.principal)}")

# логіка для ануїтетних платежів
elif args.type == "annuity":
    # коли відомі сума кредиту і щомісячний платіж, шукаємо кількість місяців
    if args.principal is not None and args.payment is not None and args.periods is None:
        n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
        years, months = divmod(n, 12)
        y_str = f"{years} year{'s' if years > 1 else ''}" if years else ""
        m_str = f"{months} month{'s' if months > 1 else ''}" if months else ""
        and_str = " and " if years and months else ""
        print(f"It will take {y_str}{and_str}{m_str} to repay this loan!")
        print(f"Overpayment = {overpayment(n * args.payment, args.principal)}")

    # коли відомі сума кредиту і період, шукаємо ануїтетний платіж
    elif args.principal is not None and args.periods is not None and args.payment is None:
        a = math.ceil(args.principal * i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1))
        print(f"Your annuity payment = {a}!")
        print(f"Overpayment = {overpayment(a * args.periods, args.principal)}")

    # коли відомі ануїтетний платіж і період, шукаємо основну суму кредиту
    elif args.payment is not None and args.periods is not None and args.principal is None:
        p = args.payment / (i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1))
        print(f"Your loan principal = {int(p)}!")
        print(f"Overpayment = {overpayment(args.payment * args.periods, p)}")

    # якщо параметри не валідні
    else:
        print("Incorrect parameters")
