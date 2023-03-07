#Program calculate the average and gets letter grade
scores =[]
print(f"Enter 4 scores to get your grade.")
#Loop to add the scores to the list
for i in range(4):
    score = float(input(f"Enter score {i+1}: "))
    scores.append(score)

total = sum(scores)
average = total/len(scores)
#Check to see if average is > 100 for data re-entry
while average > 100:
    print(f"Average score: {average:.2f}")
    print("The average is greater than 100. Please re-enter 4 scores.")
    scores = []
    for i in range(4):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)
    average = sum(scores) / len(scores)

#Determine letter grade
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"Average score: {average:.2f}")
print(f"Letter grade: {letter_grade}")
