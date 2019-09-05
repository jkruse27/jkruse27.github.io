# Class responsible for applying all the phonetic translations and
# simplifications that are invariable (do not need the probabilistic
# analysis)

class PhonemeRules:
    
    def __init__(self):
        pass
    
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
        char = word[char_num].lower()
        ret = ""
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
            ret = 'Z'
        else:
            ret = None

        return ret
