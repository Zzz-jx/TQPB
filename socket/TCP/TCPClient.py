from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence: ')
while sentence != 'close':
    # 开始发送和接受报文
    clientSocket.send(sentence.encode())
    modifedSentence = clientSocket.recv(2048)
    print('From Server: ', modifedSentence.decode())
    sentence = input('continue input or input close: ')
# 关闭连接
clientSocket.close()
