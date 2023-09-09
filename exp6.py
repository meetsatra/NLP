import nltk

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# Manually create lists for conjunctions and pronouns
conjunction_list = ['and', 'but', 'or', 'nor', 'for', 'so', 'yet']
pronoun_list = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'us', 'them']

# Create a dictionary of POS tag mappings
pos_mapping = {
    'N': 'Noun',
    'V': 'Verb',
    'J': 'Adjective',
    'R': 'Adverb',
    'C': 'Conjunction',
    'P': 'Pronoun',
}

# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Tokenize the sentence and perform POS tagging
words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)

# Assign tags to each word based on the lists and mapping
final_tags = []
for word, tag in tags:
    if word.lower() in conjunction_list:
        final_tags.append(pos_mapping['C'])
    elif word.lower() in pronoun_list:
        final_tags.append(pos_mapping['P'])
    else:
        if tag.startswith('N'):
            final_tags.append(pos_mapping['N'])
        elif tag.startswith('V'):
            final_tags.append(pos_mapping['V'])
        elif tag.startswith('J'):
            final_tags.append(pos_mapping['J'])
        elif tag.startswith('R'):
            final_tags.append(pos_mapping['R'])
        else:
            final_tags.append('Unknown')

# Print the tagged words
for word, tag in zip(words, final_tags):
    print(f"{word}: {tag}")
