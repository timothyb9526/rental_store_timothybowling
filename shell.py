from core import *
from disk import *


def user(inv, customer_employee):

    while input != 'q':
        if customer_employee == 'C':

            rent_or_return = input(
                'Would you like to [R]ent or [C]lose a current rental? ')
            print()
            if rent_or_return == 'R':

                print(inv)
                print()

                rental = int(
                    input('Which would you like to rent today?(0, 6) '))
                print()

                name = input('What name would be on this rental? ')
                print()

                rental_length = input('How many months will you be renting? ')
                print()

                rent = Rental(name, [], rental_length, rent_or_return)
                item = inv[rental]
                rentals = rent.add_item(item)

                print('Thanks for your business.')
                print()

                print(rent)

            elif rent_or_return == 'C':

                return_item = input('What rental would you like to close? ')
                print()

                customer = input('What was the name? ')
                print()

                length = input('How many months were you renting? ')
                print()

                print('Thank you for your business.')
                print()

                return_list = Rental(customer, [], length, rent_or_return)
                item = inv.give_item(return_item)
                rentals = return_list.add_item(item)

                for line in inv.properties:
                    if return_item.lower() in line.name.lower():

                        print(return_list.return_string())
                        return return_list.return_string()

        elif customer_employee == 'E':

            history = input(
                'Would you like to see the transaction [H]istory or the [I]nventory? '
            )
            print()

            if history == 'H':

                employee()

            elif history == 'I':

                print_inventory()
        break


def main():

    inv = get_inventory()

    print('Welcome to my rental agency press "q" to quit at any time.')
    print()

    customer_employee = input('Are you a [C]ustomer or an [E]mployee? ')
    print()

    rent = user(inv, customer_employee)

    write_to_log(rent)

    inventory = inv.update_stock()

    give_inventory(inventory)


if __name__ == '__main__':
    main()
