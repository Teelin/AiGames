import random
random.seed()

with open('mbfile.txt', 'a') as the_file:
    the_file.seek(0)
    the_file.truncate()
with open("bfile.txt","a+") as file:
    file.seek(0)
    file.truncate()

class board:

    def __init__(self):
        self.VMB = ""
        self.table =[]

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
            
        with open('mbfile.txt', 'a') as the_file:
            the_file.write(check + str(self.VMB)+'\n')
        

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

        with open('bfile.txt', 'a') as the_file:
            for i in self.table:
                the_file.write(str(i) + "\n")
            the_file.write("\n\n")
                
    def randXY(self):

        if self.VMB == '0':
            x = random.randint(0,2)
            y = random.randint(0,2)
        elif self.VMB == '1':
            x = random.randint(3,5)
            y = random.randint(0,2)
        elif self.VMB == '2':
            x = random.randint(6,8)
            y = random.randint(0,2)
        elif self.VMB == '3':
            x = random.randint(0,2)
            y = random.randint(3,5)
        elif self.VMB == '4':
            x = random.randint(3,5)
            y = random.randint(3,5)
        elif self.VMB == '5':
            x = random.randint(6,8)
            y = random.randint(3,5)
        elif self.VMB == '6':
            x = random.randint(0,2)
            y = random.randint(6,8)
        elif self.VMB == '7':
            x = random.randint(3,5)
            y = random.randint(6,8)
        elif self.VMB == '8':
            x = random.randint(6,8)
            y = random.randint(6,8)
        
        return x, y

    def getlegal(self):
        
        legal = False

        while legal == False:
                
            x, y = self.randXY()
            if self.table[y][x] == "0":
                legal = True
            else:
                legal = False
        with open("tester.txt","a+") as testfile:
            testfile.write(str(x) + str(y) + "\n")

        return x, y

        
        
        
