import time
import socket
import random
import threading
import string

#Variavel que guarda os caracteres usados para gerar os nicks
rand = string.ascii_lowercase+string.ascii_uppercase

#Função responsavel por gerar o nick dos bots
def GenNick():
    for x in range(8):
        nick = nick+random.choice(rand)
    return nick

#Função Responsavel por mandar um pacote com as informações nescesarias para aceitar o login
def GenConn(Ip,Port):
    #Define o protocolo e conecta o socket com o servidor
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((Ip,Port))
    #Pacote que sera enviado para o servidor
    byte = b"\x12\x00/\x0c192.168.86.3"+(Port).to_bytes(2,'big')+b"\x02\n\x00\x08"+GenNick().encode("utf-8")
    s.send(byte)
    #Mantem o socket ativo
    while True:
        s.recv(1024)

Ip = input("Digite o Ip: ")
Port = int(input("Digite a Porta: "))

#Gera a quantia de threads escolhida ficando cada um responsavel por uma conta
for x in range(int(input("Quantas contas: "))):
    Thread = threading.Thread(target=GenConn,args=(Ip,Port,))
    Thread.start()
