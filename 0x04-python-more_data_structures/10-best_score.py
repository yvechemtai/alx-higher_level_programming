#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    best_key = list(a_dictionary.keys())[0]
    highest_score = a_dictionary[best_key]
    for key, value in a_dictionary.items():
        if value > highest_score:
            highest_score = value
            best_key = key
    return best_key
