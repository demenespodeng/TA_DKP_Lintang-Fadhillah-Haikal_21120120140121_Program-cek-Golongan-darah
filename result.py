class goldar():
    def __init__(self, antiA, antiB, antiAB, antiD, darah, rhesus):
        self.antiA = antiA
        self.antiB = antiB
        self.antiAB = antiAB
        self.antiD = antiD
        self.darah  = darah
        self.rhesus = rhesus

    def findgoldar(self):
        if (self.antiA == "Menggumpal") and (self.antiB == "Tidak Menggumpal") and (self.antiAB == "Menggumpal"): #Goldar A
            self.darah =  "A"
        elif (self.antiA == "Tidak Menggumpal") and (self.antiB == "Menggumpal") and (self.antiAB == "Menggumpal"): #Goldar B
            self.darah =  "B"
        elif (self.antiA == "Menggumpal") and (self.antiB == "Menggumpal") and (self.antiAB == "Menggumpal"): #Goldar AB
            self.darah =  "AB"
        elif (self.antiA == "Tidak Menggumpal") and (self.antiB == "Tidak Menggumpal") and (self.antiAB == "Tidak Menggumpal"): #Goldar O
            self.darah =  "O"
        else:
            self.darah =  "ERROR"

    def findrh(self):
        if (self.antiD == "Menggumpal"):
            self.rhesus =  "+"
        elif (self.antiD == "Tidak Menggumpal"):
            self.rhesus =  "-"
        else :
            self.rhesus =  "ERROR"

    def setantiA(self, antiA):
        self.antiA = antiA
        pass
    def setantiB(self, antiB):
        self.antiB = antiB
        pass
    def setantiAB(self, antiAB):
        self.antiAB = antiAB
        pass
    def setantiD(self, antiD):
        self.antiD = antiD
        pass
    def getdarah(self):
        return self.darah
    def getrhesus(self):
        return self.rhesus