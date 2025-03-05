import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="172.20.10.5"
port=1234
complete=(ip_add,port) 
message=input("kya msg karoge")
encode_mgs=message.encode('ascii')
s.sendto(encode_mgs,complete)