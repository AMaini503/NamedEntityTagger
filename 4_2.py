#!/usr/bin/python3
import numpy as np
from aux import computeEmissions, isRare



def findTagAndMaxEmission(emissions, x):
    emissions_for_x = emissions[x]
    return max(emissions_for_x.items(), key = lambda x: x[1])




def writeTagsForDev(emissions):
    with open('ner_dev.dat') as f_input, open('4_2.txt', 'w') as f_output:
        for line in f_input:
            tokens = line.strip().split()
            
            line_written_to_output = ''
            
            #not a new line
            if(len(tokens) > 0):
                
                #x is modified to _RARE_ if it is qualifies as _RARE_. It is used to index emissions
                x = tokens[0]
                
                #word is used when writing to the output file, this is not modified
                word = tokens[0]
                
                if(isRare(emissions, word)):
                    x = '_RARE_'
                
                tag, max_emission = findTagAndMaxEmission(emissions, x)
                log_max_emission = np.log(max_emission)
                line_written_to_output = ' '.join([word, 
                                                   tag,
                                                  '{}'.format(log_max_emission)])
                line_written_to_output = line_written_to_output + '\n'
            else:
                line_written_to_output = '\n'
            
            f_output.write(line_written_to_output)
                    




emissions = computeEmissions()
writeTagsForDev(emissions)

