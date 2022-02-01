"""
Matthew Shvorin
Emmy Veselinov
Project with a Partner: Talk Like a Pirate
"""

def createdict(filename): 
    a_dict = {}
    file = open(filename).readlines()
    for line in file:
        line = line.strip('\n')
        splitline = line.split(':') # turns it into a list, splits into two arguments (first is the key, second is the value)
        key = splitline[0]
        value = splitline[-1]
        a_dict[key] = value
    return a_dict

def sentence_generator(piratesub_file,textfile):
    piratedict = createdict(piratesub_file)
    a_dict = piratedict
    punctuation = "!?.,/;"
    add_punc = ""
    sentence = ""
    
    story = open(textfile).read()
    newlist = story.split()
    
    for word in newlist:

        #if/elif statments for:
        # if the last charater is a punctuation or not
        # if the lowercase word is in the keys
        # if the first letter of the word is uppercase or lowercase
    
        
        if word[-1] in punctuation:
            add_punc = word[-1] # add_punc holds the last punc
            word = word.rstrip(word[-1]) # removes the punc at the end
            
            if word.lower() in a_dict.keys():
                if word[0].isupper() == True: # if the first letter is uppercase
                    word = a_dict[word.lower()]
                    word = word.capitalize()
                    sentence = sentence + word + add_punc + " "
                    
                    add_punc = "" # reset add_punc back to an empty string
                    
                elif word[0].isupper() == False: # if the first letter is lowercase
                    word = a_dict[word]
                    sentence = sentence + word + add_punc + " "
                    
                    add_punc = ""
            
            elif word.lower() not in a_dict.keys():
                sentence = sentence + word + add_punc + " "
                
                add_punc = ""
                
                
        elif word[-1] not in punctuation:
            if word.lower() in a_dict.keys():
                if word[0].isupper() == True:
                    word = a_dict[word.lower()]
                    word = word.capitalize()
                    sentence = sentence + word + " "
                    
                elif word[0].isupper() == False:
                    word = a_dict[word]
                    sentence = sentence + word + " "
                    
            elif word.lower() not in a_dict.keys():
                sentence = sentence + word + " "
    return sentence
                    
    
if __name__ == "__main__":
    replace_with_pirate_translation = sentence_generator("pirate.dat.py","input.txt")
    print("Pirate-speak translation:", replace_with_pirate_translation)
    print("\n")
    replace_with_dubya_translation = sentence_generator("dubya.dat.py","input.txt")
    print("George W. Bush translation:", replace_with_dubya_translation)
    print("\n")
    replace_with_brooklyn_translation = sentence_generator("brooklyn.dat.py", "input.txt")
    print("Brooklyn English translation:", replace_with_brooklyn_translation)
    
    