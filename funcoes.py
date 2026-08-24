import subprocess
import  platform

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