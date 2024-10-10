#DivisorGrid=[]
countmemo={}
divisormemo={}
currentdivisor=[]
sumfunc=0

def add_value(key, value):
    if key in divisormemo:
        divisormemo[key].append(value)  # Add value to existing list
    else:
        divisormemo[key] = [value]

def count_divisors(num):
    if num in countmemo:
     #DivisorGrid.append(divisormemo[num])
     return countmemo[num]
    divisors_count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors_count += 1  # Count the divisor
            #DivisorGrid.append(i)
            add_value(num,i)
            if i != num // i:
                divisors_count += 1  # Count the complement divisor
                #DivisorGrid.append(num//i)
                add_value(num,num//i)
    countmemo[num]=divisors_count
    return divisors_count


IntCaseCount= int(input(""))
if 1 <= IntCaseCount <= 10**4:
    LineGrids=[]
    nodes=[]
    for _ in range(IntCaseCount):
     StrLine= input("")
     ListLine= list(map(int,StrLine.split()))
     LineGrids.append(ListLine)
    for LineGrid in LineGrids:
        n= LineGrid[0]
        k= LineGrid[1]
        d= LineGrid[2]
        #DivisorGrid.clear()
        if 1 <= n <= 10**9 and 1 <= k <= 10**5 and 1 <= d <= 10**5:  
            sumfunc = 0
        nodes = [x for x in range(1, n + 1)]  # Create a list of nodes from 1 to n

        for dval in range(d):
            if dval > 0:
                # Reset nodes if dval > 0
                nodes = list(divisormemo.keys())  # Use the keys from divisormemo
                
            for node in nodes:
                currentdivisor.append(node)
                divisor_count = count_divisors(node)
                sumfunc += divisor_count ** k
    print(sumfunc)
    print(divisormemo)
            
