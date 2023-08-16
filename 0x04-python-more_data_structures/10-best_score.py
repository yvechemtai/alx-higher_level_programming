#!/usr/bin/python3
def find_best_score(scores_dict):
    """Returns a key with the biggest integer value."""
    if not isinstance(scores_dict, dict) or len(scores_dict) == 0:
        return None

    best_key = list(scores_dict.keys())[0]
    highest_score = scores_dict[best_key]
    for key, value in scores_dict.items():
        if value > highest_score:
            highest_score = value
            best_key = key
    return best_key
