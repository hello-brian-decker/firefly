import socket


def receiver_file_socket(ip, port):
    buffer_size = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1)
    print(f'Listening for connections on {ip}:{port}')
    
    while True:
        conn, addr = sock.accept()
        print(f'Connection from {addr[0]}:{addr[1]}')
    
        with conn:
            # Receive the file name
            file_name = conn.recv(buffer_size).decode('utf-8')
            print(f'Receiving file: {file_name}')
    
            # Open a file for writing
            with open(file_name, 'wb') as f:
                # Receive the file data in chunks
                while True:
                    data = conn.recv(buffer_size)
                    if not data:
                        break
                    f.write(data)
    
            print(f'File transfer complete: {file_name}')
