import re
print('shembeteng'.replace('mbete',''))
def translate(word):
    vwlsearch=re.compile(r'[a{1}e{1}i{1}o{1}u{1}]')
    fnd=vwlsearch.search(word)
    vwl=fnd.group()
    endl=fnd.start()+1
    ln=len(word)+1
    trans=''
    if vwl=='a':
        trans=word[0:endl]+'mbata'+word[endl:ln]
    if vwl=='e':
        trans=word[0:endl]+'mbete'+word[endl:ln]
    if vwl=='i':
        trans=word[0:endl]+'mbiti'+word[endl:ln]
    if vwl=='o':
        trans=word[0:endl]+'mboto'+word[endl:ln]
    if vwl=='u':
        trans=word[0:endl]+'mbutu'+word[endl:ln]       
    return trans
# code runner
while True:
    sentence=input("Enter a word to translate to shembeteng\n")
    words=sentence.split()
    shembetence=[]
    for wrd in words:
        shembetence.append(translate(wrd))
    print(' '.join(shembetence))