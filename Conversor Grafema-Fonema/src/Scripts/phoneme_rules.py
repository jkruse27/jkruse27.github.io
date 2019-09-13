# Class responsible for applying all the phonetic translations and
# simplifications that are invariable (do not need the probabilistic
# analysis)

class PhonemeRules:
    vogais = []

    def __init__(self):
        self.vogais = ['a', 'i', 'u', 'e', 'o', 'ã', 'â', 'í', 'ú', 'ê', 'ô', 'é', 'ó', 'õ']
    
    # Simplifies the words so that each character corresponds to 
    # one single phoneme and each digraph only correspond to one 
    # phoneme too
    
    # Receives word String and returns this word with unicharacters

    def simplify_word(self, word):
        new_word = ""
        word = word.lower()
        for i in range(len(word)):
            if(i == 0 and word[i] == 'h'):
                pass
            elif(word[i] == 'ç'):
                new_word += 'S'
            elif(i < (len(word) - 1) and word[i] == 'x' and word[i+1] == 'c'):
                new_word += 'S'
            elif(i < (len(word) -1) and word[i] == 'l' and word[i+1] == 'h'):
                new_word += '!' 
            elif(i < (len(word) - 1) and word[i] == 's' and word[i + 1] == 's'):
                new_word += '$'
            elif(i >= 1 and word[i] == 's' and word[i - 1] == 's'):
                pass
            elif(i < (len(word) - 1) and word[i] == 'n' and word[i + 1] == 'h'):
                new_word += '@'
            elif(i < (len(word) - 1) and[i] == 'c' and word[i + 1] == 'h'):
                new_word += '%'
            else:
                new_word += word[i]

        return new_word


    # Method responsible for applying the phonetic rules to individual
    # characters in a word.
    
    # Receives the word String and an int with the characters position
    # Returns the characters correspondent phoneme or null in case the 
    # probabilistic analysis is required
    
    def apply_rule(self, word, char_num):
        size = len(word)
        word = word.lower()
        char = word[char_num].lower()
        ret = None
        if (char == 'p'):
            ret = 'p'
        elif (char == 'v'):
            ret = 'v'
        elif (char == 't'):
            ret = 't'
        elif (char == 'j'):
            ret = 'j'
        elif (char == 'f'):
            ret = 'f'
        elif (char == '%'):
            ret = 'sh'
        elif (char == '!'):
            ret = 'lh'
        elif (char == '$'):
            ret = 'S'
        elif (char == '@'):
            ret = 'nh'
        elif (char == 'z'):
            ret = 'z'
        elif(char_num >= 1 and char_num < size - 1 and char == 's' and word[char_num - 1] in self.vogais and word[char_num + 1] in self.vogais):
            ret = 'z'
        elif (char_num >= 1 and char == 'x' and word[char_num - 1] == 'a'):
            ret = 'sh'
        elif (char_num >= 1 and char == 'x' and word[char_num - 1] == 'i'):
            ret = 'sh'
        elif (char == 'x' and size < char_num - 1 and word[char_num + 1] in self.vogais):
            if(char_num == 1 and char == 'x' and word[char_num - 1] == 'e'):
                ret = 'z'
            elif(word[0] == 'h' and char == 'x' and word[char_num - 1] == 'e'):
                ret = 'z'
            elif(word[0:2] == "in" or word[0:3] == "pre" or word[0:2] == "co"):
                ret = 'z'
            else:
                ret = 'ks'
        elif(char_num < size - 3 and char_num >= 1):
            if(word[char_num-1:char_num+1] == "ax" and word[char_num+2] not in self.vogais): 
                    if(word[char_num+2] != 'l' and word[char_num+2] != 's' and word[char_num+1] == 'e'):
                        ret = 'sh'
                    elif(word[char_num+1] == 'i'):
                        ret = 'sh'
        elif(char_num == size - 2 and (word[char_num-1:char_num+2]=='axe' or word[char_num-1:char_num+2] == "axe")):
            ret = 'sh'
        elif(char_num < size - 4 and char_num > 0 and word[char_num-1:char_num+3] == "axei" and (word[char_num+3] not in self.vogais)):
            ret = 'sh'
        elif(char_num > 0 and char_num < size - 2 and word[char_num-1:char_num+2] == "axa"):
            ret = 'sh'
        elif(char_num > 0 and char_num < size - 4):
            if(word[char_num-1:char_num+1] == 'ax' and word[char_num+1] in self.vogais and word[char_num+2] == 'i'):
                ret = 'ks'
            elif(word[char_num-1:char_num+2] == 'axi' and wprd[char_num+2] in self.vogais):
                ret = 'ks'
            elif(word[char_num-1:char_num+3] == 'axis'):
                ret = 'ks'
        elif(char_num == size - 1 and word[char_num-1:char_num+1] == "ax"):
            ret = 'ks'
        elif(char_num >= 2 and char_num < size - 2):
            if(word[char_num-1:char_num+1] == 'ix' and word[char_num-2] in self.vogais and word[char_num+2] in self.vogais):
                ret = 'sh'
        elif(char_num >= 1 and char_num < size - 1):
            if(word[char_num-1:char_num+1] == 'ix' and word[char_num+1] in self.vogais):
                ret = 'sh'

        return ret
