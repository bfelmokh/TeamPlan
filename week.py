from employee import employee
class week:
    def __init__(self,initw):
        self.initw=initw
    def shifting(self):
        neww=self.initw.copy()
        self.initw = self.initw[-2:] + self.initw[:-2]
        self.initw[0],self.initw[1]=neww[-2],neww[-3]
        return self.initw.copy()
    def __str__(self):
        #for i in range (len(self.initw)):
        #    print(self.initw[i])
        #print(','.join(map(str, self.initw)))
        return (','.join(map(str, self.initw)))
    def checkABS(self,nw):
        for i in range(len(self.initw)):
            self.initw[i].reload(nw)
            if (self.initw[i].isABS()) and (i not in (1,2,3)):
                #print(self.initw[i]," est absent, on doit le permuter")
                if i == 0 :
                    print(self.initw[i],"= Soir , DPM = ",self.initw[i].isDPM())
                elif i == 4 :
                    print(self.initw[i],"= Early , DPM = ",self.initw[i].isDPM())
                elif i == 5 :
                    print(self.initw[i],"= Early , DPM = ",self.initw[i].isDPM())
                elif i == 6 :
                    print(self.initw[i],"= Late , DPM = ",self.initw[i].isDPM())
                elif i == 7 :
                    print(self.initw[i],"= Late , DPM = ",self.initw[i].isDPM())
                elif i == 8 :
                    print(self.initw[i],"= WEEKEND , DPM = ",self.initw[i].isDPM())                   
        print ('Génération nouveau planning suite à l\'absence ...')
        print ('Rien à faire, décision non prise en compte\n -----------')