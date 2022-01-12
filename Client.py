import socket, os
#import subprocess, sys
import threading
import NotifyChanges as nc


class Client:
    def __init__(self,ip,port):
        self.socket = socket.socket()
        self.socket.connect((ip,port))
        self.files=[]
        self.thread = threading.Thread(target=nc.main, args=(self.files,)).start()##
        print("Initialized, connected to server. Starts monitoring.")

    def handle_file(self):
        '''sends downloaded files to the server and gets scan results.'''
        while True:
            if(len(self.file)>0):
                filename = self.files.pop(0)
                break
                
        self.socket.send(filename.encode())
        with open(filename,'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    self.socket.send(data)
                    break
                self.socket.send(data)

        report = self.socket.recv(1024).decode()#it is stuck here
        with open("answer.txt",'w') as f:
            f.write(filename + "--->" + report + "\r\n")


def main():
    client = Client('127.0.0.1',12345)
    while True:
        client.handle_file()
    client.socket.close()

main()
