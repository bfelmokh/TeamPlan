from employee import employee
from week import week
initw=[employee('A',0),employee('B',0),employee('C',0),employee('D',1),employee('E',0),employee('F',0),employee('G',0),employee('H',0),employee('B',0)]
#CIBLE=[HGABCDEFG]
#CIBL2=[FEHGABCDE]
S0 = week(initw)
#S0.print()
S1=[]
nw=0
print("Semaine Initial: ",S0)
S0.checkABS(nw)
S1=S0.shifting()
print("Rotation semaine 1: ",S0)
S0.checkABS(nw)
S1=S0.shifting()
print("Rotation semaine 2: ",S0)
S0.checkABS(nw)
S1=S0.shifting()
print("Rotation semaine 3: ",S0)
S0.checkABS(nw)