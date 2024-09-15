participantscorecount=input()
participantscorecount= participantscorecount.split()
participantscorecount= [int(x) for x in participantscorecount]
if(participantscorecount[0]>=1 and participantscorecount[0]<=50 and participantscorecount[1]>=1 and participantscorecount[1]<=50):
  advancecount=0
  participantscore=input()
  participantscores= participantscore.split()
  participantscores=[int(x) for x in participantscores]
  for participantscore in participantscores:
     if(participantscore>=0 and participantscore<=100):
            if(participantscore>=participantscores[participantscorecount[1]-1] and participantscore>0):
                advancecount=advancecount+1
  print(advancecount)
