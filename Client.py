import socket, subprocess

class Client:
    def __init__(self,ip,port):
        self.socket = socket.socket()
        self.socket.connect((ip,port))
        print("Initialized and connected.")

    def handle_file(self):
        '''sends downloaded files to the server and gets scan results.'''
        code = subprocess.run(['python','NotifyChanges.py'],shell=True)
        filename = subprocess.check_output(['python','NotifyChanges.py'],shell=True)
        self.socket.send(filename)
        with open(filename.decode(),'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    self.socket.send(data)
                    break
                self.socket.send(data)

        report = self.socket.recv(1024).decode()
        print(report) #to do later - save results to a file


def main():
    client = Client('127.0.0.1',12345)
    while True:
        client.handle_file()
    client.socket.close()

main()
