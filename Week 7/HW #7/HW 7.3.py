# This program separates words by capitalization
def convert_sentence(sentence):
    words = []
    current_word = ""
    for i in range(len(sentence)):
        if sentence[i].isupper() and current_word:
            words.append(current_word)
            current_word = sentence[i]
        else:
            current_word += sentence[i]
    words.append(current_word)
    return " ".join(words).capitalize()

# Take user input
input_sentence = input("Enter a sentence: ")

# Convert sentence
output_sentence = convert_sentence(input_sentence)

# Output result
print("Input sentence:", input_sentence)
print("Output sentence:", output_sentence)

