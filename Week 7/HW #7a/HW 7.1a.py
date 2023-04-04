# This program counts the number of vowels
# define a function to count the number of vowels in a string
def count_vowels(string):
    vowels = "aeiouAEIOU" # define all the vowels
    count = 0 # initialize count to 0
    for char in string:
        if char in vowels: # if the character is a vowel, increment the count
            count += 1
    return count # return the total count of vowels

# define a function to count the number of consonants in a string
def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" # define all the consonants
    count = 0 # initialize count to 0
    for char in string:
        if char in consonants: # if the character is a consonant, increment the count
            count += 1
    return count # return the total count of consonants

# prompt the user to enter a string
user_string = input("Enter a string: ")

# count the number of vowels and consonants in the user's string
num_vowels = count_vowels(user_string)
num_consonants = count_consonants(user_string)

# print the results to the console
print("The string '{}' contains {} vowels and {} consonants.".format(user_string, num_vowels, num_consonants))
