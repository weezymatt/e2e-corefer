"""
Implementation of algorithms for coreference resolution.
Matthew A. Hernandez, 2023
"""

def hobbs_naive(sentence, pronoun_index):
  """
  *code goes here*
  """
  tokens = nltk.word_tokenize(sentence)
  tagged_tokens = nltk.pos_tag(tokens)
  pronoun = tagged_tokens[pronoun_index][0]

  # Determine the noun phrase whose pronoun corefers
  for i in range(pronoun_index -1, -1, -1):
    if tagged_tokens[i][1] in ['NN', 'NNS']:
      noun_phrase = tagged_tokens[i][0]
      break

  # Apply hobbs' naive algorithm to find antecedent
  for i in range(pronoun_index - 1, -1, -1):
    if tagged_tokens[i][1] in ['NN', 'NNS']:
      if tagged_tokens[i][0] != noun_phrase:
        return tagged_tokens[i][0]
    elif tagged_tokens[i][1] in ['PRP', 'PRP$']:
      return tagged_tokens[i][0]
  
  return None # No suitable antecedent found.

