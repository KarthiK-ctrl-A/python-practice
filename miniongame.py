def minion_game(string):
    s = len(string)
    vow = con = 0
    for i in range(s):
        if string[i] in 'AEIOU':          #getting vowels word count
            vow = vow + (s-i)             #s-i returns the count of word with vowel
        else:                             #getting consonants word count
            con = con + (s-i)             #s-i returns the count of word with consonant
            
    if con>vow:
        print("Stuart {}".format(con))
    elif con==vow:
        print("Draw")
    else:
        print("Kevin {}".format(vow))

if __name__ == '__main__':
    s = input()
    minion_game(s)