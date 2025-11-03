# Python regularni izrazi
import re

# Uvod u regularne izraze
def test_re(txt,uzorci=[]):
    """
        Program za provjeru regularnih izraza.       
    """
    for uzorak,opis in uzorci:
        print('-'*20)
        print('=> Uzorak %s (%s)' % (uzorak,opis))
        print('%r' % txt)
        
        for nasli in re.finditer(uzorak,txt):
            s = nasli.start()
            e = nasli.end()
            nasli = txt[s:e]
            n_kosih = txt[:s].count('\\')
            prefix = '.' * (s + n_kosih)
            print(' %s%r' % (prefix,nasli))

