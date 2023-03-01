# this will ask for the monthly rainfall to get the total and store it in a list

def main():
    month_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']
    month_rain = []
    print('Enter the rain fall for each month. \n')

    index = 0
    for i in month_in_year:
        rain = float(input(f'Enter the amount of rain for {i}: '))
        month_rain.append(rain)
        index += 1

    total_rain = total(month_rain)
    average_rain = total_rain / len(month_rain)
    less_rain = min(month_rain)
    less_rain_index = month_rain.index(less_rain)
    most_rain = max(month_rain)
    most_rain_index = month_rain.index(most_rain)

    print(f'The total rain in the year was: {total_rain}')
    print(f'The average rain in each month is: {average_rain: .2f}')
    print(f'The month with lowest rain was {month_in_year[less_rain_index]} with {less_rain} inches of rain')
    print(f'The month with highest rain was {month_in_year[most_rain_index]} with {most_rain} inches of rain')
    write('yearly_rain.txt', month_rain, total_rain, month_in_year)

def total(numbers):
    sum = 0
    for value in numbers:
        sum += int(value or 0)
    return sum

def write(name, month_rain, total, month_in_year):
    index = 0
    output = open(name, 'w')
    for rain in month_rain:
        output.writelines(f'{month_in_year[index]}: {rain} inches\n')
        index += 1
    output.writelines(f'Total rain: {total: .2f} inches\n')
    output.writelines(f'The average rain on this year was {total / len(month_in_year)} inches\n')
    less_rain = min(month_rain)
    less_rain_index = month_rain.index(less_rain)
    most_rain = max(month_rain)
    most_rain_index = month_rain.index(most_rain)
    output.writelines(
        f'The month with lowest rain was {month_in_year[less_rain_index]} with {less_rain} inches of rain')
    output.writelines(
        f'The month with highest rain was {month_in_year[most_rain_index]} with {most_rain} inches of rain')

main()