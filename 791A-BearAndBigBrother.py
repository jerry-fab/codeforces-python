BearWeight = input("")
BearWeight = BearWeight.split()
BearWeight= [int(x) for x in BearWeight]
if(BearWeight[0]<=BearWeight[1] and BearWeight[0]>=1 and BearWeight[0]<=10 and BearWeight[1]>=1 and BearWeight[1]<=10):
    BearWeightcount=0
    while(True):
        BearWeight[0]*=3
        BearWeight[1]*=2
        BearWeightcount+=1
        if(BearWeight[0]>BearWeight[1]):
            break
    print(BearWeightcount)