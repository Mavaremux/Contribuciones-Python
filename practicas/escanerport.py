import socket

ip = input("Ingrese la ip a escanear")

for puerto in range (0, 65535):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    rs = sock.connect_ex((ip , puerto))

    if rs == 0:
    
        print(f"[+] Puerto {puerto}: ABIERTO y escuchando peticiones")
    
        sock.close()
    else: 
        print("El puerto esta cerrado o filtrado")
