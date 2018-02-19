#!/usr/bin/python3
import numpy as np
import os
from aux import computeEmissionsCategorical, getWordCount
from RareWordClassifier import RareWordClassifier

#return count(x, y) / count(y)
def getEmission(emissions, x, y):
    global classifier
    word = classifier.classify(x)
    return emissions[word][y]    


def getq(q, u, v, w):
    if((u, v, w) in q):
        return q[(u, v, w)]
    else:
        return -1


def getT(x, k, emissions):
    if(k < 0):
        return ['*']
    else:
        global classifier
        word = classifier.classify(x[k]) 
        return emissions[word].keys()



def tagUsingViterbi(x, emissions, q):
    

    #initialization
    pi = dict()
    bp = dict()
    
    pi[(-1, '*', '*')] = 1
    
    
    for k in range(len(x)):
        for u in  getT(x, k - 1, emissions):
            for v in getT(x, k, emissions):
                
                pi[(k, u, v)] = 0
                
                for w in getT(x, k - 2, emissions):       
                        q_ml = getq(q, w, u, v)
                        if(q_ml != -1):
                            this_probability = pi[(k - 1, w, u)] * q_ml * getEmission(emissions, x[k], v)                        
                            if(pi[(k, u, v)]  < this_probability):
                                pi[(k, u, v)] = this_probability
                                bp[(k, u, v)] = w

    
    max_prob = -1
    n = len(x)
    
    #tagged sequence has same length as the input sequence
    y = x[:]
    
    for u in getT(x, n - 2, emissions):
        for v in getT(x, n - 1, emissions):
            q_ml = getq(q, u, v, 'STOP')
            if(q_ml != -1):
                if(max_prob < pi[(n - 1, u, v)] * q_ml):
                    max_prob = pi[(n - 1, u, v)] * q_ml
                    y[n - 2] = u
                    y[n - 1] = v
    
    for k in range(n - 3, -1, -1):
        y[k] = bp[(k + 2, y[k + 1], y[k + 2])]
    
    return (y, pi)



#this function assumes that y is 1-indexed
def gety(y, k):
    if(k < 0):
        return '*'
    else:
        return y[k]

def getLogLikelihood(x, y, pi):
    log_likelihood = []
    for k in range(len(x)):
        log_prob = np.log(pi[(k, gety(y, k - 1), gety(y, k))])
        log_likelihood.append(log_prob)
    
    return log_likelihood




def writeThisSentence(f_output, x, y, log_likelihood):
    for (word, tag, log_prob) in zip(x, y, log_likelihood):
        this_line = ' '.join((word, tag, '{}'.format(log_prob)))
        this_line = this_line + '\n'
        f_output.write(this_line)
    f_output.write('\n')


def computeq():
    count_of_trigrams = dict()
    count_of_bigrams = dict()
    
    with open('ner_rare.counts') as f_input:
        for line in f_input:
            tokens = line.strip().split()
            if(tokens[1] == '2-GRAM'):
                u, v = tokens[2], tokens[3]
                count_of_bigrams[(u, v)] = int(tokens[0])
            elif(tokens[1] == '3-GRAM'):
                u, v, w = tokens[2], tokens[3], tokens[4]
                count_of_trigrams[(u, v, w)] = int(tokens[0])
    q = dict()
    for (u, v, w) in count_of_trigrams:
        q[(u, v, w)] = float(count_of_trigrams[(u, v, w)])/ float(count_of_bigrams[(u, v)])
    
    return q


#create the ner_train_rare_categorical.dat file using 6_1.py
os.system('python 6_1.py')
#generate the ner_rare_categorical.counts file
os.system('python2 count_freqs.py ner_train_rare_categorical.dat > ner_rare_categorical.counts')

#initial parameters
q = computeq()
count_of_words = getWordCount()
classifier = RareWordClassifier(count_of_words)
emissions = computeEmissionsCategorical(classifier)


with open('ner_dev.dat') as f_input, open('6.txt', 'w') as f_output:
    x = []
    for line in f_input:
        tokens = line.strip().split()
        
        if(len(tokens) > 0):
            x.append(tokens[0])
        else:
            y, pi = tagUsingViterbi(x, emissions, q)
            log_likelihood = getLogLikelihood(x, y, pi) 
            writeThisSentence(f_output, x, y, log_likelihood)
            
            x = []


