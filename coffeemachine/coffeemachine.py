class CoffeeMachine:
    def __init__(self):

        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

        self.state = "choosing_action"
        print("Write action (buy, fill, take, remaining, exit):")

    def report(self):

        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money\n")

    def check_resources(self, water_needed, milk_needed, beans_needed):

        if self.water < water_needed:
            print("Sorry, not enough water!")
            return False
        if self.milk < milk_needed:
            print("Sorry, not enough milk!")
            return False
        if self.beans < beans_needed:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return False
        return True

    def process_input(self, user_input):

        if user_input == "exit":
            return False

        if self.state == "choosing_action":
            if user_input == "buy":
                self.state = "choosing_coffee"
                print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif user_input == "fill":
                self.state = "filling_water"
                print("\nWrite how many ml of water you want to add:")
            elif user_input == "take":
                print(f"\nI gave you {self.money}")
                self.money = 0
                print("\nWrite action (buy, fill, take, remaining, exit):")
            elif user_input == "remaining":
                self.report()
                print("Write action (buy, fill, take, remaining, exit):")
            else:
                print("Unknown action.")

        elif self.state == "choosing_coffee":
            if user_input == "back":
                self.state = "choosing_action"
            elif user_input == "1":
                if self.check_resources(250, 0, 16):
                    print("I have enough resources, making you a coffee!")
                    self.water -= 250
                    self.beans -= 16
                    self.cups -= 1
                    self.money += 4
            elif user_input == "2":
                if self.check_resources(350, 75, 20):
                    print("I have enough resources, making you a coffee!")
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.cups -= 1
                    self.money += 7
            elif user_input == "3":
                if self.check_resources(200, 100, 12):
                    print("I have enough resources, making you a coffee!")
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.cups -= 1
                    self.money += 6

            self.state = "choosing_action"
            print("\nWrite action (buy, fill, take, remaining, exit):")

        elif self.state == "filling_water":
            self.water += int(user_input)
            self.state = "filling_milk"
            print("Write how many ml of milk you want to add:")
        elif self.state == "filling_milk":
            self.milk += int(user_input)
            self.state = "filling_beans"
            print("Write how many grams of coffee beans you want to add:")
        elif self.state == "filling_beans":
            self.beans += int(user_input)
            self.state = "filling_cups"
            print("Write how many disposable cups you want to add:")
        elif self.state == "filling_cups":
            self.cups += int(user_input)
            self.state = "choosing_action"
            print("\nWrite action (buy, fill, take, remaining, exit):")

        return True

machine = CoffeeMachine()
while True:
    entry = input("> ")
    if not machine.process_input(entry):
        break