problemscount= int(input(""))
if problemscount<=1000 and problemscount>=1:
    problemsreports = []
    problemsolvecount=0
    for _ in range(problemscount):
        problemsreport= input("").strip()
        problemsreport= problemsreport.replace(' ','')
        problemsreports.append(problemsreport)

    for problemreport in problemsreports:
        solutioncount=0
        for problemanalysis in problemreport:
            if problemanalysis =="1":
                solutioncount+=1
        if solutioncount>=2:
         problemsolvecount+=1
    print(problemsolvecount)
        
          
  



    