# Dictionary containing morphological analysis information for given words
morphological_data = {
    'men': ['man', 'noun', 'plural', 'masc', 'singular/plural', '1/2/3', None, None, None],
    'works': ['work', 'noun', 'plural', 'neut', 'singular/plural', '1/2/3', None, None, None],
    'riding': ['ride', 'verb', 'gerund', 'masc/fem', 'singular/plural', '1/2/3', None, None, None],
    'books': ['book', 'noun', 'plural', 'masc/fem', 'singular/plural', '1/2/3', None, None, None],
    'class': ['class', 'noun', 'singular', 'masc/fem', 'singular/plural', '1/2/3', None, None, None],
    'किताबें': ['किताब', 'noun', 'plural', 'fem', 'singular/plural', '1/2/3', None, None, None],
    'भागो': ['भाग', 'noun', 'singular', 'masc/fem', 'singular/plural', '1/2/3', None, None, None],
    'देखो': ['देख', 'verb', 'imperative', 'masc/fem', 'singular/plural', '1/2/3', 'present', 'habitual'],
    'सुन्दर': ['सुन्दर', 'adjective', 'singular', 'masc/fem', 'singular/plural', '1/2/3', None, None, None],
    'अभियांत्रिकी': ['अभियांत्रिक', 'noun', 'singular', 'fem', 'singular/plural', '1/2/3', None, None, None]
}


# User input
user_input = input("Enter a word: ")

# Retrieve and print the morphological analysis for the user input
if user_input in morphological_data:
    print(f"Word: {user_input}")
    features = morphological_data[user_input]
    print(f"Root: {features[0]}")
    print(f"Category: {features[1]}")
    print(f"Gender: {features[3]}")
    print(f"Number: {features[4]}")
    print(f"Person: {features[5]}")
    print(f"Case: {features[6]}")
    print(f"Tense: {features[7]}")
    print(f"Aspect: {features[8]}")
else:
    print("Word not found in the dictionary.")

