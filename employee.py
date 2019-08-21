class employee:
    def __init__(self,name,dpm):
        self.name=name
        self.dpm=dpm
        self.listABS=[]
        self.listDPM=[]
        filename=self.name+".txt"
        fd= open(filename,"r")
        line=fd.readline()
        self.listABS=line.split(',')
        self.absences=self.listABS[0]
    def print(self):
        print("Nom: ",self.name, "Absences: ",self.absences, "DPM: ",self.dpm)
    def __str__(self):
        return(self.name)
    def isABS(self):
        return int(self.absences)
    def isDPM(self):
        return int(self.dpm)
    def setABS(self,absences):
        self.absences=absences
    def setDPM(self,dpm):
        self.dpm=dpm
    def reload(self,nw):
        self.absences=self.listABS[nw]