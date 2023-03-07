#This program takes 4 scores, calculates the sum and the average

scores_list = []

for i in range(4):
    score = float(input(f"Enter score {i+1}: "))
    scores_list.append(score)

sum = sum(scores_list)
average = sum/len(scores_list)

print("Sum =", sum)
print("Average =", average)