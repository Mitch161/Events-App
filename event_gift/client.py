#!/usr/bin/env python3
import socket
import struct
import base64
import json as js
import os
from key_exchange import DiffieHellman

class Client():
    def __init__(self):
        self.s = socket.socket()
        self.host = "mitchell-laptop"
        self.port = 8081

    def create_key(self):
        exchange = DiffieHellman(3)
        exchange.set_value()
        self.s.send(str(exchange.get_value()).encode('ascii'))
        received_key = self.s.recv(65536).decode()
        received_key = int(received_key)
        exchange.double_power(received_key)
        return exchange

    def download_data(self):
        #s = socket.socket()
        #host = "mitchell-laptop"
        #port = 8081
        self.s.connect((self.host, self.port))
        print("Connected...")
        print("Exchanging key...")
        exchange = self.create_key()


        data = ""
        data_dict = {}
        data = self.s.recv(200000)

        #--------------------------------
        exchange.hash_key()
        data = exchange.decrypt(data)
        print(data)
        #--------------------------------
        
        data_dict = js.loads(data)
        filepath = "giftevent/data"
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        for i in data_dict.keys():
            file = open("giftevent/data/"+i, "wb")
            file.write(base64.b64decode(data_dict[i]))
            file.close()

        print("Files has been received successfully")




#def main():
#    connection = Client()
#    connection.download_data()

#if __name__ == '__main__':
#    main()
