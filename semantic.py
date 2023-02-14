# run all the code extracts above,
import spacy
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# What I found interesting :
    # I found that the similarities changed from the example code above to my own,
    # I am unsure of the reasoning behind this,

# Think of an example of my own :
tokens = nlp('dog orange dolphin apricot ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go", 
             "Hello, there is my car",
             "I\ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarlity = nlp(sentence).similarity(model_sentence)
    print(sentence+" - ", similarlity)
    
###Note on what is different between 'en_core_web_md' and 'en_core_web_sm'.###
# The simple model returns the warning, that it does not use word vectors