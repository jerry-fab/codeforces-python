stringwithvowels= input("")
vowels = "aeiouyAEIOUY"
stringwithoutvowels = ''.join(char for char in stringwithvowels if char not in vowels)
if len(stringwithvowels) <=100 and len(stringwithvowels)>=1:
    concatstring =  '.'+'.'.join(char for char in stringwithoutvowels)
print(concatstring.lower())