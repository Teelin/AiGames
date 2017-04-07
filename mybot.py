import sys, fileinput
from board import board


with open('somefile.txt', 'a') as the_file:
    the_file.seek(0)
    the_file.truncate()
with open("settings.txt","a+") as file:
    file.seek(0)
    file.truncate()


while True:

    currentboard = board()

    for line in fileinput.input():
        with open('somefile.txt', 'a') as the_file:
            the_file.write( line+'\n')

        parts = line.split(" ")

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
                #oppid = 1 if myid = 2 else 1


        elif parts[0] == "update":
            if parts[2] == "macroboard":
                mbstr = parts[3]
                currentboard.setMboard(mbstr)
            elif parts[2] == "field":
                bstr = parts[3]
                currentboard.setBoard(bstr)
            

        elif parts[0] == "action":
            sys.stdout.write('place_move 0 1\n')
            sys.stdout.flush()
            with open("settings.txt","a+") as file:
                file.write(str(timebank) +"\n"+ str(time_per_move) +"\n"+ player_names + mybot + str(myid)+"\n\n\n")

