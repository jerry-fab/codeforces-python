Strname= input("")
if(len(Strname)<=100 and len(Strname)>=1):
    distinct_Strname= set(Strname)
    if(len(distinct_Strname)%2==0):
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")