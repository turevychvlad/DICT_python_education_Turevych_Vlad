class CoffeeMachine:
    def __init__(self):
        # Початковий стан кавомашини
        self.water = 400  # мл води
        self.milk = 540  # мл молока
        self.beans = 120  # грам кавових зерен
        self.cups = 9  # кількість одноразових стаканчиків
        self.money = 550  # гроші у грн

    def print_status(self):
        # Вивід поточного стану кавомашини
        print("\nThe coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.beans} g of coffee beans")
        print(f"{self.cups} disposable cups")
        print(f"{self.money} of money\n")

    def has_enough_resources(self, water_needed, milk_needed, beans_needed, cups_needed):
        # Перевірка наявності інгредієнтів
        try:
            if self.water < water_needed:
                print("Sorry, not enough water!")
                return False
            if self.milk < milk_needed:
                print("Sorry, not enough milk!")
                return False
            if self.beans < beans_needed:
                print("Sorry, not enough coffee beans!")
                return False
            if self.cups < cups_needed:
                print("Sorry, not enough disposable cups!")
                return False
            return True
        except Exception as e:
            print(f"Error while checking resources: {e}")
            return False

    def make_coffee(self, water_needed, milk_needed, beans_needed, cost):
        # Приготування кави
        try:
            self.water -= water_needed
            self.milk -= milk_needed
            self.beans -= beans_needed
            self.cups -= 1
            self.money += cost
            print("I have enough resources, making you a coffee!")
        except Exception as e:
            print(f"Error while making coffee: {e}")

    def buy(self):
        # Логіка покупки кави
        try:
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n>")
            if choice == "1":
                if self.has_enough_resources(250, 0, 16, 1):
                    self.make_coffee(250, 0, 16, 4)
            elif choice == "2":
                if self.has_enough_resources(350, 75, 20, 1):
                    self.make_coffee(350, 75, 20, 7)
            elif choice == "3":
                if self.has_enough_resources(200, 100, 12, 1):
                    self.make_coffee(200, 100, 12, 6)
            elif choice == "back":
                return
            else:
                print("Invalid choice!")
        except Exception as e:
            print(f"Error in buy method: {e}")

    def fill(self):
        # Поповнення запасів
        try:
            self.water += int(input("Write how many ml of water you want to add:\n>"))
            self.milk += int(input("Write how many ml of milk you want to add:\n>"))
            self.beans += int(input("Write how many grams of coffee beans you want to add:\n>"))
            self.cups += int(input("Write how many disposable cups you want to add:\n>"))
        except Exception as e:
            print(f"Error in fill method: {e}")

    def take(self):
        # Вилучення грошей
        try:
            print(f"I gave you {self.money}")
            self.money = 0
        except Exception as e:
            print(f"Error in take method: {e}")

    def start(self):
        # Основний цикл роботи кавомашини
        while True:
            try:
                action = input("Write action (buy, fill, take, remaining, exit):\n")
                if action == "buy":
                    self.buy()
                elif action == "fill":
                    self.fill()
                elif action == "take":
                    self.take()
                elif action == "remaining":
                    self.print_status()
                elif action == "exit":
                    break
                else:
                    print("Invalid action!")
            except Exception as e:
                print(f"Error in main loop: {e}")

# Створення і запуск кавомашини
coffee_machine = CoffeeMachine()
coffee_machine.start()
