# Module 7 - Text Conversion Program

# Set all variables including a list of the vowels to check against
user_input = ""
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
ay = "ay"
yay = "yay"

# Custom function to take apart the sentence and return it in Pig Latin
def to_pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = []
    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + yay)
        elif word[1] in vowels:
            pig_latin_words.append(word[1:] + word[0] + ay)
        elif word[2] in vowels:
            pig_latin_words.append(word[2:] + word[:2] + ay)
        elif word[3] in vowels:
            pig_latin_words.append(word[3:] + word[:3] + ay)
        # Could continue but sensing there's probably an easier way to make this ladder I don't know yet
    return " ".join(pig_latin_words) 



while user_input != "exit":
    user_input = input("\nEnter a sentence to convert to Pig Latin or type exit to quit: ")
    if user_input.lower() == "exit":
        user_input = user_input.lower()
        print("Goodbye")
    else:
        pig_latin = to_pig_latin(user_input)
        print(pig_latin)
