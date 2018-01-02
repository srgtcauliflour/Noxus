from Noxus import computer
import sys

params = sys.argv


if len(params) > 1:
    if params[1] =="os" or params[1] == "system":
        print("Sistema Operacional: ", computer.os())
        print("versao: ", computer.osVersion())
    elif params[1] == "name":
        print("Node de Rede: ", computer.name())
    elif params[1] == "distro":
        print("Distribuicao: ", computer.distro())
    elif params[1] == "processor", or params[1] == "-p":
        print("processador: ", computer.cpu())
    elif params[1] == "arc":
        print("Arquitetura da Maquina")
    else:
        print("Parametro desconhecido!")
else:
    print("Sistema Operacional: ", computer.os())