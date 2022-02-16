#Installing the required packages
!pip install pyspellchecker


from spellchecker import SpellChecker

spell = SpellChecker()
def spellcheckr():
    text = input('Enter your text here:',)
    dict_of_autocorrect_words = {}
    for i in spell.unknown(text.split()):
        dict_of_autocorrect_words[i] = spell.correction(i)

    print(f'The AUTOCORRECT suggestions are Mis-spelled words are {dict_of_autocorrect_words}')

    temp = text.split()
    res = []
    for wrd in temp:
        res.append(dict_of_autocorrect_words.get(wrd, wrd))
    res = ' '.join(res)
    return(res)

spellcheckr()
