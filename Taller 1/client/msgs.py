import pickle

def msg_service(socket):
	while True:
		try:
			data = socket.recv(1024)
			if data:
			    print('\r'+pickle.loads(data)['name']+': '+pickle.loads(data)['msg']+'\nYou: ', end='')
		except:
			pass

def send_msg(s, msg):
	s.send(pickle.dumps(msg))