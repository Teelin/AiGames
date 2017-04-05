import sys



while True:
    line = sys.stdin.read()
    
    parts = line.split(" ")
    with open("settings.txt","a+") as file:
        file.write(parts + "/n")

    if parts[0] == "settings":
        #store settings
        if parts[1] == "timebank":
            print("test")
            timebank = int(parts[2])
        elif parts[1] == "time_per_move":
            print("test")
            time_per_move = int(parts[2])
        elif parts[1] == "player_names":
            print("test")
            player_names = parts[2]
        elif parts[1] == "your_bot":
            print("test")
            mybot = parts[2]
        elif parts[1] == "your_botid":
            print("test")
            mybotid = int(parts[2])
            
        
        
        
    elif parts[0] == "update":
        #store settings
        print("test")
        
    elif parts[0] == "action":
        sys.stdout.write("place_move 6 6")
        sys.stdout.flush() 
        with open("settings.txt","a+") as file:
            file.write(str(timebank) + str(time_per_move) + player_names + mybot + str(mybotid))
        

    
