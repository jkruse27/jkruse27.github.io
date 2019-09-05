# Class responsible for the exceptions dictionary

class ExceptionHashMap:
    
    address = ''
    dic = {}
    
    # When initialized it requires the address where the 
    # hash map will be stored and recovered from

    def __init__(self, address):
        self.address = address

    
    # Returns the phoneme translation to a word in the case it is
    # in the exceptions dictionary

    def get_phoneme(self, word):
        ret = ""
        
        if(word.lower() in self.dic):
            ret = self.dic[word.lower()]
        
        return ret
    
    
    # Adds another exception to the dictionary
    # Requires the word and it's translation

    def add_exception(self, grapheme, phoneme):
        if(grapheme.lower() not in self.dic):
            self.dic[grapheme.lower()] = phoneme
    
    
    # Removes a word from the dictionary

    def remove_exception(self, word):
        if(word.lower() in self.dic):
            self.dic.pop(word.lower())

    
    # Creates the dictionary from the file in the address
    
    def create_hash(self):
        arq = open(self.address, "r")
        for line in arq:
            line = line.split()
            self.dic[line[0].lower()] = line[1]

    
    # Stores the hash map in the file in the address

    def store_hash(self):
        arq = open(self.address, "r")
        for word in self.dic:
            arq.write(word.lower(), self.dic[word])
        arq.close()


