# This is a TCP Client made to receive documents accross from a Server
# v4 -- Works. available files list is now sent by server

# modules
import socket
import sys

# variables
port= 8888
all = False
some = [] # TO DO
IP = input('Ingrese la dirección IP del servidor o deje en blanco para conectarse a una red local.\n\n>>>>')
IP = IP if IP != '' else socket.gethostbyname(socket.gethostname())

# Initial connection to get files
print(f'\nConectandose con {IP}...')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((IP, port))
    except socket.gaierror:
        print('\nNo se pudo establecer la conneción con la dirección IP...\nSaliendo del Programa...\n')
        sys.exit()

    # Saludo inicial
    print('\n\nIniciando...')
    s.send('archivos'.encode())
    msg = s.recv(1024).decode()

# Solicitar al usuario el nombre del archivo
names = msg.split(',')
keys = list(range(len(names)))
files = {keys[i]: names[i] for i in range(len(keys))}
nl = "\n"
while True:
    fname = input(f'''
        Seleccione el archivo que desea descargar:

{nl.join(f"{key}) {value}" for key, value in files.items())}
t) TODOS
s) SALIR

        Ingrese el numero del archivo correspondiente que desea descargar,
        La letra "t" para descargar TODOS los archivos encontrados
        O la letra "s" para salir del programa.

        >>>> ''')
    if fname == 's':
        sys.exit()
    elif fname == 't':
        all = True
        break
    try:
        fname = int(fname)
    except ValueError:
        print('\nIngreso Incorrecto...\n')
        continue
    if fname in range(len(files)):
        fname = files[fname]
        break
    else:
        print('\nIngreso Incorrecto...\n')

# Define a function that handles the connection
def connector(fn):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, port))
        print('Conectado con el Servidor')

        # Enviar nombre del archivo
        fh = open(f'./receive/{fn}', 'wb')
        s.send(fn.encode())
        msg = s.recv(1024).decode()
        print(f'[SERVIDOR] : {msg}')
        print('Comenzando la Descarga...')

        # Recibir datos del archivo
        data = s.recv(1024)
        while (data):
            fh.write(data)
            data = s.recv(1024)
        print('¡Datos Descargados!')

# Connect with server
if (all):
    for file in files:
        connector(files[file])
else:
    connector(fname)

"""# v3 -- works. Client can now download more than one file

# modules
import socket
import sys

# variables
host = '127.0.0.1'
port= 8888
files = {
    'a': 'Provedores Todos.xlsm',
    'b': 'PDVDATA.FDB'
}
multiple = False

# Get file name
while True:
    fname = input('''
    Seleccione el archivo que desea descargar:

        a) Provedores Todos.xlsm
        b) PDVDATA.FDB
        c) Ambos

    Ingrese la letra del archivo correspondiente que desea descargar
    O la letra "s" para salir del programa

    >>>> ''')

    if fname == 'a':
        fname = files['a']
        break
    elif fname == 'b':
        fname = files['b']
        break
    elif fname == 'c':
        multiple = True
        break
    elif fname == 's':
        print('Saliendo del programa...')
        sys.exit()
    else:
        print('\n************** Ingreso incorrecto ************\n')

# Define a function that handles the connection
def connector(fn):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print('Conectado con el servidor')

        # Enviar nombre del archivo
        fh = open(f'./receive/{fn}', 'wb')
        s.send(fn.encode())
        msg = s.recv(1024).decode()
        print(f'Mensaje del servidor: {msg}')

        # Recibir datos del archivo
        data = s.recv(1024)
        while (data):
            fh.write(data)
            data = s.recv(1024)
        print('Datos descargados')

# Connect with server
if (multiple):
    for file in files:
        connector(files[file])
else:
    connector(fname)
"""
# *************************************************************************************




"""# v2 -- works. Client can choose between 2 *predefined* files
# IDEA: For multiple files make the connection call in a loop (mmmm a connection call from within a call?? <---- Not possible???)
# FOLLOWUP IDEA: make an initial connection to know the files then close and manage the loop of connection 

# modules
import socket
import sys

# variables
host = '127.0.0.1'
port= 8888
files = {
    'a': 'Provedores Todos.xlsm',
    'b': 'PDVDATA.FDB'
}

# Get file name
while True:
    fname = input('''
    Seleccione el archivo que desea descargar:

        a) Provedores Todos.xlsm
        b) PDVDATA.FDB

    Ingrese la letra del archivo correspondiente que desea descargar
    O la letra "s" para salir del programa

    >>>> ''')

    if fname == 'a':
        fname = files['a']
        break
    elif fname == 'b':
        fname = files['b']
        break
    elif fname == 's':
        print('Saliendo del programa...')
        sys.exit()
    else:
        print('\n************** Ingreso incorrecto ************\n')

# Connect with server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print('Conectado con el servidor')

    # Enviar nombre del archivo
    fh = open(f'./receive/{fname}', 'wb')
    s.send(fname.encode())
    msg = s.recv(1024).decode()
    print(f'Mensaje del servidor: {msg}')

    # Recibir datos del archivo
    data = s.recv(1024)
    while (data):
        fh.write(data)
        data = s.recv(1024)
    print('Datos descargados')
"""


""" v1 -- works but only handles 1 file
import socket

host = '127.0.0.1'
port= 8888
fh = open('./receive/Provedores Todos.xlsm', 'wb')

# 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print('Conectado con el servidor')
    data = s.recv(1024)
    print('Descargando...')
    while (data):
        fh.write(data)
        data = s.recv(1024)
    print('¡Descarga completada!')
"""