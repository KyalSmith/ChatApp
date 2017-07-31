import socket
import threading

sockets = []
threads = []
recv_buffer = 4096

def Chat_Server():
    global sockets


    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,1)
    server_socket.bind(('127.0.0.1',6003))
    server_socket.listen(255)

    while True:

        client_sock,addr = server_socket.accept()
        sockets.append(client_sock)

        if client_sock:
            client_sock.send("[+]Welcome to Kyal's chat server!".encode())
            client_thread = threading.Thread(target=Check_Messages,args=(client_sock,))
            threads.append(client_thread)
            client_thread.start()



def Check_Messages(client_sock):
    global recv_buffer
    while 1:
        msg = client_sock.recv(recv_buffer)
        Broadcast(client_sock,msg)


def Broadcast(client_sock,msg):
    global sockets
    for sock in sockets:
        if client_sock != sock:
            sock.send(msg)













if __name__=="__main__":
    Chat_Server()