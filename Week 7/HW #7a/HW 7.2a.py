#This program counts and displays the character that appears the most
def most_frequent(s):

    # Creating a dictionary to store the count of each character
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    # Finding the character that appears most frequently
    max_count = 0
    max_char = ''
    for char, count in freq.items():
        if count > max_count:
            max_count = count
            max_char = char
    # Returning the character and its count
    return max_char, max_count

# Accepting a string input from the user
string = input("Enter a string: ")
# Calling the most_frequent function to find the most frequently occurring character and its count
char, count = most_frequent(string)
# Displaying the result
print("The character that appears most frequently in the string is '{}' and it appears {} times.".format(char, count))
