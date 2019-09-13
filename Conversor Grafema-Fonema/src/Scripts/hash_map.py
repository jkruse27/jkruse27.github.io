# Class responsible for the exceptions dictionary

class ExceptionHashMap:
    
    address = ''
    #dic_s is for words that are exceptions by themselves
    dic_s = {}
    #dic_c is for words that are exceptions and their derivatives are exceptions too
    dic_c = {}

    # When initialized it requires the address where the 
    # hash map will be stored and recovered from

    def __init__(self, address):
        self.address = address

    
    # Returns the phoneme translation to a word in the case it is
    # in the exceptions dictionary

    def get_phoneme(self, word):
        ret = ""
        
        if(word.lower() in self.dic_s):
            return self.dic_s[word.lower()]
        for i in self.dic_c:
            if(i in word.lower()):
                ret = self.dic_c[i]
                break
        return ret
    
    
    # Adds another exception to the dictionary
    # Requires the word and it's translation and if it is simple or composite

    def add_exception(self, grapheme, phoneme, form):
        if(form.lower() == 'simple'):
            if(grapheme.lower() not in self.dic_s):
                self.dic_s[grapheme.lower()] = phoneme
        else:
            if(grapheme.lower() not in self.dic_c):
                self.dic_c[grapheme.lower()] = phoneme
    
    # Removes a word from the dictionary

    def remove_exception(self, word, form):
        if(form.lower() == 'simple'):
            if(word.lower() in self.dic_s):
                self.dic_s.pop(word.lower())
        else:
            if(word.lower() in self.dic_c):
                self.dic_c.pop(word.lower())

    
    # Creates the dictionary from the file in the address
    
    def create_hash(self):
        arq = open(self.address, "r")
        for line in arq:
            if(line.lower() == "simples\n"):
                continue
            elif(line.lower() == '\n'):
                continue
            elif(line.lower() == "composto\n"):
                break
            else:
                line = line.split()
                self.dic_s[line[0].lower()] = line[1]
        for line in arq:
            if(line != "\n"):
                line = line.split()
                self.dic_c[line[0].lower()] = line[1]

    
    # Stores the hash map in the file in the address

    def store_hash(self):
        arq = open(self.address, "r")
        arq.write("Simples")
        for word in self.dic_s:
            arq.write(word.lower(), self.dic[word])
        for word in self.dic_c:
            arq.write(word.lower(), self.dic[word])
        arq.close()

    # Finds if part of a word is  a exception or the whole word

    def part_or_total(self, word):
        if(word.lower() in self.dic_s):
            return 1
        for i in self.dic_c:
            if i in word:
                return 2
        return 0

    #Returns the beggining and end of the part for which the exception applies

    def get_range_of_part(self, word):
        for i in self.dic_c:
            if(i in word.lower()):
                a = word.lower().find(i)
                return a, a+len(i)
