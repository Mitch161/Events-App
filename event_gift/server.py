import socket
import os
import json as js
import base64
from key_exchange import DiffieHellman

def create_key(conn):
    exchange = DiffieHellman(4)
    exchange.set_value()
    key = exchange.get_value()
    key = str(key)
    conn.send(key.encode('ascii'))
    received_key = conn.recv(65536).decode()
    received_key = int(received_key)
    exchange.double_power(received_key)
    return exchange

def retrieve_files():
    files_list = []
    files = os.listdir('/home/mitchell/fileServer')
    for file in files:
        files_list.append(file)
    return files_list

def main():
    json_dict = {}
    s = socket.socket()
    host = "0.0.0.0"
    port = 8081
    s.bind((host, port))

    s.listen(7)
    print(host)
    print("Waiting for any incoming connections...")
    
    conn, addr = s.accept()
    print(addr, "Has connected to the server")
    exchange = create_key(conn)
    files_list = retrieve_files()

    for filename in files_list:
        file = open('/home/mitchell/fileServer/'+filename, 'rb')
        data = base64.b64encode(file.read())
        data = data.decode()
        json_dict[filename] = data # cloud be this


    json_string = js.dumps(json_dict)
    exchange.hash_key()
    print(json_string)
    json_string = exchange.encrypt(json_string)
    #json_string = exchange.decrypt(json_string)
    #print(json_string)
    #json_string = json_string.encode("ascii")
    conn.send(json_string)
    s.close()
    print("data has been transmitted successfully")

if __name__ == '__main__':
    main()