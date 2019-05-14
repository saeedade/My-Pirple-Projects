class Vehicle:
    def __init__(self, Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance= NeedsMaintenance
        self.TripsSinceMaintenance=TripsSinceMaintenance

    def getModel(self):
        return self.Model

    def getMake(self):
        return self.Make
    
    def getYear(self):
        return self.Year
    
    def getWeight(self):
        return self.Weight

    def setMake(self, Make):
        self.Make = Make

    def setModel(self,Model):
        self.Model = Model

    def setYear(self,Year):
        self.Year = Year

    def setWeight(self,Weight):
        self.Weight = Weight


class Cars(Vehicle):
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0,isDriving=False):
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0)
        self.isDriving = isDriving

    def Drive(self):
        self.isDriving = True
      #  print("Driving",self.isDriving)

    def Stop(self):
        self.isDriving = False
        if self.isDriving == False:
            self.TripsSinceMaintenance += 1
            print("Trips: ", self.TripsSinceMaintenance)
        if self.TripsSinceMaintenance <= 3:
            self.NeedsMaintenance = False
            print("Need Maintenance: ", self.NeedsMaintenance,"\n")
        if self.TripsSinceMaintenance > 3:
            self.NeedsMaintenance = True
            print("Need Maintenance: ", self.NeedsMaintenance)
            print("Sending for Repairing")
            self.repair()
        

    def repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False
        print("Vehical is Repaired &  RESET","\n")

    def st(self):
        print("Make: " + self.Make +"\n" + \
               "Model: " + self.Model + "\n" + \
               "Year: " + self.Year + "\n" + \
               "Weight: " + self.Weight 
             )

Ford_GT = Cars("Ford","GT","1966","1520",True)



Ford_GT.st()
Ford_GT.Drive()
Ford_GT.Stop()
Ford_GT.st()
Ford_GT.Drive()
Ford_GT.Stop()
Ford_GT.st()
Ford_GT.Drive()
Ford_GT.Stop()
Ford_GT.st()
Ford_GT.Drive()
Ford_GT.Stop()
Ford_GT.st()
Ford_GT.Drive()
Ford_GT.Stop()
Ford_GT.st()
Ford_GT.Drive()
Ford_GT.Stop()
