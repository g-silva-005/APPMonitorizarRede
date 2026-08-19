import subprocess
import  platform

#-------------------------------------------------------------------------#

def testa_ligacao(host):

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

ip_teste = "8.8.8.8"

print ("A testar ligacao... :)")

if (testa_ligacao(ip_teste)):
    print ("Sucesso! Tens acesso a internet :)")
else:
    print ("Infelizmente nao tens internet, verifica o teu wifi ou o teu router :(")




