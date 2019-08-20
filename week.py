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
        print(','.join(map(str, self.initw)))
        # return res
    def checkABS(self):
        for i in range(len(self.initw)):
            if (self.initw[i].isABS()) and (i not in (1,2,3)):
                #print(self.initw[i]," est absent, on doit le permuter")
                if i == 0 :
                    print("Soir",self.initw[i].isDPM())
                elif i == 4 :
                    print("Early",self.initw[i].isDPM())
                elif i == 5 :
                    print("Early",self.initw[i].isDPM())
                elif i == 6 :
                    print("Late",self.initw[i].isDPM())
                elif i == 7 :
                    print("Late",self.initw[i].isDPM())
                elif i == 8 :
                    print("Soir",self.initw[i].isDPM())
                elif i == 9 :
                    print("Weekend")                    
                