# Question 1
def to_uppercase(words):
    for word in words:
        print(word.capitalize())

# Question 2 & 3
def print_upper_words(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.capitalize())

#Question 4
def print_upper_words_custom(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.capitalize())
                break
