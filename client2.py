from socket import socket, AF_INET, SOCK_STREAM
import time

# Configura o do servidor (ext-dn)
SERVER_IP = "192.168.70.130"  # IP do eth0 do oai-ext-dn
PORT = 1235  # Porta do servidor

# Criando o socket
mClientSocket = socket(AF_INET, SOCK_STREAM)

try:
    # Tentando conectar ao servidor
    print(f"Conectando ao servidor {SERVER_IP}:{PORT}...")
    mClientSocket.connect((SERVER_IP, PORT))
    print("Conexao estabelecida com sucesso!")

    # Enviando "Hello World" 15 vezes com intervalo de 5s
    for i in range(15):
        message = f"Hello World #{i+1} from UE 2"
        mClientSocket.send(message.encode())  # Envia a mensagem
        data = mClientSocket.recv(2048)  # Recebe resposta do servidor
        reply = data.decode()
        print(f'Resposta recebida: {reply}')
        time.sleep(5)  # Aguarda 5 segundos

except Exception as e:
    print(f"Erro ao conectar ao servidor: {e}")

finally:
    # Fecha o socket aps enviar todas as mensagens
    print("Fechando conexao...")
    mClientSocket.close()
