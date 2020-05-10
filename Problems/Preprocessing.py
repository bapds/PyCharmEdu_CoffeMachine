"""
Solution of Problem of the day
solved this problem of the day 
BAPDS in 10/05/2020
"""

def tratment_string(entrada):
    ex = "!.,;:?"
    newtext = ''
    for caracter in entrada:
        for compare in ex:
            if caracter == compare:
                ok = False
                break
            ok = True
        if ok:
            newtext += caracter
    return newtext.lower()


print(tratment_string(input()))
