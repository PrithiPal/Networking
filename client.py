import socket
import logging
import os


def main() : 
    
    if os.path.exists('client.log') : 
        os.remove('client.log')

    logger = logging.getLogger('ClientLogger')
    logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler('client.log')
    
    formatter = logging.Formatter('%(levelname)s -  %(asctime)s -  %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    logger.info('Client has started')
    
    s = socket.socket()
    local_hostname = socket.gethostname()
    server_address = (local_hostname,12345)
    
    s.connect(server_address)
    logger.info('Pinged the server')
    s.close()
    
    
if __name__ == '__main__' : 
    main()
    
    