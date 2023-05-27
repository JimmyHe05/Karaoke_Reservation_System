# This program is used to calculate the cost of karaoke and drinks at Nam's Noddle (my cousin's restaurant)

def calculate_charge(start_time, end_time):
    # Define the hourly rates based on time intervals
    rates = {
        'Early Bird Special': 30,  # Rate during daytime (12 AM - 6 PM)
        'Before 9': 45,  # Rate during evening (6 PM - 9 PM)
        'After 9': 50  # Rate during night (9 PM - 12 PM)
    }

    # Convert start and end times to 12-hour format
    try:
        start_hour = int(start_time[:-3])
        end_hour = int(end_time[:-3])
    except ValueError as e:
        print('Input Error, re-input: ')
        new_start_time = input('Enter the start time (in 12-hour format, e.g., 12:00): ')
        new_end_time = input('Enter the end time (in 12-hour format, e.g., 4:00): ')
        print()
        return calculate_charge(new_start_time, new_end_time)

    # Handle 12:00 pm, 12 > 1
    if int(start_time[:-3]) > end_hour:
        start_hour = 0

    # Split the start and end times into minutes
    start_minute = int(start_time[-2:])
    end_minute = int(end_time[-2:])

    # Calculate the minutes per hour for the start time
    minutes_per_hour = 60 - start_minute if start_minute > 0 else 60

    # Calculate the total number of minutes
    total_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)

    # Calculate the charge based on the time intervals
    karaoke_subtotal_charge = 0.0
    current_hour = start_hour

    while total_minutes > 0:
        if 0 <= current_hour < 6:  # Between 12 pm and 6 pm
            rate_name = 'Early Bird Special'
        elif 6 <= current_hour < 9:  # Between 6 pm and 9 pm
            rate_name = 'Before 9'
        elif 9 <= current_hour <= 12:  # Between 9 pm and 12 am
            rate_name = 'After 9'
        else:
            rate_name = None

        interval = min(minutes_per_hour, total_minutes)  # Calculate minutes within the current hour
        rate = rates[rate_name]
        karaoke_subtotal_charge += round(rate * (interval / 60), 2)

        if karaoke_subtotal_charge <= 100:
            hour_period = current_hour + 12 if rate_name == 'Early Bird Special' and current_hour == 0 else current_hour
            if hour_period == 12:
                print(
                    rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(4) +
                    ' | Time interval: ' + str(interval).rjust(2) + ' min |  $' + f'{karaoke_subtotal_charge:.2f}')
            else:
                print(
                    rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(5) +
                    ' | Time interval: ' + str(interval).rjust(2) + ' min |  $' + f'{karaoke_subtotal_charge:.2f}')
        else:
            if rate_name == 'Early Bird Special':
                hour_period = current_hour + 12 if current_hour == 0 else current_hour
                print(
                    rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(
                        5) +
                    ' | Time interval: '.rjust(18) + str(interval).rjust(
                        2) + ' min | $' + f'{karaoke_subtotal_charge:.2f}')
            else:
                hour_period = current_hour
                if hour_period == 10 or hour_period == 11:
                    print(
                        rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(
                            4) +
                        ' | Time interval: '.rjust(18) + str(interval).rjust(
                            2) + ' min | $' + f'{karaoke_subtotal_charge:.2f}')
                else:
                    print(
                        rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(
                            5) +
                        ' | Time interval: '.rjust(18) + str(interval).rjust(
                            2) + ' min | $' + f'{karaoke_subtotal_charge:.2f}')

        total_minutes -= interval
        current_hour += 1
        minutes_per_hour = 60  # Reset minutes_per_hour for the remaining hours

    print()
    global tax_rate
    karaoke_subtotal_charge = '{:.2f}'.format(karaoke_subtotal_charge)
    karaoke_tax = '{:.2f}'.format(float(karaoke_subtotal_charge) * tax_rate)
    total_karaoke_charge = float(karaoke_subtotal_charge) + float(karaoke_tax)

    print('Karaoke subtotal: $' + karaoke_subtotal_charge)
    if float(karaoke_tax) < 10 and float(karaoke_subtotal_charge) < 100:
        print('Tax: ' + ('$' + karaoke_tax).rjust(19))
    else:
        print('Tax: ' + ('$' + karaoke_tax).rjust(20))
    if float(karaoke_subtotal_charge) < 100:
        print('Karaoke total: ' + ('$' + str(total_karaoke_charge)).rjust(9))
    else:
        print('Karaoke total: ' + ('$' + str(total_karaoke_charge)).rjust(10))

    return total_karaoke_charge


