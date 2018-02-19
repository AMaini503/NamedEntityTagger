import datetime
class RareWordClassifier:
    def __init__(self, count_of_words):
        self.count_of_words = count_of_words
    def classify(self, word):
        

        if(word not in self.count_of_words or (word in self.count_of_words and self.count_of_words[word] < 5)):
            #classify as if numbers only
            if(word.isnumeric() and len(word) == 2):
               return "_TWO_DIGIT_NUM_"
            if(word.isnumeric() and len(word) == 4):
               return "_FOUR_DIGIT_NUM_"
            if(not word.isalpha() and word.isalnum()):
               return "_DIGIT_AND_ALPHA_"
                 
            tokens = word.split("-")
            if(len(tokens) == 2 and len(tokens[0]) > 1 and len(tokens[1]) > 1 and tokens[0].isnumeric() and tokens[1].isnumeric()):
                return "_DIGIT_AND_DASH"
            
            #check for date in month/day/year format (2 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%m/%d/%y")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass

            #check for date in month/day/Year format (4 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%m/%d/%Y")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass
            
            #check for date in day/month/year format (2 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%d/%m/%y")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass

            #check for date in day/month/Year format (4 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%d/%m/%Y")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass
            
            #check for date in month-day-year format (2 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%m-%d-%y")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass
            
            #check for date in month-day-year format (4 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%m-%d-%Y")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass
            
             
            #check for date in day-month-year format (2 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%d-%m-%y")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass
            
            #check for date in day/month/Year format (4 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%d-%m-%Y")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass
            
            #check for date in day-month-year format (2 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%y-%m-%d")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass
            
            #check for date in day/month/Year format (4 digit year)
            try:
                date_object = datetime.datetime.strptime(word, "%Y-%m-%d")
                return "_DIGIT_AND_SLASH_"
            except Exception as e:
                pass
            
            tokens = word.split(".")
            if(len(tokens) == 2 and (tokens[0].isnumeric() or len(tokens[0]) == 0) and tokens[1].isnumeric()):
                return "_DIGIT_AND_PERIOD_"
           
            if(word.isnumeric()):
               return "_OTHERNUM_"

            if(word.isupper()):
                return "_ALL_CAPS_"
            if(len(word) == 2 and (word[0] >= 'A' and word[0] <= 'Z')):
                return '_CAP_PERIOD_'
            if(word.istitle()):
                return '_INIT_CAP_'
            if(word.islower()):
                return '_LOWERCASE_'
            return '_OTHER_'
        else:
            return word            
