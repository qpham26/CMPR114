#Midterm question 1: Calculate Calories from Fat and Carbohydrates
# Get inputs from the user
fat_grams = float(input("Enter the number of fat grams consumed: "))
carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))

# Calculate the calories from fat and carbohydrates
calo_from_fat = fat_grams * 9
calo_from_carbs = carb_grams * 4

# Calculate the total number of calories
total_calories = calo_from_fat + calo_from_carbs

# Display the results to the user
print(f"Calories from fat: {calo_from_fat:.2f}")
print(f"Calories from carbohydrates: {calo_from_carbs:.2f}")
print(f"Total calories: {total_calories:.2f}")
