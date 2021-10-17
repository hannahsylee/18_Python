# elmo = ('Elmo', 5, ['hugging', 'being nice'])
# sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
# gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """

    friend1_hobbies = set(a[2])
    friend2_hobbies = set(b[2])

    if friend1_hobbies & friend2_hobbies != set():
        return True
    return False

#     # return friend1_hobbies & friend2_hobbies
#     #     return True
#     # return False

# print(friend_date(elmo, sauron))
# print(friend_date(sauron, gandalf))
    

    