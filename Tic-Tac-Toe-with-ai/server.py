import socket
import threading
import os

# initializing variable
player = 'o'
computer = 'x'
 
global XO
XO = 'o'

# setting up a 3 * 3 board in canvas
board = [['_','_','_'],['_','_','_'],['_','_','_']]

def eval():
	b = board
	for i in range(3):
		if(b[i][0]==b[i][1] and b[i][1]==b[i][2]):
			if(b[i][0]==player):
				return 10
			elif (b[i][0]==computer):
				return -10
	for i in range(3):
		if (b[0][i]==b[1][i] and b[1][i]==b[2][i]):
			if(b[0][i]==player):
				return 10
			elif (b[0][i]==computer):
				return -10
		if (b[0][0]==b[1][1] and b[1][1]==b[2][2]):
			if (b[0][0]==player):
				return 10
			elif (b[0][0]==computer):
				return -10
		if (b[0][2]==b[1][1] and b[1][1]==b[2][0]):
			if(b[0][2]==player):
				return 10
			elif(b[0][2]==computer):
				return -10
	if(not movesleft()):
		return 0
	return -1
	
def mark_x(x,y):
	board[x][y] = computer

def mark_o(x,y):
	board[x][y]= player
	
def miniMax(Max,depth,alpha,beta):
	score=eval()
	if(score!=-1):
		return score
	if(Max):
		best=-1000000
		for i in range(3):
			for j in range(3):
				if (board[i][j]=='_'):
					board[i][j]=player
					val=self.miniMax(not Max,depth+1,alpha,beta)
					board[i][j]='_'
					best=max(best,val)
					alpha=max(best,alpha)
					if beta<=alpha:
						return alpha-depth
		return alpha-depth
	else:
		best=1000000
		for i in range(3):
			for j in range(3):
				if (board[i][j]=='_'):
					board[i][j]='x'
					val=self.miniMax(not Max,depth+1,alpha,beta)
					board[i][j]='_'
					best=min(best,val)
					beta=min(best,beta)
					if beta<=alpha:
						return beta+depth
		return beta+depth

def findnext():
	bestnow=1000000
	bestmove=[-1,-1]
	for i in range(3):
		for j in range(3):
			if(board[i][j]=='_'):
				board[i][j]='x'
				moveval=miniMax(True,1,-1000000,1000000)
				board[i][j]='_'
				if(moveval<bestnow):
					bestnow=moveval
					bestmove=[i,j]
	return bestmove
		
def move_ai():
	coordx,coordy=findnext()
	mark_o(coordx,coordy)
	coordx, coordy = coordx*(400//3), coordy*(400//3)
	send_data = '{}-{}'.format(coordx,coordy).encode()
	return send_data()

# Defining A count Var
count = 0

conn_established = False

# create a separate thread to send and receive data from the client Since It is a blocking parameter
def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()

# Defining A connection Object
s = socket.socket()

#binding Host And Port
s.bind(('', 9999))

# Listening For Connection
s.listen(1)

# Accepting The Connection
conn, addr = s.accept()  # wait for a connection, it is a blocking method
conn_established = True

print('You Are Connected To ---- IP : ' + str(addr[0]) + ' port : ' + str(addr[1]))


# Function For Recieving data
def receive_data():
    global conn
    while True:
        if XO == 'o':
            # get coordinates of mouse click
            data = conn.recv(1024).decode()
            if(data == 'quit'):
                conn = None
                exit()
            data = data.split('-')
            x, y = int(data[0])//(400//3), int(data[1])//(400//3)
            mark_o(x, y)
            XO = 'x'
        else:
            conn.send(move_ai())
            XO = 'o'  


# run the blocking functions in a separate thread
create_thread(receive_data)
