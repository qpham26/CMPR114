# This program ask for number of year, inches of rainfall each month,
# then outputs the total number of months,
# the total inches and the average rainfall for the entire period

# Initialize variables
num_years = int(input("Enter the number of years: "))
total_rainfall = 0
num_months = num_years * 12

# Data collection Loop
for year in range(1, num_years + 1):
    print(f"Year {year}:")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall in inches for month {month}: "))
        total_rainfall += rainfall

# Return outputs
average_rainfall = total_rainfall / num_months

print(f"\nNumber of months: {num_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f}")