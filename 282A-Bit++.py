bitinputcount= int(input(""))
if(bitinputcount>=1 and bitinputcount<=150):
    bit=0
    for _ in range(bitinputcount):
     bitinput= input()
     if(bitinput=="++X" or bitinput=="X++"):
        bit=bit+1
     else:
        bit=bit-1
    print(bit)
    