def print_upper_words1(words):
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words1(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words2(["eagle", "Edward", "Alfred"])
print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})