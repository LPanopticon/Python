import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Yes/No: " % get_close_matches(w, data.keys())[0])
        if yn == "Yes":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "No":
            return "That isn't a word in our dictionary."
        else:
            return "I didn't catch that."
    else:
        return "Are you sure that is a real word?"

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    i = 0
    for item in output:
        i = i+1
        print(str(i)+":", item)
else:
    print(translate(word))
