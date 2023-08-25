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

# making table:
# import pandas as pd

# # Create a DataFrame for English data
# english_data = {
#     'English Word': ['men', 'works', 'riding', 'books', 'class'],
#     'Category': ['noun', 'noun', 'verb', 'noun', 'noun'],
#     'Number': ['plural', 'plural', 'gerund', 'plural', 'singular'],
#     'Gender': ['masc', 'neut', 'masc/fem', 'masc/fem', 'masc/fem'],
#     'Person': ['singular/plural', 'singular/plural', 'singular/plural', 'singular/plural', 'singular/plural'],
#     'Case': ['1/2/3', '1/2/3', '1/2/3', '1/2/3', '1/2/3'],
#     'Tense': [None, None, None, None, None],
#     'Mood': [None, None, None, None, None],
#     'Verb Form': [None, None, None, None, None]
# }

# df_english = pd.DataFrame(english_data)

# # Create a DataFrame for Hindi data
# hindi_data = {
#     'Hindi Word': ['किताबें', 'भागो', 'देखो', 'सुन्दर', 'अभियांत्रिकी'],
#     'Category': ['noun', 'noun', 'verb', 'adjective', 'noun'],
#     'Number': ['plural', 'singular', 'singular/plural', 'singular', 'singular'],
#     'Gender': ['fem', 'masc/fem', 'masc/fem', 'masc/fem', 'fem'],
#     'Person': ['singular/plural', 'singular/plural', 'singular/plural', 'singular/plural', 'singular/plural'],
#     'Case': ['1/2/3', '1/2/3', '1/2/3', '1/2/3', '1/2/3'],
#     'Tense': ['present', None, 'present', None, None],
#     'Mood': ['habitual', None, None, None, None],
#     'Verb Form': [None, None, 'imperative', None, None]
# }

# df_hindi = pd.DataFrame(hindi_data)

# # Create an Excel writer object and save the DataFrames to different sheets
# with pd.ExcelWriter('morphological_data.xlsx', engine='openpyxl') as writer:
#     df_english.to_excel(writer, sheet_name='English', index=False)
#     df_hindi.to_excel(writer, sheet_name='Hindi', index=False)

# print("Excel file 'morphological_data.xlsx' has been created with two sheets (English and Hindi).")