def drink_cost(usr_input):
    global tax_rate
    drinks = {'soft drink': 2.75, 'mixed drink': 7, 'shot': 5, 'beer': 5, 'cup of beer': 5, 'bottle of beer': 5,
              'top shelf shot': 7, 'pitcher of beer': 16,
              "Nam's Lychee": 8, 'Summertime Swirl': 8, 'Moscow Mule': 8, 'Tequila Sunrise': 7, 'Mai Tai': 8}

    subtotal_cost = 0.0
    ordered_list = []
    while True:
        if usr_input.lower() not in ['quit', 'q']:
            ordered_list.extend(usr_input.split(','))
        if usr_input.lower() in ['quit', 'q']:
            break

        drink_list = []
        drink_list.extend(usr_input.split(','))
        item_count = 0

        for item in drink_list:
            item = item.strip()
            try:
                first_space_index = item.find(" ")
                quantity = int(item[:first_space_index])
                name = item[first_space_index + 1:]
                if name not in drinks:
                    raise ValueError("Invalid drink option")

                cost = quantity * drinks[name]
                subtotal_cost += cost
                item_count += 1
                if item_count == len(drink_list):
                    print("Current cost: $" + str(subtotal_cost))

            except ValueError:
                print("Input Error, please enter a valid quantity and drink name.")
                print("Current cost: $" + str(subtotal_cost))
                continue

        else:
            usr_input = input("What is the quantity and drink name of the order (e.g., 2 soft drink, 4 shot)?:\n")
            continue
        break

    subtotal_cost = '{:.2f}'.format(subtotal_cost)
    tax = '{:.2f}'.format(float(subtotal_cost) * tax_rate)

    drinks_quantities = {}

    for ordered_item in ordered_list:
        try:
            ordered_item = ordered_item.strip()
            first_space_index = ordered_item.find(" ")
            quantity = int(ordered_item[:first_space_index])
            drink_name = ordered_item[first_space_index + 1:]

            if drink_name not in drinks:
                continue

            if drink_name in drinks_quantities:
                drinks_quantities[drink_name] += quantity
            else:
                drinks_quantities[drink_name] = quantity
        except ValueError:
            continue

    item_list = [f"{quantity} {drink_name}" for drink_name, quantity in drinks_quantities.items()]
    print("You have ordered:", ", ".join(item_list))
    print()
    drink_total = '{:.2f}'.format(float(subtotal_cost) + float(tax))

    print('Drink subtotal:', ('$' + str(subtotal_cost)))
    if float(subtotal_cost) < 10:
        print('Tax: ' + ('$' + tax).rjust(16))
        print('Drink total: ' + ('$' + drink_total).rjust(8))
    elif float(subtotal_cost) < 100:
        print('Tax: ' + ('$' + tax).rjust(17))
        print('Drink total: ' + ('$' + drink_total).rjust(9))
    else:
        print('Tax: ' + ('$' + tax).rjust(18))
        print('Drink total: ' + ('$' + drink_total).rjust(10))

    return drink_total


def calc_total_cost(total_karaoke_cost, total_drink_cost):
    return total_karaoke_cost + total_drink_cost


# Assuming that karaoke time will only be from 12:00 pm to 12:00 am
print('Karaoke Charge Rate'.center(77, '-'))
print('Early Bird Special rate: $30/hr, (12 PM - 6 PM)', end=' | ')
print('Before 9 PM rate: $45/hr, (6 PM - 9 PM)', end=' | ')
print('After 9 PM rate: $50/hr, (9 PM - 12 AM)')
print('Karaoke Start Time'.center(77, '-'))

tax_rate = 0.055

try:
    karaoke_start_time = input('Enter the start time (in 12-hour format, e.g., 12:00): ')

    print('Drinks'.center(77, '-'))
    user_input = input(
        "What is the quantity and drink name of the order (e.g., 2 soft drink, 4 shot)? Press 'q' or 'quit' to get "
        "the total cost.\n")

    total_drink_cost = float(drink_cost(user_input))  # calculate the total cost for drinks

    print('Karaoke End Time'.center(77, '-'))
    karaoke_end_time = input('Enter the end time (in 12-hour format, e.g., 4:00): ')
    print()

    total_karaoke_cost = calculate_charge(karaoke_start_time,
                                          karaoke_end_time)  # calculate the total charge for karaoke


except KeyboardInterrupt:
    print("\nProgram interrupted by the user.")

total_cost = calc_total_cost(total_karaoke_cost, total_drink_cost)
print('Karaoke and Drinks Total'.center(77, '-'))
print('Your total plus tax is: $' + str(total_cost) + '\n')
print('Have a good day!')
