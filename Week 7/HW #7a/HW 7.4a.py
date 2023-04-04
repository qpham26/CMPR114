#This program converts sentences to PIG LATIN
def pig_latin(sentence):
    vowels = "AEIOU"
    words = sentence.upper().split()
    pig_latin_sentence = []

    for word in words:
        if word[0] in vowels:
            pig_latin_sentence.append(word + "AY")
        else:
            pig_latin_sentence.append(word[1:] + word[0] + "AY")

    return " ".join(pig_latin_sentence)

input_sentence = input("Enter a sentence: ")
output_sentence = pig_latin(input_sentence)

print("Pig Latin: " + output_sentence)

