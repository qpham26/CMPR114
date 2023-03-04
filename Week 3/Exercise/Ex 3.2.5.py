# Prompt user to enter number of laps
num_laps = int(input("Enter the number of laps you have run: "))

# Declaring variables
fastest_lap = 0
slowest_lap = 0
total_time = 0

# Prompt user to enter lap time for each lap
for x in range(num_laps):
    lap_time = float(input(f"Enter the time for lap {x + 1}: "))
    total_time += lap_time

    # Finding the fastest and slowest lap times
    if fastest_lap == 0 or lap_time < fastest_lap:
        fastest_lap = lap_time
    if slowest_lap == 0 or lap_time > slowest_lap:
        slowest_lap = lap_time

# Calculate average
average = total_time / num_laps

# Return results
print(f"Fastest lap time: {fastest_lap}")
print(f"Slowest lap time: {slowest_lap}")
print(f"Average lap time: {average}")

