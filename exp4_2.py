from polyglot.text import Text

# User input
user_input = input("Enter a word: ")

# Analyze the word using polyglot
text = Text(user_input)
word = text.words[0]

if len(word.morphemes) > 0:
    morphemes = word.morphemes[0]

    print(f"Word: {user_input}")
    print(f"Root: {morphemes.root}")
    print(f"Category: {morphemes.tag}")
    print(f"Gender: {morphemes.gender}")
    print(f"Number: {morphemes.number}")
    print(f"Person: {morphemes.person}")
    print(f"Case: {morphemes.case}")
    print(f"Tense: {morphemes.tense}")
    print(f"Aspect: {morphemes.aspect}")
else:
    print("Word not found.")
