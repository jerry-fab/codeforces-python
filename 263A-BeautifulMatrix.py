grid=[]
n=5
for _ in range(n):
  line = input()
  row= list(map(int,line.split()))
  grid.append(row)
flattenlist = [item for row in grid for item in row]
onepossition=flattenlist.index(1)
onepossition=grid.index(1)
zerocount= flattenlist.count(0)
onecount= flattenlist.count(1)
onepossition=flattenlist.index(1)
#if(zerocount==24 and onecount==1):
   

