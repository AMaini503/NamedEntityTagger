#!/usr/bin/python

#creates the new train file
from RareWordClassifier import RareWordClassifier
from aux import getWordCount

def modifyRareWords(classifier):
    new_train_file_name = 'ner_train_rare_categorical.dat'
    old_train_file_name = 'ner_train.dat'
    
    with open(new_train_file_name, 'w+') as fnew, open(old_train_file_name) as fold:
        for line in fold:
            

            #new line is added manually afterwards, so striped
            tokens = line.strip().split()
            
            new_line = ''
            
            #if not a new line
            if(len(tokens) > 0):
                word = tokens[0]
                tokens[0] = classifier.classify(word)
                new_line = ' '.join(tokens)
                new_line = new_line + '\n'
            else:
                new_line = line
                
            fnew.write(new_line)


count_of_words = getWordCount()

#classifies words depending on their counts
classifier = RareWordClassifier(count_of_words)
modifyRareWords(classifier)
