import socket
import logging
import os 

def main() : 

	if os.path.exists('server.log') : 
		os.remove('server.log')
	
	logger = logging.getLogger('ServerLogger')
	logger.setLevel(logging.INFO)
	
	handler = logging.FileHandler('server.log')
	handler.setLevel(logging.INFO)

	formatter = logging.Formatter('%(levelname)s -  %(asctime)s -  %(message)s')
	handler.setFormatter(formatter)

	logger.addHandler(handler)
	logger.info('Server has started')
	s = socket.socket()
	local_hostname = socket.gethostname()
	address = (local_hostname,12345)
	s.bind(address)

	s.listen(4)
	
	logger.info('Waiting for incoming connections')
	while True : 
		client,client_addr = s.accept()
		logger.info('Client from {} pinging'.format(str(client_addr)))

	logger.info('Server Exiting')
	s.close()

if __name__ == '__main__' : 
	main()
