import socket
import vtScanning as vt

class Server:
    def __init__(self,ip,port):
        self.socket = socket.socket()
        self.socket.bind((ip,port))
        self.socket.listen(1)
        self.client_soc, addr = self.socket.accept()
        print("Server initialized, founded connection.")

    def get_file(self):
        '''gets file from client, saves it and returns its name.'''
        filename = self.client_soc.recv(1024).decode()
        with open(filename,'wb') as f:
            while True:
                data = self.client_soc.recv(1024)
                if not data:
                    break
                f.write(data)

        return filename

    def send_file(self, apikey, filename):
        '''sends file to virusTotal scan and gets result.'''
        vt.set_apikey(apikey)
        vt.scan_file(filename)
        report = vt.get_report(file_name)
        print(report)
        self.client_soc.send(report.encode())

        
def main():
    apikey = 'd833c4df1b028d805148e488937c7159f05e192d7f192dc6f239511e0c14d1ea'
    server = Server('127.0.0.1',12345)
    while True:
        filename = server.get_file()
        server.send_file(apikey, filename)
    server.client_soc.close()
    server.socket.close()

main()
