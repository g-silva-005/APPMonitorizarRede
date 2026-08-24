import subprocess
import  platform
import socket
#-------------------------------------------------------------------------#

def testa_ligacao(host="8.8.8.8"):

    # verificar o sistema operativo do user
    if platform.system() == "Windows":
        parametro = "-n"
    else:
        parametro = "-c"

    comando = ["ping", parametro, "1", host]

    resposta = subprocess.call(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if resposta == 0:
        return True
    else:
        return False

 #-------------------------------------------------------------------------#

def nomeIP_local():
    maquina = socket.gethostname()
    ip = socket.gethostbyname(maquina)

    printf("Maquina: ", maquina "| "IP: ", ip)

