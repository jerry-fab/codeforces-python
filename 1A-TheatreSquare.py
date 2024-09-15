import math

lnthbreadtharea = input("")
attributes = [int(digit) for digit in lnthbreadtharea.split()]
result= False
#attributes = np.array(attributes)
#result=np.all((attributes >= 1) & (attributes <= pow(10, 9)))
for element in attributes:
    if element < 1 or element > pow(10, 9):
        result = False
        break
    else:
        result=True
        
if(result):
    lengthcalc= math.ceil(attributes[0]/attributes[2]) 
    breadthcalc= math.ceil(attributes[1]/attributes[2])
    print(lengthcalc*breadthcalc)

        