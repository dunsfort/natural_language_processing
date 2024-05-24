#!/usr/bin/env python
# coding: utf-8

# ### Import libraries 

# In[1]:


# Import library
import spacy


# The module used in the code is 'spacy', which is a natural language processing library in python. It provides tools and pre-trained models for various (Natural Language Processing) NLP tasks such as tokenization, part of speech tagging, named entity recognition (NER), and depedency parsing.

# In[2]:


# NER with spacy
nlp = spacy.load("en_core_web_sm")


# ### Atleast 2 garden path sentences (from the web)

# In[3]:


# Define the garden path sentences 
gardenpathSentences = [
    "The man whistling tunes pianos beatifully.",
    "The cotton clothing is usually made of grows in Mississippi.",
    "The chicken ready to eat.",
    "The old man the newspaper."
]


# In[4]:


# Add the additional sentences
additionalSentences = [
    "Marry gave the child a Band_Aid.",
    "That Jill is never here hurts.",
    "The old man the ships."
]

# Combine the two lists
gardenpathSentences.extend(additionalSentences)


# ### Tokenise each sentence in the list and perform NER
# - Tokenisation is importanant concept in natural learning processing (NLP) that involves breaking down a text into smaller units, typically words or subwords, called tokens. These tokens serves as the basic building block for NLP tasks such as part of speech (POS) tagging, NER, and systactic parsing.

# In[19]:


# Iterate through each sentence in the list and tokenize it 
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    
    # Iterate through each word in the tokenized sentence and print its text and POS 
    for token in doc:
        print(token.text, token.pos_, spacy.explain(token.pos_))
    
    # Iterate through each recognized entity in the sentence and print its text, label, and explanation  
    for ent in doc.ents:
        print(ent.text, ent.label_, spacy.explain(ent.label_))
        
    # Add a blank line for readibilty between each sentence's entities    
    print("\n")


# ### Two looked up entities
# - Entities in Named Entity Recognition (NER) are specific pieces of information within text that refer to real world objects, such as persons, organizations, locations, dates, etc.
# 
# **Looked up entities:**
# 
# **1. GPE:** Geopolitical entity i.e., countries, cities, states.
#    - Explanation: This entity represents geopitical entities such as countries, cities, and provinces/states.
#    - Examples: "Mississippi" was categorized as a GPE in the sentence "The cotton clothing is usually made of growth in Mississipi." 
#      Yes, the entity "GPE" makes sense in terms of the word "Mississippi" associated with it, as Mississippi is a state in the United States
# 
# **2. ORG:** Organisations i.e., companies, agencies, institutions, etc.
#    - Explanation: This entity represents organisations such as a companies, agencies, institutions, etc.
#    - Examples: "Band_Aid" was categorized as an ORG entity in the sentence "Marry gave the child a Band_Aid."
#    - No, the entity "ORG" does not make sense in term of the word "Band_Aid" Associated with it, as "Band_Aid" is a band name adhesive bandages, not an organisation.
