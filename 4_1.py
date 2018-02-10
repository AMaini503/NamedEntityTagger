#!/usr/bin/python

def getWordCount():
    words = set()
    count_of_words = dict()
    
    with open('ner.counts') as f:
        for line in f:
            tokens = line.strip().split()
            if(tokens[1] == 'WORDTAG'):
                word = tokens[3]
                this_count = int(tokens[0])
                if(word in count_of_words):
                    count_of_words[word] += this_count
                else:
                    count_of_words[word] = this_count
    return count_of_words

def modifyRareWords(rare_words):
    new_train_file_name = 'ner_train_rare.dat'
    old_train_file_name = 'ner_train.dat'
    
    with open(new_train_file_name, 'w') as fnew, open(old_train_file_name) as fold:
        for line in fold:
            

            #new line is added manually afterwards, so striped
            tokens = line.strip().split()
            
            new_line = ''
            
            #if not a new line
            if(len(tokens) > 0):
                word = tokens[0]
                if(word in rare_words):
                    tokens[0] = '_RARE_'
                    new_line = ' '.join(tokens)
                    new_line = new_line + '\n'
                else:
                    new_line = line
            else:
                new_line = line
                
            fnew.write(new_line)

def getRareWords(count_of_words):
    rare_words = [word for word in count_of_words if count_of_words[word] < 5]
    return rare_words

count_of_words = getWordCount()
rare_words = getRareWords(count_of_words)
modifyRareWords(rare_words)
