#Toolkit de Redes & Automação SysAdmin

---

Uma ferramenta de linha de comandos (CLI) desenvolvida em Python para ambientes Windows. Este toolkit reúne as ferramentas de diagnóstico de rede mais essenciais e automatiza tarefas diárias de Administração de Sistemas (SysAdmin) num menu interativo e de fácil utilização.

---

#Funcionalidades
O projeto está dividido em dois módulos principais:

 Menu de Rede
 
 - Teste de Conectividade: Verifica o estado da ligação à internet.

 - Informações de Rede Local: Descobre instantaneamente o IP local e o nome da máquina (Hostname).

 - Resolução de DNS: Descobre o IP público por detrás de qualquer domínio/site.

 - Ping Personalizado: Ferramenta de ping rápido para diagnóstico de latência ou quebras.

 - Calculadora IPv4 (CIDR): Calcula automaticamente a Máscara, Rede, Broadcast e Hosts Úteis a partir de um IP com anotação CIDR, corrigindo inputs de utilizador dinamicamente.

Menu de Administração de Sistemas
 - Análise de Armazenamento: Verifica o espaço total, usado e livre de qualquer disco/partição através de integração com o PowerShell.

 - Limpeza de Ficheiros Temporários: Varre e elimina silenciosamente o lixo acumulado na pasta %TEMP% do Windows, ignorando ficheiros em uso.

 - Sistema de Backups Rápidos: Comprime qualquer diretoria num ficheiro .zip com um único clique.

---

#Como Executar

Pré-requisitos

 - Sistema Operativo Windows.

 - Python 3.x instalado na máquina. (Não são necessárias bibliotecas externas, o projeto usa apenas bibliotecas nativas como os, shutil, time e ipaddress).

---

#Instalação e Uso
Faz o download ou clone deste repositório:

Bash
git clone (https://github.com/g-silva-005/APPMonitorizarRede.git)
Navega até à pasta do projeto.

Faz duplo clique no ficheiro programa.bat.

Nota: O ficheiro .bat configura automaticamente a cor do terminal, ajusta a pasta de trabalho (mesmo se aberto como Administrador) e lança o script Python de forma limpa.

---

#Estrutura do Projeto
main.py - O motor principal da aplicação, responsável pelos menus interativos e pela interface do utilizador.

funcoes.py - Módulo de suporte contendo funções isoladas e lógica de rede/sistema.

programa.bat - Script de arranque rápido para o terminal do Windows.
