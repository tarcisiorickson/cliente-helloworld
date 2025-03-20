from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def HandleRequest(mClientSocket, mClientAddr):
    while True:
        # Este loop foi criado para que o servidor conseguisse receber diversas requisi    es de
        # um mesmo cliente, usando a mesma conex  o, ou seja, sem que fosse necess  ria a
        # cria    o de uma nova conex  o.
        print('Esperando o pr  ximo pacote ...')
        # Recebendo os dados do Cliente:
        # o Servidor ir   receber bytes do cliente, sendo necess  ria a convers  o de bytes
        # para string ou para o tipo desejado.
        data = mClientSocket.recv(2048)
        print(f'Requisi    o recebida de {mClientAddr}')
        req = data.decode()
        print(f'A requisi    o foi:{req}')
        # Ap  s receber e processar a requisi    o o servidor est   apto para enviar uma resposta.
        rep = 'Hey cliente!'
        mClientSocket.send(rep.encode())

#Passo 1: Cria    o do socket
mSocketServer = socket(AF_INET, SOCK_STREAM)
print(f'Socket criado ...')
#Passo 2: Transformando o socket em um socket servidor.
#Dar Bind significa vincular um socket a um endere  o
mSocketServer.bind(('192.168.70.130',1235))

#Colocar o servidor para escutar as solicita    es de conex  o
mSocketServer.listen()
while True:
    # Este loop foi colocado para que o servidor conseguisse se conectar com v  rios cliente;
    # Passo 3: Colocar o servidor para aceitar as solicita    es de conex  o:
    clientSocket, clientAddr =  mSocketServer.accept()
    print(f'O servidor aceitou a conex  o do Cliente: {clientAddr}')
    # Passo 4: Cria    o de m  ltiplas threads para que o servidor consiga responder mais de
    # um cliente por vez.
    Thread(target=HandleRequest, args=(clientSocket, clientAddr)).start()
