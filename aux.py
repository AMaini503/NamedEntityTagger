def getAllWordsAndTags(filename):
    with open(filename) as f_input:
        tags = set()
        words = set()
        for line in f_input:
            tokens = line.strip().split()
            
            if(tokens[1] == 'WORDTAG'):
                tag = tokens[2]
                tags.add(tag)
                word = tokens[3]
                words.add(word)
    return words, tags

def computeEmissionsCategorical(classifier):
    #read the ner_rare.counts file
    #compute e(x|y) for all x and y

    words, tags = getAllWordsAndTags('ner_rare_categorical.counts')

    #emissions[word][tag] -> e(word | tag)
    emissions = dict()

    for word in words:
        emissions[word] = dict()


    #count(y)
    count_of_tags = dict()
    for tag in tags:
        count_of_tags[tag] = 0

    with open('ner_rare_categorical.counts') as f:
        for line in f:
            tokens = line.strip().split()
            if(tokens[1] == 'WORDTAG'):
                word = tokens[3]
                tag = tokens[2]
                tag_count = int(tokens[0])
                count_of_tags[tag] += tag_count
                emissions[word][tag] = int(tokens[0])

    #normalize the counts now
    for word in words:
        for tag in emissions[word]: 
            emissions[word][tag] = float(emissions[word][tag]) / float(count_of_tags[tag])
    
    return emissions

def computeEmissions():
    #read the ner_rare.counts file
    #compute e(x|y) for all x and y

    words, tags = getAllWordsAndTags('ner_rare.counts')

    #emissions[word][tag] -> e(word | tag)
    emissions = dict()

    for word in words:
        emissions[word] = dict()


    #count(y)
    count_of_tags = dict()
    for tag in tags:
        count_of_tags[tag] = 0

    with open('ner_rare.counts') as f:
        for line in f:
            tokens = line.strip().split()
            if(tokens[1] == 'WORDTAG'):
                word = tokens[3]
                tag = tokens[2]
                tag_count = int(tokens[0])
                count_of_tags[tag] += tag_count
                emissions[word][tag] = int(tokens[0])

    #normalize the counts now
    for word in words:
        for tag in emissions[word]: 
            emissions[word][tag] = emissions[word][tag] / count_of_tags[tag]
    
    return emissions




def computeWC():
    #read the ner_rare.counts file
    #compute e(x|y) for all x and y

    words = set()
    tags = set()

    #find out all the distinct words and tags
    with open('ner_rare.counts') as f:
        for line in f:
            tokens = line.strip().split()
            if(tokens[1] == 'WORDTAG'):
                words.add(tokens[3])
                tags.add(tokens[2])
                
    #emissions[word][tag] -> e(word | tag)
    emissions = dict()

    for word in words:
        emissions[word] = dict()

        #by defult if a tag is not assigned to a word => count(x, y) = 0
        for tag in tags:
            emissions[word][tag] = 0

    #count(y)
    count_of_tags = dict()
    for tag in tags:
        count_of_tags[tag] = 0

    with open('ner_rare.counts') as f:
        for line in f:
            tokens = line.strip().split()
            if(tokens[1] == 'WORDTAG'):
                word = tokens[3]
                tag = tokens[2]
                tag_count = int(tokens[0])
                count_of_tags[tag] += tag_count
                emissions[word][tag] = int(tokens[0])
    
    return emissions


# In[ ]:


def isRare(emissions, x):
    return (x not in emissions)


# In[ ]:


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


# In[ ]:


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

def getRareWords_(count_of_words):
    rare_words = [word for word in count_of_words if count_of_words[word] < 5]
    return rare_words

def getRareWords():
    count_of_words = getWordCount()
    rare_words = getRareWords_(count_of_words)
    return rare_words

