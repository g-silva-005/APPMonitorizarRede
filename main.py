import time 
import subprocess
import  platform
import funcoes
import os

while True:

        print ()

        print("================== M E N U  de  R E D E ==================")
        print("======== 1 - Testar Ligacao a Internet            ========")
        print("======== 2 - Ver IP Local e Nome da Maquina       ========")
        print("======== 3 - Descobrir o IP de um Site (DNS)      ========")
        print("======== 4 - Fazer Ping a um IP Personalizado     ========")
        print("======== 5 - Calculadora de Sub-Rede IPv4         ========")
        print("======== 6 - Menu de Administrador de Sistemas    ========")
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
            print ()
            input("Pressione qualquer tecla para proseguir...")
            os.system("cls")

        elif (opcao == 2):
            print ("A descobrir IP Local e Nome da Maquina...")
            print ()
            time.sleep(3)
            funcoes.nomeIP_local()
            print ()
            input("Pressione qualquer tecla para proseguir...")
            os.system("cls")
            
        elif (opcao == 3):
            print ("Introduz o link do site :)")
            site = input ("\n : ")
            print("A verificar o site...")
            time.sleep(3)
            print()
            funcoes.descobrirIPSite(site)
            print ()
            input("Pressione qualquer tecla para proseguir...")
            os.system("cls")

        elif (opcao == 4):
            ip = input("Introduza o IP que quer fazer o ping: ")
            print("A enviar Pacotes...")
            time.sleep(3)
            print()
            funcoes.pingIN(ip)
            print ()
            input("Pressione qualquer tecla para proseguir...")
            os.system("cls")

        elif (opcao == 5):
            rede = input("Introduza o ip que deseja fazer o calculo (com o cidr): ")
            print ()
            print ("A calcular... ")
            time.sleep(3)
            print ()
            res=funcoes.calculadora(rede)

            if res:
                print("=========================================================")
                print("============       R E S U L T A D O         ============")
                print(f"========== Rede: {res['rede']}                    ============" )
                print(f"========== Broadcast: {res['broadcast']}             ============" )
                print(f"========== Mascara: {res['mascara']}            ============" )
                print(f"========== Hosts Disponiveis: {res['hosts_uteis']}            ============" )
                print("=========================================================")

            else:
                print("Inseriu um IP invalido ou sem o CIDR :( (ex: 10.0.0.0/24)")
            print ()
            input("Pressione qualquer tecla para proseguir...")
            os.system("cls")

        elif (opcao == 6):
            os.system("cls")
            while True:
                print ()
                
                print("================== M E N U  de  A D M I S T R A D O R  de  S I S T E M A S ==================")
                print("======== 1 - Verificar Espaco em Disco Selecionado                                   ========")
                print("======== 2 - Limpar Ficheiros Temporarios do Windows                                 ========")
                print("======== 3 - Fazer Backup de uma Pasta (.zip)                                        ========")
                print("======== 0 - Voltar ao menu anterior                                                 ========")
                print("=============================================================================================")
                
                print ()

                opcao = int(input("Selecione uma opcao: "))

                print()

                if (opcao == 1):
                    disco = input("Selecione o disco que deseja ver o espaco disponivel: ")
                    print()
                    print("A verificar o espaco...")
                    time.sleep(3)
                    print()
                    os.system(f'powershell "Get-PSDrive {disco}| Out-Host"')
                    print()
                    input("Pressione qualquer tecla para continuar...")
                    os.system("cls")

                elif (opcao == 2):
                    print ("Apesar de ser ficheiros temporarios, deseja mesmo eliminar todos? (Y/n)")
                    decisao = input(": ")

                    if (decisao == "Y" or "y"):
                        codigo_saida = os.system('del /q /f /s "%temp%\*" >nul 2>&1')

                        if (codigo_saida == 0):
                            print()
                            print("Todos os ficheiros temporarios eliminado com sucesso :) ")
                            print()
                            input("Pressiona qualquer tecla para continuar...")
                            os.system("cls")

                        else:
                            print()
                            print("Nao foram eliminados todos os ficheiros temporarios :( verfica se nao estas a usar nenhum neste momento")
                            print()
                            input("Pressiona qualquer tecla para continuar...")
                            os.system("cls")

                    elif (decisao == "N"or "n"):
                        print ("A voltar para o menu...")
                        time.sleep(3)
                    else:
                        print("Opcao invalida!")
                        

                elif (opcao == 0):
                    print ("A voltar ao menu anterior...")
                    time.sleep(3)
                    break

        elif (opcao == 0):
            print ("A fechar o Programa...")
            time.sleep(3)
            break

        else:
            print("Introduziu uma opcao invalida, por favor selecione um numero de 1 a 5 ou 0 se pretender sair.")
            time.sleep(3)
            os.system("cls")





