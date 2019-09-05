from hash_map import *
from phoneme_rules import *

k = PhonemeRules()
exceptions = ExceptionHashMap("mapa.txt")
exceptions.create_hash()
lista = ["palavra", "fdddes", "amendoim", "linha", "galhozinho"]
for i in lista:
    a = exceptions.get_phoneme(i)
    if (a != ""):
        print(i, a)
    else:
        for j in range(len(i)):
            b = k.simplify_word(i)
            x = k.apply_rule(b, j)
            if x:
                print(x, end='')
            else:
                print('-', end='')
        print()

            

