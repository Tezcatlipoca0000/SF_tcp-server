# This is a TCP Server made to send documents accross to a Client
# v4 -- Creates a recent copy of the important files before sending

# Modules
import socket
import os
import shutil

# Variables
host = '127.0.0.1'
port = 8888
dir = './send/'
src1 = r'C:/Program Files (x86)/AbarrotesPDV/db/PDVDATA.FDB'
src2 = r'C:/Users/casa/Desktop/Provedores Todos.xlsm'
files = []

# Get files to send
print('Haciendo una copia actualizada...')
try:
    shutil.copy(src1, dir)
    shutil.copy(src2, dir)
    print('Completado.')
except:
    print('No se encontraron los archivos.')
for file in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, file)):
        files.append(file)
        

# Connection
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print('Esperando una conección...')
        conn, addr = s.accept()
        with conn:
            print(f'Cliente conectado: {addr}')
            
            # Enviar lista de archivos disponibles
            saludo = conn.recv(1024).decode()
            if saludo == 'archivos':
                print('Enviando lista de archivos disponibles')
                conn.send(','.join(files).encode())

            # Enviar archivo(s) seleccionados por el usuario
            else:
                fname = saludo
                # Copiar archivos antes de enviarlos
                if fname == 'PDVDATA.FDB':
                    try:
                        print('Copiando archivo...')
                        shutil.copy(src1, dir)
                        print('¡Copiado!')
                    except:
                        print('Archivo no copiado')
                if fname == 'Provedores Todos.xlsm':
                    try:
                        print('Copiando archivo...')
                        shutil.copy(src2, dir)
                        print('¡Copiado!')
                    except:
                        print('Archivo no copiado')

                print('El nombre del archivo: --> ', fname)
                conn.send(f'Nombre recibido: {fname}'.encode())

                # Enviar datos del archivo
                print('Leyendo el archivo...')
                with open(f'./send/{fname}', 'rb') as fh:
                    while True:
                        data = fh.read(1024)
                        if not data:
                            break
                        conn.sendall(data)
                print('Datos enviados')


"""# v3 -- Works. available files list is now sent by server

# Modules
import socket
import os

# Variables
host = '127.0.0.1'
port = 8888
dir = './send/'
files = []

# Get files to send
for file in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, file)):
        files.append(file)
        

# Connection
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Cliente conectado: {addr}')

            # Enviar lista de archivos disponibles
            saludo = conn.recv(1024).decode()
            if saludo == 'archivos':
                print('Enviando lista de archivos disponibles')
                conn.send(','.join(files).encode())
            # Enviar archivo(s) seleccionados por el usuario
            else:
                # Obtener el nombre de archivo
                fname = saludo
                print('the file name --> ', fname)
                conn.send(f'Nombre recibido: {fname}'.encode())

                # Enviar datos del archivo
                with open(f'./send/{fname}', 'rb') as fh:
                    while True:
                        data = fh.read(1024)
                        if not data:
                            break
                        conn.sendall(data)
                print('Datos enviados')
"""

"""# v2 -- works. Client can choose between 2 *predefined* files
# TO DO: server must copy original file and paste it in the "send" folder before sending the copy
# TO DO: server must send list of file names available from wich the client will choose

# Modules
import socket

# Variables
host = '127.0.0.1'
port = 8888

# Connection
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Cliente conectado: {addr}')

            # Obtener el nombre de archivo
            fname = conn.recv(1024).decode()
            print('the file name --> ', fname)
            conn.send(f'Nombre recibido: {fname}'.encode())

            # Enviar datos del archivo
            with open(f'./send/{fname}', 'rb') as fh:
                while True:
                    data = fh.read(1024)
                    if not data:
                        break
                    conn.sendall(data)
            print('Datos enviados')
   """             



""" v1 -- works but only handles 1 file
import socket

host = '127.0.0.1'
port = 8888
fh = open('./send/Provedores Todos.xlsm', 'rb')
    

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Conectado con {addr}')
            with open('./send/Provedores Todos.xlsm', 'rb')as fh:
                print('Enviando datos...')
                while True:
                    data = fh.read(1024)
                    if not data:
                        break
                    conn.sendall(data)
            print('¡Datos enviados!')
"""