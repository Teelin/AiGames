import sys, fileinput
import io


#while True:

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
            mybotid = int(parts[2])


    elif parts[0] == "update":
        #store settings
        print("test")

    elif parts[0] == "action":
        #print("place_move 0 0")        

        
        io.IOBase.write("place_move 0 0")
        io.flush()
        
        with open("settings.txt","a+") as file:
            file.write(str(timebank) + str(time_per_move) + player_names + mybot + str(mybotid))

