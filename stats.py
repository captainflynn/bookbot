def count_words(string):
    return len(string.split())

def count_char(string):
    lower_string = string.lower()
    characters = {}
    for c in range(len(lower_string)):
        if lower_string[c] in characters:
            characters[lower_string[c]] += 1
        else:
            characters[lower_string[c]] = 1
    return characters

def sort_on(dict):
    return dict["count"]

def sort_dict(dictionary):
    sorted = []
    for letter in dictionary:
        sorted.append({"character": letter, "count": dictionary[letter]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted