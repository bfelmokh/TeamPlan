from employee import employee
from week import week
initw=[employee('A',0,0),employee('B',0,0),employee('C',0,0),employee('D',1,0),employee('E',0,0),employee('F',0,0),employee('G',0,0),employee('H',0,0),employee('B',0,0)]
#CIBLE=[HGABCDEFG]
#CIBL2=[FEHGABCDE]
S0 = week(initw)
#S0.print()
S1=[]
S0.__str__()
S1=S0.shifting()
S0.__str__()
S0.checkABS()
S1=S0.shifting()
S0.__str__()
S1=S0.shifting()
S0.__str__()