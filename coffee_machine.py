class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def do_action(self, action):
        if action == 'buy':
            self.choose_coffee()
        elif action == 'fill':
            self.fill_machine()
        elif action == 'take':
            self.take_money()
        elif action == 'remaining':
            self.remaining()
        elif action == 'exit':
            exit(0)
        else:
            ...

    def choose_coffee(self):
        print()
        type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, "back" - to back menu: \n')
        if type == '1':
            self.make_coffee([250, 0, 16, 1, 4])
        elif type == '2':
            self.make_coffee([350, 75, 20, 1, 7])
        elif type == '3':
            self.make_coffee([200, 100, 12, 1, 6])
        elif type == 'back':
            print()
            main()
        else:
            ...

    def make_coffee(self, data):
        if self.water >= data[0]:
            if self.milk >= data[1]:
                if self.beans >= data[2]:
                    if self.cups > data[3]:
                        self.water -= data[0]
                        self.milk -= data[1]
                        self.beans -= data[2]
                        self.cups -= data[3]
                        self.money += data[4]
                        print('I have enough resources, making you a coffee!')
                        print()
                        main()
                    else:
                        print('Sorry, not enough cups!')
                        print()
                        main()
                else:
                    print('Sorry, not enough beans!')
                    print()
                    main()
            else:
                print('Sorry, not enough milk!')
                print()
                main()
        else:
            print('Sorry, not enough water!')
            print()
            main()

    def remaining(self):
        print()
        print(f'The coffee machine has:\n'
              f'{self.water} of water\n'
              f'{self.milk} of milk\n'
              f'{self.beans} of coffee beans\n'
              f'{self.cups} of disposable cups\n'
              f'${self.money} of money\n')
        main()

    def fill_machine(self):
        print()
        self.water += int(input('Write how many ml of water do you want to add: \n'))
        self.milk += int(input('Write how many ml of milk do you want to add: \n'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add \n'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: \n'))
        print()
        main()

    def take_money(self):
        print()
        print(f'I gave you ${self.money}')
        self.money -= self.money
        print()
        main()


def main():
    action = input('Write action (buy, fill, take, remaining, exit): \n')
    if action in ('buy', 'fill', 'take', 'remaining', 'exit'):
        machine.do_action(action)
    else:
        ...


# Main program starts here:
machine = CoffeeMachine()
main()
