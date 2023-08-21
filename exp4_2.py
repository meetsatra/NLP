from polyglot.text import Text

# Function to generate a word based on morphological details
def generate_word(language, morphological_details):
    try:
        text = Text(morphological_details, hint_language_code=language)
        generated_word = text.entities[0].morphemes[0]
        return generated_word
    except Exception as e:
        return f"Error: {str(e)}"

# Input language choice
language = input("Enter language ('hi' for Hindi, 'en' for English): ")

# Input morphological details
morphological_details = {
    'root': input("Enter root: "),
    'category': input("Enter category: "),
    'gender': input("Enter gender: "),
    'number': input("Enter number: "),
    'person': input("Enter person: "),
    'case': input("Enter case: "),
    'tense': input("Enter tense: "),
}

# Generate and display the word
generated_word = generate_word(language, morphological_details)
print(f"Generated word: {generated_word}")



# Enter language ('hi' for Hindi, 'en' for English): hi
# Enter root: कर
# Enter category: verb
# Enter gender: masculine
# Enter number: plural
# Enter person: first
# Enter case: none
# Enter tense: present
# Generated word: करते