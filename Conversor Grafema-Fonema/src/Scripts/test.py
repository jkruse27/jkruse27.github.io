from hash_map import *
from phoneme_rules import *

k = PhonemeRules()
exceptions = ExceptionHashMap("mapa.txt")
exceptions.create_hash()
lista = input().split()
for i in lista:
    if(exceptions.part_or_total(i) == 1):
        a = exceptions.get_phoneme(i)
        print(i, a)
    elif(exceptions.part_or_total(i) == 2):
        b = k.simplify_word(i)
        x = ''
        w, z = exceptions.get_range_of_part(b)
        ex = exceptions.get_phoneme(i)
        for j in range(w):
            l = k.apply_rule(b, j)
            if(l == None):
                x += '-'
            else:
                x += l
        x += ex
        for j in range(z, len(b)):
            l = k.apply_rule(b, j)
            if(l == None):
                x += '-'
            else:
                x += l
        print(i, x)
    else:
        b = k.simplify_word(i)
        for j in range(len(i)):
            x = k.apply_rule(b, j)
            if x:
                print(x, end='')
            else:
                 print('-', end='')
        print()

            

