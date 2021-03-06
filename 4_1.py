#!/usr/bin/python3
from aux import getWordCount

def modifyRareWords(count_of_words):
    new_train_file_name = 'ner_train_rare.dat'
    old_train_file_name = 'ner_train.dat'
    
    with open(new_train_file_name, 'w+') as fnew, open(old_train_file_name) as fold:
        for line in fold:
            

            #new line is added manually afterwards, so striped
            tokens = line.strip().split()
            
            new_line = ''
            
            #if not a new line
            if(len(tokens) > 0):
                word = tokens[0]
                if(count_of_words[word] < 5):
                    tokens[0] = '_RARE_'
                    new_line = ' '.join(tokens)
                    new_line = new_line + '\n'
                else:
                    new_line = line
            else:
                new_line = line
                
            fnew.write(new_line)


count_of_words = getWordCount()
modifyRareWords(count_of_words)
