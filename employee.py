class employee:
    def __init__(self,name,absences,dpm):
        self.name=name
        self.absences=absences
        self.dpm=dpm
    def print(self):
        print("Nom: ",self.name, "Absences: ",self.absences, "DPM: ",self.dpm)
    def __str__(self):
        return(self.name)
    def isABS(self):
        return self.absences
    def isDPM(self):
        return self.dpm