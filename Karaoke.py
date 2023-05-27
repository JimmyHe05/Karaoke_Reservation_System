# This program is used to calculate the cost of karaoke and drinks at Nam's Noddle (my cousin's restaurant)

import math


def calculate_charge(start_time, end_time):
    print('Early Bird Special rate: $30/hr, (12 PM - 6 PM)', end=' | ')
    print('Before 9 PM rate: $45/hr, (6 PM - 9 PM)', end=' | ')
    print('After 9 PM rate: $50/hr, (9 PM - 12 AM)')
    print()

    # Define the hourly rates based on time intervals
    rates = {
        'Early Bird Special': 30,  # Rate during daytime (12 AM - 6 PM)
        'Before 9': 45,  # Rate during evening (6 PM - 9 PM)
        'After 9': 50  # Rate during night (9 PM - 12 PM)
    }

    # Convert start and end times to 24-hour format
    start_hour = int(start_time[:-3])
    end_hour = int(end_time[:-3])

    # Handle 12:00 pm, 12 > 1
    if int(start_time[:-3]) > end_hour:
        start_hour = 0

    # Split the start and end times into hours and minutes
    start_minute = int(start_time[-2:])
    end_minute = int(end_time[-2:])

    # Calculate the minutes per hour for the start time
    minutes_per_hour = 60 - start_minute if start_minute > 0 else 60

    # Calculate the total number of minutes
    total_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)

    # Calculate the charge based on the time intervals
    charge = 0
    current_hour = start_hour

    while total_minutes > 0:
        if 0 <= current_hour < 6:  # Between 12 am and 6 am
            rate_name = 'Early Bird Special'
        elif 6 <= current_hour < 9:
            rate_name = 'Before 9'
        elif 9 <= current_hour <= 12:
            rate_name = 'After 9'
        else:
            rate_name = None

        interval = min(minutes_per_hour, total_minutes)  # Calculate minutes within the current hour
        rate = rates[rate_name]
        charge += rate * (interval / 60)

        if charge <= 100:
            hour_period = current_hour + 12 if rate_name == 'Early Bird Special' and current_hour == 0 else current_hour
            if hour_period == 12:
                print(
                    rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(4) +
                    ' | Time interval: ' + str(interval).rjust(2) + ' min |  $' + f'{charge:.2f}')
            else:
                print(
                    rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(5) +
                    ' | Time interval: ' + str(interval).rjust(2) + ' min |  $' + f'{charge:.2f}')
        else:
            if rate_name == 'Early Bird Special':
                hour_period = current_hour + 12 if current_hour == 0 else current_hour
                print(
                    rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(
                        5) +
                    ' | Time interval: '.rjust(18) + str(interval).rjust(2) + ' min | $' + f'{charge:.2f}')
            else:
                hour_period = current_hour
                if hour_period == 10 or hour_period == 11:
                    print(
                        rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(
                            4) +
                        ' | Time interval: '.rjust(18) + str(interval).rjust(2) + ' min | $' + f'{charge:.2f}')
                else:
                    print(
                        rate_name.ljust(20) + ' | Hour period: ' + str(hour_period) + '-' + str(current_hour + 1).ljust(
                            5) +
                        ' | Time interval: '.rjust(18) + str(interval).rjust(2) + ' min | $' + f'{charge:.2f}')

        total_minutes -= interval
        current_hour += 1
        minutes_per_hour = 60  # Reset minutes_per_hour for the remaining hours
    print()
    return charge


# Example usage, assuming that karaoke time will only be from 12:00 pm to 12:00 am

karaoke_start_time = '6:00'
karaoke_end_time = '8:01'
# karaoke_start_time = input('Enter the start time (in 12-hour format, e.g., 12:00): ')
# karaoke_end_time = input('Enter the end time (in 12-hour format, e.g., 4:00): ')


# Convert start and end times to 24-hour format
subtotal_charge = format(calculate_charge(karaoke_start_time, karaoke_end_time), '.2f')
tax_rate = 0.055
tax = format((float(subtotal_charge) * tax_rate), '.2f')
total_karaoke_charge = format((float(subtotal_charge) + float(tax)), '.2f')

print('Subtotal: ' + ('$' + subtotal_charge))
if float(tax) < 10:
    if float(subtotal_charge) > 100:
        print('Tax: ' + ('$' + tax).rjust(12) + '\n')
    else:
        print('Tax: ' + ('$' + tax).rjust(11) + '\n')
else:
    print('Tax: ' + ('$' + tax).rjust(12) + '\n')

if karaoke_end_time[:-3] == '12':
    print('The total charge for karaoke from ' + karaoke_start_time + ' pm to ' + karaoke_end_time + ' am is $' +
          total_karaoke_charge)
else:
    print('The total charge for karaoke from ' + karaoke_start_time + ' pm to ' + karaoke_end_time + ' pm is $' +
          total_karaoke_charge)

print('Drinks'.center(63, '-'))

drinks = {
    'soft drink': 2.75,
    'mixed drink': 7,
    'shot': 5,
}

try:
    usr_input = input('What is the drink and quantity of order (e.g., 2 soft drink)\n')
    total_price = 0
    ordered_list = []
    while usr_input != 'quit':
        ordered_list.append(usr_input)
        quantity = usr_input[0]
        drink_name = usr_input[2:]
        price = float(quantity) * drinks[drink_name]
        total_price += price
        usr_input = input('What is the drink and quantity of order (e.g., 2 soft drink)\n')
        if usr_input == 'quit':
            # print a summary table
            print(','.join(ordered_list))
            print('Total drink price: $' + str(total_price))
except KeyError as e:
    print('Input Error, re-input:')
    usr_input = input('What is the drink and quantity of order (e.g., 2 soft drink)\n')
