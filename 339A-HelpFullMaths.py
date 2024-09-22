operationstring= input("")
strsplit=operationstring.split('+')
if(len(strsplit)<=100):
    orderbyoperationalstring = '+'.join(sorted(strsplit))
    print(orderbyoperationalstring)
