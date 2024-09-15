letterscount=int(input(""))
#iterate over letters count to get words as input 
words=[]
for _ in range(letterscount):
  word = input().strip()
  words.append(word)
#iterate over words to extract a sing word
for word in words:
    letters=[]
    #checking for abbrevation words
    if len(word)>10:
        #iterate over letter in a word to print abbrevation
        for letter in word:
         letters.append(letter)
         abbcount= len(letters[1:-1])#slice first and last character
        print(letters[0]+str(abbcount)+letters[-1])
    else:
        print(word)    


