#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None:
        return None
    elif len(a_dictionary) is 0:
        return None

    sort_dict = dict(sorted(a_dictionary.items(), key=lambda x: x[1]))

    best_key = next(reversed(sort_dict.keys()))

    return best_key
