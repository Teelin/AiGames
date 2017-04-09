import random
random.seed()


class board:

    def __init__(self):
        self.validM = []
        self.VMB = ""
        self.table =[]
        self.board1 =[]
        self.board2 =[]
        self.board3 =[]
        self.board4 =[]
        self.board5 =[]
        self.board6 =[]
        self.board7 =[]
        self.board8 =[]
        self.board9 =[]
        self.x = 0
        self.y = 0
        myid = 0
        oppid = 0

    def setMboard(self, mbstr):
        
        mbList = mbstr.split(",")
        self.validM = []
        for i in range(0, len(mbList)):
            if mbList[i] == "-1" or mbList[i] == "-1\n":
                self.validM.append(i)            
        

    def setBoard(self,bstr):
        bList = bstr.split(",")
        self.table = []
        a = ["0","9","18","27","36","45","54","63","72"]
        b = ["1","10","19","28","37","46","55","64","73"]
        c = ["2","11","20","29","38","47","56","65","74"]
        d = ["3","12","21","30","39","48","57","66","75"]
        e = ["4","13","22","31","40","49","58","67","76"]
        f = ["5","14","23","32","41","50","59","68","77"]
        g = ["6","15","24","33","42","51","60","69","78"]
        h = ["7","16","25","34","43","52","61","70","79"]
        j = ["8","17","26","35","44","53","62","71","80"]
        for i in range(len(a)):
            a[i] = bList[int(a[i])]
        for i in range(len(b)):
            b[i] = bList[int(b[i])]
        for i in range(len(c)):
            c[i] = bList[int(c[i])]
        for i in range(len(d)):
            d[i] = bList[int(d[i])]
        for i in range(len(e)):
            e[i] = bList[int(e[i])]
        for i in range(len(f)):
            f[i] = bList[int(f[i])]
        for i in range(len(g)):
            g[i] = bList[int(g[i])]
        for i in range(len(h)):
            h[i] = bList[int(h[i])]
        for i in range(len(j)):
            j[i] = bList[int(j[i])]
        self.table.append(a)
        self.table.append(b)
        self.table.append(c)
        self.table.append(d)
        self.table.append(e)
        self.table.append(f)
        self.table.append(g)
        self.table.append(h)
        self.table.append(j)

        self.board1 = ["0","1","2","9","10","11","18","19","20"]
        self.board2 = ["3","4","5","12","13","14","21","22","23"]
        self.board3 = ["6","7","8","15","16","17","24","25","26"]
        self.board4 = ["27","28","29","36","37","38","45","46","47"]
        self.board5 = ["30","31","32","39","40","41","48","49","50"]
        self.board6 = ["33","34","35","42","43","44","51","52","53"]
        self.board7 = ["54","55","56","63","64","65","72","73","74"]
        self.board8 = ["57","58","59","66","67","68","75","76","77"]
        self.board9 = ["60","61","62","69","70","71","78","79","80"]
        for i in range(len(self.board1)):
            self.board1[i] = bList[int(self.board1[i])]
        for i in range(len(self.board2)):
            self.board2[i] = bList[int(self.board2[i])]
        for i in range(len(self.board3)):
            self.board3[i] = bList[int(self.board3[i])]
        for i in range(len(self.board4)):
            self.board4[i] = bList[int(self.board4[i])]
        for i in range(len(self.board5)):
            self.board5[i] = bList[int(self.board5[i])]
        for i in range(len(self.board6)):
            self.board6[i] = bList[int(self.board6[i])]
        for i in range(len(self.board7)):
            self.board7[i] = bList[int(self.board7[i])]
        for i in range(len(self.board8)):
            self.board8[i] = bList[int(self.board8[i])]
        for i in range(len(self.board9)):
            self.board9[i] = bList[int(self.board9[i])]

        '''with open('bfile.txt', 'a') as the_file:
              for i in self.table:
                  the_file.write(str(i) + "\n")
              the_file.write("\n\n")

        with open('ffile.txt', 'a') as the_file:
            the_file.write(str(self.board1)+"\n")
            the_file.write(str(self.board2)+"\n")
            the_file.write(str(self.board3)+"\n")
            the_file.write(str(self.board4)+"\n")
            the_file.write(str(self.board5)+"\n")
            the_file.write(str(self.board6)+"\n")
            the_file.write(str(self.board7)+"\n")
            the_file.write(str(self.board8)+"\n")
            the_file.write(str(self.board9)+"\n")
            the_file.write("\n\n")'''
                





    def getMacro(self):
        board = []
        
        if len(self.validM) == 1:
            self.VMB = str(self.validM[0])
            check = "single"
            
        elif len(self.validM) > 1 and len(self.validM)<9:
            check = "Multiple"
            self.VMB = "50"
            mywin = False
            for i in self.validM:
                if str(i) == '0':
                    board = self.board1
                    b = '0'
                elif str(i) == '1':
                    board = self.board2
                    b = '1'
                elif str(i) == '2':
                    board = self.board3
                    b = '2'
                elif str(i) == '3':
                    board = self.board4
                    b = '3'
                elif str(i) == '4':
                    board = self.board5
                    b = '4'
                elif str(i) == '5':
                    board = self.board6
                    b = '5'
                elif str(i) == '6':
                    board = self.board7
                    b = '6'
                elif str(i) == '7':
                    board = self.board8
                    b = '7'
                elif str(i) == '8':
                    board = self.board9
                    b = '8'
                    
                if self.wincheck(self.myid,board):
                    self.VMB = b
                    mywin = True
                elif self.wincheck(self.oppid,board) and mywin == False:
                    self.VMB = b
                    
                
            if self.VMB == "50":
                choice = random.choice(self.validM)
                self.VMB = str(choice)
                    
                  
        else:
            self.VMB = str(random.randint(0,8))
            check = "random"
        
        '''with open('bfile.txt', 'a') as the_file:
            
            the_file.write(check + ' '+self.VMB + "\n\n")'''







        
    def getmove(self,pid):
        valid =[]
        myspots =[]
        self.myid = pid
        
        if self.myid == 1:
            self.oppid = 2
        else:
            self.oppid = 1
            
        self.getMacro()
        
        if self.VMB == '0':
            for i in self.board1:
                if i == "0":
                    valid.append(self.board1.index(i))
                elif i == str(self.myid):
                    myspots.append(self.board1.index(i))
            
            if len(valid) == 9:
                self.x = 0
                self.y = 0
            else:

                if self.wincheck(self.myid,self.board1):
                    self.x += 0
                    self.y += 0
                elif self.wincheck(self.oppid,self.board1):
                    self.x += 0
                    self.y += 0
                else:
                    if len(myspots)>0:
                        self.nextTo(myspots,self.board1)
                        self.x += 0
                        self.y += 0
                    else: 
                        self.x = random.randint(0,2)
                        self.y = random.randint(0,2)

        elif self.VMB == '1':
            for i in self.board2:
                if i == "0":
                    valid.append(self.board2.index(i))
                elif i == str(self.myid):
                    myspots.append(self.board2.index(i))
            
            if len(valid) == 9:
                self.x = 3
                self.y = 0
            else:

                if self.wincheck(self.myid,self.board2):
                    self.x += 3
                    self.y += 0
                elif self.wincheck(self.oppid,self.board2):
                    self.x += 3
                    self.y += 0
                else:
                    if len(myspots)>0:
                        self.nextTo(myspots,self.board2)
                        self.x += 3
                        self.y += 0
                    else: 
                        self.x = random.randint(3,5)
                        self.y = random.randint(0,2)
                        
        elif self.VMB == '2':
            for i in self.board3:
                if i == "0":
                    valid.append(self.board3.index(i))
                elif i == str(self.myid):
                    myspots.append(self.board3.index(i))
            
            if len(valid) == 9:
                self.x = 6
                self.y = 0
            else:

                if self.wincheck(self.myid,self.board3):
                    self.x += 6
                    self.y += 0
                elif self.wincheck(self.oppid,self.board3):
                    self.x += 6
                    self.y += 0
                else:
                    if len(myspots)>0:
                        self.nextTo(myspots,self.board3)
                        self.x += 6
                        self.y += 0
                    else: 
                        self.x = random.randint(6,8)
                        self.y = random.randint(0,2)
                        
        elif self.VMB == '3':
            for i in self.board4:
                if i == "0":
                    valid.append(self.board4.index(i))
                elif i == str(self.myid):
                    myspots.append(self.board4.index(i))
            
            if len(valid) == 9:
                self.x = 0
                self.y = 3
            else:

                if self.wincheck(self.myid,self.board4):
                    self.x += 0
                    self.y += 3
                elif self.wincheck(self.oppid,self.board4):
                    self.x += 0
                    self.y += 3
                else:
                    if len(myspots)>0:
                        self.nextTo(myspots,self.board4)
                        self.x += 0
                        self.y += 3
                    else: 
                        self.x = random.randint(0,2)
                        self.y = random.randint(3,5)
                        
        elif self.VMB == '4':
            for i in self.board5:
                if i == "0":
                    valid.append(self.board5.index(i))
                elif i == str(self.myid):
                    myspots.append(self.board5.index(i))
            
            if len(valid) == 9:
                self.x = 3
                self.y = 3
            else:

                if self.wincheck(self.myid,self.board5):
                    self.x += 3
                    self.y += 3
                elif self.wincheck(self.oppid,self.board5):
                    self.x += 3
                    self.y += 3
                else:
                    if len(myspots)>0:
                        self.nextTo(myspots,self.board5)
                        self.x += 0
                        self.y += 0
                    else: 
                        self.x = random.randint(3,5)
                        self.y = random.randint(3,5)
                        
        elif self.VMB == '5':
            for i in self.board6:
                if i == "0":
                    valid.append(self.board6.index(i))
                elif i == str(self.myid):
                    myspots.append(self.board6.index(i))
            
            if len(valid) == 9:
                self.x = 6
                self.y = 3
            else:

                if self.wincheck(self.myid,self.board16):
                    self.x += 6
                    self.y += 3
                elif self.wincheck(self.oppid,self.board6):
                    self.x += 6
                    self.y += 3
                else:
                    if len(myspots)>0:
                        self.nextTo(myspots,self.board6)
                        self.x += 6
                        self.y += 3
                    else: 
                        self.x = random.randint(6,8)
                        self.y = random.randint(3,5)
                    
        elif self.VMB == '6':
            for i in self.board7:
                if i == "0":
                    valid.append(self.board7.index(i))
                elif i == str(self.myid):
                    myspots.append(self.board7.index(i))
            
            if len(valid) == 9:
                self.x = 0
                self.y = 6
            else:

                if self.wincheck(self.myid,self.board7):
                    self.x += 0
                    self.y += 6
                elif self.wincheck(self.oppid,self.board7):
                    self.x += 0
                    self.y += 6
                else:
                    if len(myspots)>0:
                        self.nextTo(myspots,self.board7)
                        self.x += 0
                        self.y += 6
                    else: 
                        self.x = random.randint(0,2)
                        self.y = random.randint(6,8)
                        
        elif self.VMB == '7':
            for i in self.board8:
                if i == "0":
                    valid.append(self.board8.index(i))
                elif i == str(self.myid):
                    myspots.append(self.board8.index(i))
            
            if len(valid) == 9:
                self.x = 3
                self.y = 6
            else:

                if self.wincheck(self.myid,self.board8):
                    self.x += 3
                    self.y += 6
                elif self.wincheck(self.oppid,self.board8):
                    self.x += 3
                    self.y += 6
                else:
                    if len(myspots)>0:
                        self.nextTo(myspots,self.board8)
                        self.x += 3
                        self.y += 6
                    else: 
                        self.x = random.randint(3,5)
                        self.y = random.randint(6,8)
                        
        elif self.VMB == '8':
            for i in self.board9:
                if i == "0":
                    valid.append(self.board9.index(i))
                elif i == str(self.myid):
                    myspots.append(self.board9.index(i))
            
            if len(valid) == 9:
                self.x = 6
                self.y = 6
            else:

                if self.wincheck(self.myid,self.board9):
                    self.x += 6
                    self.y += 6
                elif self.wincheck(self.oppid,self.board9):
                    self.x += 6
                    self.y += 6
                else:
                    if len(myspots)>0:
                        self.nextTo(myspots,self.board9)
                        self.x += 6
                        self.y += 6
                    else: 
                        self.x = random.randint(6,8)
                        self.y = random.randint(6,8)
        




    def wincheck(self,pid,testboard):
        win = False
        
        if testboard[0] == testboard[1] and testboard[0] == str(pid) and testboard[2] == "0":
            self.x = 2
            self.y = 0
            win = True
        elif testboard[0] == testboard[2] and testboard[0] == str(pid)and testboard[1] == "0":
            self.x = 1
            self.y = 0
            win = True
        elif testboard[1] == testboard[2] and testboard[1] == str(pid)and testboard[0] == "0":
            self.x = 0
            self.y = 0
            win = True
        elif testboard[0] == testboard[3] and testboard[0] == str(pid)and testboard[6] == "0":
            self.x = 0
            self.y = 2
            win = True
        elif testboard[0] == testboard[6] and testboard[0] == str(pid)and testboard[3] == "0":
            self.x = 0
            self.y = 1
            win = True
        elif testboard[3] == testboard[6] and testboard[3] == str(pid)and testboard[0] == "0":
            self.x = 0
            self.y = 0
            win = True
        elif testboard[0] == testboard[4] and testboard[0] == str(pid)and testboard[8] == "0":
            self.x = 2
            self.y = 2
            win = True
        elif testboard[0] == testboard[8] and testboard[0] == str(pid)and testboard[4] == "0":
            self.x = 1
            self.y = 1
            win = True
        elif testboard[4] == testboard[8] and testboard[4] == str(pid)and testboard[0] == "0":
            self.x = 0
            self.y = 0
            win = True
        elif testboard[1] == testboard[4] and testboard[1] == str(pid)and testboard[7] == "0":
            self.x = 1
            self.y = 2
            win = True
        elif testboard[1] == testboard[7] and testboard[1] == str(pid)and testboard[4] == "0":
            self.x = 1
            self.y = 1
            win = True
        elif testboard[4] == testboard[7] and testboard[4] == str(pid)and testboard[1] == "0":
            self.x = 1
            self.y = 0
            win = True
        elif testboard[2] == testboard[4] and testboard[2] == str(pid)and testboard[6] == "0":
            self.x = 0
            self.y = 2
            win = True
        elif testboard[2] == testboard[6] and testboard[2] == str(pid)and testboard[4] == "0":
            self.x = 1
            self.y = 1
            win = True
        elif testboard[4] == testboard[6] and testboard[4] == str(pid)and testboard[2] == "0":
            self.x = 2
            self.y = 0
            win = True
        elif testboard[2] == testboard[5] and testboard[2] == str(pid)and testboard[8] == "0":
            self.x = 2
            self.y = 2
            win = True
        elif testboard[2] == testboard[8] and testboard[2] == str(pid)and testboard[5] == "0":
            self.x = 2
            self.y = 1
            win = True
        elif testboard[5] == testboard[8] and testboard[5] == str(pid)and testboard[2] == "0":
            self.x = 2
            self.y = 0
            win = True
        elif testboard[3] == testboard[4] and testboard[3] == str(pid)and testboard[5] == "0":
            self.x = 2
            self.y = 1
            win = True
        elif testboard[3] == testboard[5] and testboard[3] == str(pid)and testboard[4] == "0":
            self.x = 1
            self.y = 1
            win = True
        elif testboard[4] == testboard[5] and testboard[4] == str(pid)and testboard[3] == "0":
            self.x = 0
            self.y = 1
            win = True
        elif testboard[6] == testboard[7] and testboard[6] == str(pid)and testboard[8] == "0":
            self.x = 2
            self.y = 2
            win = True
        elif testboard[6] == testboard[8] and testboard[6] == str(pid)and testboard[7] == "0":
            self.x = 1
            self.y = 2
            win = True
        elif testboard[7] == testboard[8] and testboard[7] == str(pid)and testboard[6] == "0":
            self.x = 0
            self.y = 2
            win = True

        return win
        

    def nextTo(self,myspots,board):

        for i in myspots:
            if str(i) == "0":
                if board[4] == "0":
                    self.x = 1
                    self.y = 1
                elif board[1] == "0":
                    self.x = 1
                    self.y = 0
                elif board[3] == "0":
                    self.x = 0
                    self.y = 1
            elif str(i) == "1":
                if board[4] == "0":
                    self.x = 1
                    self.y = 1
                elif board[0] == "0":
                    self.x = 0
                    self.y = 0
                elif board[2] == "0":
                    self.x = 2
                    self.y = 0
            elif str(i) == "2":
                if board[4] == "0":
                    self.x = 1
                    self.y = 1
                elif board[1] == "0":
                    self.x = 1
                    self.y = 0
                elif board[5] == "0":
                    self.x = 2
                    self.y = 1
            elif str(i) == "3":
                if board[4] == "0":
                    self.x = 1
                    self.y = 1
                elif board[0] == "0":
                    self.x = 0
                    self.y = 0
                elif board[6] == "0":
                    self.x = 0
                    self.y = 2
            elif str(i) == "5":
                if board[4] == "0":
                    self.x = 1
                    self.y = 1
                elif board[2] == "0":
                    self.x = 2
                    self.y = 0
                elif board[8] == "0":
                    self.x = 2
                    self.y = 2
            elif str(i) == "6":
                if board[4] == "0":
                    self.x = 1
                    self.y = 1
                elif board[3] == "0":
                    self.x = 0
                    self.y = 1
                elif board[7] == "0":
                    self.x = 1
                    self.y = 2
            elif str(i) == "7":
                if board[4] == "0":
                    self.x = 1
                    self.y = 1
                elif board[6] == "0":
                    self.x = 0
                    self.y = 2
                elif board[8] == "0":
                    self.x = 2
                    self.y = 2
            elif str(i) == "8":
                if board[4] == "0":
                    self.x = 1
                    self.y = 1
                elif board[7] == "0":
                    self.x = 1
                    self.y = 2
                elif board[5] == "0":
                    self.x = 2
                    self.y = 1
            elif str(i) == "4":
                if board[0] == "0":
                    self.x = 0
                    self.y = 0
                elif board[1] == "0":
                    self.x = 1
                    self.y = 0
                elif board[2] == "0":
                    self.x = 2
                    self.y = 0
                elif board[3] == "0":
                    self.x = 0
                    self.y = 1
                elif board[5] == "0":
                    self.x = 2
                    self.y = 1
                elif board[6] == "0":
                    self.x = 0
                    self.y = 2
                elif board[7] == "0":
                    self.x = 1
                    self.y = 2
                elif board[8] == "0":
                    self.x = 2
                    self.y = 2
            
    
    def getlegal(self,myid):
        
        legal = False
        
        while legal == False:
                
            self.getmove(myid)
            
            if self.table[self.x][self.y] == "0":
                legal = True
            else:
                legal = False
