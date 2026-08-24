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

    print ("Maquina: ", maquina, "| IP: ", ip)

 #-------------------------------------------------------------------------#

def descobrirIPSite(site):
    try:
        ip = socket.gethostbyname(site)
        print ("O ip do Site ", site, "é: ", ip)
    except:
        print ("Nao consegui verificar o IP desse site :( \n Vê se o link do site está okay. ")

 #-------------------------------------------------------------------------#

def pingIN(ip):

    if platform.system() == "Windows":
            parametro = "-n"
    else:
        parametro = "-c"

    comando = ["ping", parametro, "1", ip]

    resposta = subprocess.call(comando)

    if resposta == 0:
        print ("ping a ",ip, "feito com sucesso!")
    else:
        print ("que pena, deu erro! Verifica se o ip esta correto")


      

