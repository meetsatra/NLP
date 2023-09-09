import spacy 
# Load the SpaCy model 
nlp = spacy.load ( "en_core_web_sm" ) 
# # Get the sentence from the user 
sentence = input ( "Enter a sentence: " ) 
# Process the sentence using SpaCy 
doc = nlp ( sentence ) 
# Print the tagged words 
for token in doc : 
   print(f"{token.text}:{token.pos_}")