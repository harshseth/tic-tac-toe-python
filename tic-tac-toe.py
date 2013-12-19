#Harsh Seth 
#username hsseth
#Base code from http://forum.codecall.net/topic/50892-tic-tac-toe-in-python/
#Converted it into a One-Player Tic-Tac-Toe game.
def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""

		
def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print turn, "won!!!"
            return True
        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        print turn, "won!!!"
        return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Draw"
        return True
        

    return False

"""This function checks the computer copy of the MAP viz called the CMAP, for letting the computer know if player is winning in the next move"""
def cmap_check_done(): 
	global cmap
	for i in range(0,3):
		if cmap[i][0] == cmap[i][1] == cmap[i][2] == pturn!= " " \
		or cmap[0][i] == cmap[1][i] == cmap[2][i] == pturn != " ":
			return True
        
	if cmap[0][0] == cmap[1][1] == cmap[2][2] == pturn != " " \
	or cmap[0][2] == cmap[1][1] == cmap[2][0] == pturn != " ":
		return True

	if " " not in cmap[0] and " " not in cmap[1] and " " not in cmap[2]:
		print "Draw"
		return True
        
	return False
#This function helps the computer to decide the winning move in the next step 
def wcmap_check_done():
	global cmap
	for i in range(0,3):
		if cmap[i][0] == cmap[i][1] == cmap[i][2] == computer!= " " \
		or cmap[0][i] == cmap[1][i] == cmap[2][i] == computer != " ":
			return True
        
	if cmap[0][0] == cmap[1][1] == cmap[2][2] == computer != " " \
	or cmap[0][2] == cmap[1][1] == cmap[2][0] == computer != " ":
		return True

	if " " not in cmap[0] and " " not in cmap[1] and " " not in cmap[2]:
		print "Draw"
		return True
        
	return False
	
#counts how many unoccupied corners are remaining 	
def count_corner():
	counter = 0
	corner = [1,3,7,9]
	for i in range(0,3):
		cpos= corner[i]
		if cpos <=9 and cpos >=1:
			Y = cpos/3
			X = cpos%3
			if X != 0:
				X -=1
			else:
				X = 2
				Y -=1
        if map[Y][X] == " ":
			counter= counter+1
			
	return counter
#if computer is the X, so it will select a random corner for the first move	
def random_corner():
	global map
	corner = [1,3,7,9]
	a= random.randint(0,3)
	cpos= corner[a]
	if cpos <=9 and cpos >=1:
		Y = cpos/3
		X = cpos%3
		if X != 0:
			X -=1
		else:
			X = 2
			Y -=1
	if map[Y][X] == " ":
		map[Y][X] = computer

#Helps the computer to decide on which empty corner should be occupied next		
def place_corner():
	global map
	m=0
	corner = [1,3,7,9]
	for i in range(0,3):
		if m!= 1:
			cpos= corner[i]
			if cpos <=9 and cpos >=1:
				Y = cpos/3
				X = cpos%3
				if X != 0:
					X -=1
				else:
					X = 2
					Y -=1
			if map[Y][X] == " ":
				map[Y][X]=computer
				m=1
#we call this function to check what next move of the computer will make it win			
def c_win_move():
	m=0
	for i in range(0,3):
		for j in range(0,3):
			if m != 1:
				if cmap[2-i][j] == " ":
					cmap[2-i][j] = computer
					cdone= wcmap_check_done()
					cmap[2-i][j] = " "
					if cdone == True:
						map[2-i][j]=computer
						m=1
						cdone= False
						break 
					cdone= False	
	return m				
		

#the main function where all the moves of the computer are defined
def computer_moves():
	count=0
	m=0
	ccount=0
	corner = [1,3,7,9]
	global map
	global cmap
	cdone = False
	#First make a copy of the current Map for the use of computer
	for i in range(0,3):
		for j in range(0,3):
			cmap[2-i][j]= map[2-i][j]
			if map[2-i][j] == " ":
				count = count +1
	#this varibale lets the computer know if it has made a move or no		
	m=0
	
	#for the first move viz. when computer is X
	if count == 9:
		random_corner()
		m=1
		
	
	
	#Blocking the player from winning
	for i in range(0,3):
		for j in range(0,3):
			if m != 1:
				if cmap[2-i][j] == " ":
					cmap[2-i][j] = pturn
					cdone= cmap_check_done()
					m=c_win_move()
					cmap[2-i][j] = " "
					if cdone == True and m!=1:
						map[2-i][j]=computer
						m=1
						cdone= False
						break 
					cdone= False	
						
	if m!=1:
		m = c_win_move()
		ccount = count_corner() 
		if ccount >= 0 and m !=1:
			place_corner()
			m=1
	#checks if the centre is unoccupied
	if m!=1:	
		if map[1][1] == " ":
			map[1][1]= computer
			m=1
			
					
	
		
		
	
computer =""
correct_input = False

while correct_input != True:
	pturn = raw_input( "Please select X or O \n").upper()
	if pturn == "X":
		computer = "O"
		correct_input = True
	elif pturn == "O":
		computer = "X"
		correct_input = True
	else:
		print "Wrong input please try again"
		correct_input = False	
		


		

import random		
turn ="X"
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False
#cmap is the computers copy of the main map, which the computer uses to estimate its moves
cmap = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]

while done != True:
	print "Current status of the board"
	print_board()
	print
	print turn, "'s turn"
	print

	moved = False
	
	if computer == turn:
		computer_moves()
		moved =True	
		done = check_done()
		if done == False:
			if turn == "X":
				turn = "O"
			else:
				turn = "X"
                
		
	
	while moved != True:
		print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
		print "7|8|9"
		print "4|5|6"
		print "1|2|3"
		print

		try:
			pos = input("Select: ")
			if pos <=9 and pos >=1:
				Y = pos/3
				X = pos%3
				if X != 0:
					X -=1
				else:
					X = 2
					Y -=1
                    
				if map[Y][X] == " ":
					map[Y][X] = turn
					moved = True
					done = check_done()

					if done == False:
						if turn == "X":
							turn = "O"
						else:
							turn = "X"
                
            
		except:
			print "You need to add a numeric value"