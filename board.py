import random
random.seed()


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
            self.choice = random.choice(validM)
                  
        else:
            self.VMB = str(random.randint(0,8))
            check = "random"
            
        with open('mbfile.txt', 'a') as the_file:
            the_file.write(check + str(self.VMB)+'\n')
        

    def setBoard(self,bstr):
        bList = bstr.split(",")
        
        a = ["0","1","2","9","10","11","18","19","20"]
        b = ["3","4","5","12","13","14","21","22","23"]
        c = ["6","7","8","15","16","17","24","25","26"]
        d = ["27","28","29","36","37","38","45","46","47"]
        e = ["30","31","32","39","40","41","48","49","50"]
        f = ["33","34","35","42","43","44","51","52","53"]
        g = ["54","55","56","63","64","65","72","73","74"]
        h = ["57","58","59","66","67","68","75","76","77"]
        i = ["60","61","62","69","70","71","78","79","80"]
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
                for j in range (0,len(i)):
                    the_file.write(str(i[j]))
                    if j == 2 or j == 5 or j == 8:
                        the_file.write("\n")
                the_file.write("\n")
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
        with open("tester.txt","a+") as myfile:
                myfile.write(str(x) + str(y))
        return x, y

        
