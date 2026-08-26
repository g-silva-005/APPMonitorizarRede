import time 
import subprocess
import  platform
import funcoes

print ()

print("================== M E N U  de  R E D E ==================")
print("======== 1 - Testar Ligacao a Internet            ========")
print("======== 2 - Ver IP Local e Nome da Maquina       ========")
print("======== 3 - Descobrir o IP de um Site (DNS)      ========")
print("======== 4 - Fazer Ping a um IP Personalizado     ========")
print("======== 5 - Calculadora de Sub-Rede IPv4         ========")
print("======== 0 - Sair do Programa                     ========")
print("==========================================================")

print ()

opcao = int(input("Escolhe uma opcao: "))

print ()

if (opcao == 1):
    print ("A testar ligacao... :)")
    time.sleep(3)
    if (funcoes.testa_ligacao()):
        print ("Sucesso! Tens acesso a internet :)")
    else:
        print ("Infelizmente nao tens internet, verifica o teu wifi ou o teu router :(")


elif (opcao == 2):
    print ("A descobrir IP Local e Nome da Maquina...")
    print ()
    time.sleep(3)
    funcoes.nomeIP_local()

elif (opcao == 3):
    print ("Introduz o link do site :)")
    site = input ("\n : ")
    print("A verificar o site...")
    time.sleep(3)
    print()
    funcoes.descobrirIPSite(site)

elif (opcao == 4):
    ip = input("Introduza o IP que quer fazer o ping: ")
    print("A enviar Pacotes...")
    time.sleep(3)
    print()
    funcoes.pingIN(ip)

elif (opcao == 5):
    rede = input("Introduza o ip que deseja fazer o calculo (com o cidr): ")
    print ()
    print ("A calcular... ")
    time.sleep(3)
    print ()
    res=funcoes.calculadora(rede)

    if res:
        print("=========================================================")
        print("============          R E S U L T A D O      ============")
        print(f"========== Rede: {res[rede]}               ===========" )
        print(f"========== Broadcast: {res['broadcast']}     ===========" )
        print(f"========== Mascara: {res['netmask']}         ===========" )
        print(f"========== Hosts Disponiveis: {res['hosts_uteis']} ===========" )
        print("=========================================================")

    else:
        print("Inseriu um IP invalido ou sem o CIDR :( (ex: 10.0.0.0/24)")







