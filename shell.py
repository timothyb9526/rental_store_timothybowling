import core
import disk
import time


def customer(inv, customer_employee, rent_or_return):

    while True:

        print(inv)
        print()
        rental = int(input('Which would you like to rent today?(0, 5) '))
        print()
        time.sleep(.5)
        if rental <= 5:
            name = input('What name would be on this rental? ')
            print()
            time.sleep(.5)
            rental_length = input('How many months will you be renting? ')
            print()
            print('One moment please.......')
            print()
            time.sleep(1)
            rent = core.Rental(name, [], rental_length, rent_or_return)
            item = inv[rental]
            rentals = rent.add_item(item)

            print('Thanks for your business.')
            print()

            print(rent)
            return rent

        else:
            print('Invalid Response')


def return_rental(inv, rent_or_return):

    customer = input('What\'s your name? ')
    print()
    time.sleep(.5)
    return_item = input('okay ' + customer +
                        ' what rental would you like to close? ')
    print()
    time.sleep(.5)
    while True:
        length = int(input('How many months were you renting? '))
        print()
        if length in range(1, 13):

            print('One moment please.........')
            print()
            time.sleep(1)
            print('Thank you for your business.')
            print()

            return_list = core.Rental(customer, [], length, rent_or_return)
            item = inv.return_item(return_item)
            rentals = return_list.add_item(item)

            print(return_list.return_string())
            return return_list

        else:
            print('You can only rent 1 year in advance.')
            print()


def employee(customer_employee):
    while True:

        history = input(
            'Would you like to see the transaction [H]istory or the [I]nventory? '
        )
        print()

        if history == 'H':
            time.sleep(1)
            disk.employee()
            break

        elif history == 'I':
            time.sleep(1)
            disk.print_inventory()
            break
        else:
            print('Please select History or Inventory.')
            print()


def main():

    inv = disk.get_inventory()

    print('Welcome to my rental agency press "q" to quit at any time.')
    print()
    while True:
        customer_employee = input('Are you a [C]ustomer or an [E]mployee? ')
        print()
        if customer_employee == 'C':
            time.sleep(.5)
            while True:

                rent_or_return = input(
                    'Would you like to [R]ent or [C]lose a current rental? ')
                print()
                if rent_or_return == 'R':
                    rent = customer(inv, customer_employee, rent_or_return)
                    disk.write_to_log(rent)

                elif rent_or_return == 'C':
                    return_list = return_rental(inv, rent_or_return)
                    disk.write_to_log_return(return_list)
                break
            break
        elif customer_employee == 'E':
            employee(customer_employee)
            break

    inventory = inv.update_stock()

    disk.give_inventory(inventory)


if __name__ == '__main__':
    main()
