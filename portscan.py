#AUTHOR: Edson Brenno
#DATA: 02/20/2021
#contact: bytegold64@gmail.com
#Descripition: Portscan

#!/usr/bin/python3.9

import sys
import socket
import os

#validar se todos os agumentos foram passados:

if (len(sys.argv) < 2): #se Faltar a passagem de argumentos:
    print("Host Discover --help")
    print("Sintaxe: {} [ip]" .format(sys.argv[0]))
    print("Ex: {} {}".format(sys.argv[0],"192.168.1.1"))
elif (str("{}".format(sys.argv[1])) == "--help"): #se o usuario usar o --help
    print("Host Discover --help")
    print("Sintaxe: {} [ip]" .format(sys.argv[0]))
    print("Ex: {} {}".format(sys.argv[0],"192.168.1.1"))
elif (str("{}".format(sys.argv[1])) == "-h"): #se o usuario usar o -h
    print("Host Discover --help")
    print("Sintaxe: {} [ip]" .format(sys.argv[0]))
    print("Ex: {} {}".format(sys.argv[0],"192.168.1.1"))
else: #Inicia o processo:
    a = "figlet ETB"
    b = " figlet PORTSCAN"
    print("===================================================================")
    os.system(a) #o nome ETB
    os.system(b) #O nome PORTSCAN
    print("===================================================================")
    print("       [+] Testando se o host {} esta ativo ".format(sys.argv[1]))
    #vamos Testar se o host esta ativo:
    test = os.popen("ping -c 1 {} | grep 'received' | cut -d ' ' -f4".format(sys.argv[1]))
    t1 = int(test.readline()) #transformar o resultado do ping em int
    if (t1 == 1): #se o host etive ativo:
        print("===================================================================")
        print("                     [+] Testando as portas")
        print("===================================================================")
        print("        IP                  PORTA             STATUS   ")
        print("===================================================================")
        for c in range(65535):
            try:
                d_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            except socket.error as err:
                print("Criancao do socket nao completada. Erro: {}".format(err))
            
            t = d_socket.connect_ex((sys.argv[1],c)) #teste de conexao
            if ( t == 0): #se t for igual a 0 o host esta ativo
                print("   {}               {}               ATIVO".format(sys.argv[1],c))
                d_socket.close()
        print("===================================================================")
    else: #se o host nao estiver ativo
        print("===================================================================")
        print("               O HOST {} NAO ESTA ATIVO".format(sys.argv[1]))
        print("===================================================================")
            
            
