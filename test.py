st = 'this is a test string'

def Capitalize(st):
    for word in st.split():
        newstring = ''
        if len(word) > 1:
            word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            word = word[0].upper()
        newstring += word
        print(word)
Capitalize(st)
