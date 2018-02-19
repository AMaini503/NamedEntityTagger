#!/usr/bin/python3
import numpy as np

def getTrigramCount(w_x, w_y, w_z):
    count_of_trigram = 0
    with open('ner_rare.counts') as f:
        for line in f:
            tokens = line.strip().split()
            if(tokens[1] == '3-GRAM' 
               and tokens[2] == w_x 
               and tokens[3] == w_y 
               and tokens[4] == w_z):
                
                count_of_trigram = int(tokens[0])
                break
    return count_of_trigram
                




def getBigramCount(w_x, w_y):
    count_of_bigram = 0
    with open('ner_rare.counts') as f:
        for line in f:
            tokens = line.strip().split()
            if(tokens[1] == '2-GRAM' 
               and tokens[2] == w_x 
               and tokens[3] == w_y):
                
                count_of_bigram = int(tokens[0])
                break
    return count_of_bigram
                




with open('trigrams.txt') as f_input, open('5_1.txt', 'w') as f_output:
    for line in f_input:
        w_x, w_y, w_z = line.strip().split()
        
        count_of_trigram = getTrigramCount(w_x, w_y, w_z)
        count_of_bigram  = getBigramCount(w_x, w_y)
        
        prob_q = float(count_of_trigram) / float(count_of_bigram)
        log_prob_q = np.log(prob_q)
        
        line_written_to_output = ' '.join([w_x, w_y, w_z, 
                                           '{}'.format(log_prob_q)])
        line_written_to_output = line_written_to_output + '\n'
        
        f_output.write(line_written_to_output)
        

