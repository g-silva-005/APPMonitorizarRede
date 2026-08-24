from asyncio import sleep
import subprocess
import  platform
import funcoes

print ()

print("================== M E N U  de  R E D E ==================")
print("======== 1 - Testar Ligacao a Internet            ========")
print("======== 2 - Ver IP Local e Nome da Maquina       ========")
print("======== 3 - Descobrir o IP de um Site (DNS)      ========")
print("======== 4 - Fazer Ping a um IP Personalizado     ========")
print("======== 5 - Testar se uma Porta TCP esta Aberta  ========")
print("======== 0 - Sair do Programa                     ========")
print("==========================================================")

print ()

opcao = int(input("Escolhe uma opcao: "))

print ()

if (opcao == 1):
    print ("A testar ligacao... :)")

    if (funcoes.testa_ligacao()):
        print ("Sucesso! Tens acesso a internet :)")
    else:
        print ("Infelizmente nao tens internet, verifica o teu wifi ou o teu router :(")


if (opcao == 2):
    print ("A descobrir IP Local e Nome da Maquina...")
    sleep(3)
    funcoes.nomeIP_local()

    


