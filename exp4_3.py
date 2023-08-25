import spacy

# Load the spaCy language model for your desired language
nlp = spacy.load("en_core_web_sm")  # Replace 'en' with your desired language code

# Input word from the user
user_input = input("Enter a word: ")

# Process the input text with spaCy
doc = nlp(user_input)

# Extract and print morphological details
if doc:
    for token in doc:
        print(f"Word: {token.text}")
        print(f"Lemma: {token.lemma_}")
        print(f"Part of Speech: {token.pos_}")
        print(f"Gender: {token._.gender if hasattr(token._, 'gender') else 'N/A'}")
        print(f"Number: {token._.number if hasattr(token._, 'number') else 'N/A'}")
        print(f"Case: {token._.case if hasattr(token._, 'case') else 'N/A'}")
        print(f"Person: {token._.person if hasattr(token._, 'person') else 'N/A'}")
        print(f"Tense: {token._.tense if hasattr(token._, 'tense') else 'N/A'}")
        print(f"Mood: {token._.mood if hasattr(token._, 'mood') else 'N/A'}")
        print(f"Verb Form: {token._.verb_form if hasattr(token._, 'verb_form') else 'N/A'}")
else:
    print("Invalid input or word not found in the language model.")
