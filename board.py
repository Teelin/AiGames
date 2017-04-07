import random


class board:

    def setMboard(self, mbstr):
        
        mbList = mbstr.split(",")
        validM = []
        for i in range(0,(len(mbList)-1)):
            if mbList[i] == "-1":
                validM.append(i)
        if len(validM) == 1:
            VMB = str(validM[0])
            check = "single"
        else:
            VMB = str(random.randint(0,8))
            check = "random"
            
        with open('mbfile.txt', 'a') as the_file:
            the_file.write(check + VMB+'\n')
        

    def setBoard():
        return

    def getMboard():
        return

    def getBoard():
        return
