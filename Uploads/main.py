import sys
from board1 import board
currentboard = board()

def __main__():
    while True:

        
        line = sys.stdin.readline().rstrip('\r\n')
        parts = line.split(" ")
        '''with open('test.txt', 'a') as the_file:
            the_file.write(str(line) +"\n\n")'''

        if parts[0] == "settings":
            #store settings
            if parts[1] == "timebank":
                timebank = int(parts[2])
                
            elif parts[1] == "time_per_move":
                time_per_move = int(parts[2])
                
            elif parts[1] == "player_names":
                player_names = parts[2]
                
            elif parts[1] == "your_bot":
                mybot = parts[2]
                
            elif parts[1] == "your_botid":
                myid = int(parts[2])
                


        elif parts[0] == "update":
            if parts[2] == "macroboard":
                mbstr = parts[3]
                currentboard.setMboard(mbstr)
            elif parts[2] == "field":
                bstr = parts[3]
                currentboard.setBoard(bstr)
            

        elif parts[0] == "action":
 
            currentboard.getlegal(myid)
            x = currentboard.x
            y = currentboard.y
            
            sys.stdout.write('place_move '+str(x)+' '+str(y)+'\n')
            sys.stdout.flush()
           



__main__()

