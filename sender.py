import socket


def sender_file_socket(ip, port):
    buffer_size = 4096
    file_path = 'path/to/file'
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        print(f'Connected to {ip}:{port}')
    
        # Send the file name to the server
        file_name = file_path.split('/')[-1]
        sock.sendall(file_name.encode('utf-8'))
    
        # Send the file data in chunks
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(buffer_size)
                if not data:
                    break
                sock.sendall(data)
    
        print(f'File transfer complete: {file_name}')
