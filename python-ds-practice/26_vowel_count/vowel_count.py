def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    VOWELS = set('aeiou')
    vowel_dictionary = {}
    phrase = phrase.lower()

    for letter in phrase:
        if letter in VOWELS:
            vowel_dictionary[letter] = vowel_dictionary.get(letter, 0) + 1

    return vowel_dictionary
