def invert_dictionary(d):
    inverted = dict()
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key] 
    return inverted

print(invert_dictionary({"a": 1, "b": 2, "c": 3}))

def merge_dictionaries(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))


def word_frequencies(text):
    words = text.split()
    return {word: words.count(word) for word in set(words)}

text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))


def add_contact(contacts, name, **details):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(details)

contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St") 
print(contacts)

