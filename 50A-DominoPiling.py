rowscolumnscount= input()
rowscolumnscount = rowscolumnscount.split()
rowscolumnscount = [int(x) for x in rowscolumnscount]
if(rowscolumnscount[0]>=1 and rowscolumnscount[0]<=16 and rowscolumnscount[1]>=1 and rowscolumnscount[1]<=16):
    dominoescoount = int((rowscolumnscount[0]*rowscolumnscount[1])/2)
    print(dominoescoount)
