import random
random.seed()


class board:

    def __init__(self):
        self.VMB = ""
        self.table =[]
        self.x = 0
        self.y = 0

    def setMboard(self, mbstr):
        
        mbList = mbstr.split(",")
        validM = []
        for i in range(0, len(mbList)):
            if mbList[i] == "-1" or mbList[i] == "-1\n":
                validM.append(i)
        
        if len(validM) == 1:
            self.VMB = str(validM[0])
            check = "single"
            
        elif len(validM) > 1 and len(validM)<9:
            check = "Multiple"
            choice = random.choice(validM)
            self.VMB = str(choice)
                  
        else:
            self.VMB = str(random.randint(0,8))
            check = "random"
            
        

    def setBoard(self,bstr):
        bList = bstr.split(",")
        self.table = []
        
        a = ["0","1","2","3","4","5","6","7","8"]
        b = ["9","10","11","12","13","14","15","16","17"]
        c = ["18","19","20","21","22","23","24","25","26"]
        d = ["27","28","29","30","31","32","33","34","35"]
        e = ["36","37","38","39","40","41","42","43","44"]
        f = ["45","46","47","48","49","50","51","52","53"]
        g = ["54","55","56","57","58","59","60","61","62"]
        h = ["63","64","65","66","67","68","69","70","71"]
        i = ["72","73","74","75","76","77","78","79","80"]
        self.table.append(a)
        self.table.append(b)
        self.table.append(c)
        self.table.append(d)
        self.table.append(e)
        self.table.append(f)
        self.table.append(g)
        self.table.append(h)
        self.table.append(i)
        for i in range(0,len(self.table)):
            test = self.table[i]
            for j in test:
                ind = test.index(j)
                self.table[i][ind] = bList[int(j)]
                
    def randXY(self):

        if self.VMB == '0':
            self.x = random.randint(0,2)
            self.y = random.randint(0,2)
        elif self.VMB == '1':
            self.x = random.randint(3,5)
            self.y = random.randint(0,2)
        elif self.VMB == '2':
            self.x = random.randint(6,8)
            self.y = random.randint(0,2)
        elif self.VMB == '3':
            self.x = random.randint(0,2)
            self.y = random.randint(3,5)
        elif self.VMB == '4':
            self.x = random.randint(3,5)
            self.y = random.randint(3,5)
        elif self.VMB == '5':
            self.x = random.randint(6,8)
            self.y = random.randint(3,5)
        elif self.VMB == '6':
            self.x = random.randint(0,2)
            self.y = random.randint(6,8)
        elif self.VMB == '7':
            self.x = random.randint(3,5)
            self.y = random.randint(6,8)
        elif self.VMB == '8':
            self.x = random.randint(6,8)
            self.y = random.randint(6,8)
        

    def getlegal(self):
        
        legal = False

        while legal == False:
                
            self.randXY()
            
            if self.table[self.y][self.x] == "0":
                legal = True
            else:
                legal = False


        
        
        
