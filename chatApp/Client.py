
import socket
import threading

recv_buffer = 4096
output_lock = threading.Lock()

def Chat_Client():
    threads = []
    global recv_buffer,output_lock
    Client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        Client_socket.connect(('127.0.0.1',6003))
        msg = Client_socket.recv(recv_buffer)
        print(msg.decode())
    except Exception as e:
        print(e)
        pass

    Check_for_Messages_Thread = threading.Thread(target=Check_for_Messages,args=(Client_socket,))
    Check_for_Messages_Thread.daemon = True
    Check_for_Messages_Thread.start()

    while 1:


        output_msg = input("Message: ")

        if output_msg.lower() == "exit":
            print("Exiting...\n")
            Check_for_Messages_Thread.join()
            break

        Client_socket.send(output_msg.encode())


def Check_for_Messages(socket):

    global recv_buffer,output_lock
    while 1:
        msg = socket.recv(recv_buffer)
        if msg:
            output_lock.acquire()
            print("\n"+str(msg.decode())+"\n"+"Message: ")
            output_lock.release()













if __name__=="__main__":
    Chat_Client()