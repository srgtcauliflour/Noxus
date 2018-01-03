from Noxus import computer
from Noxus import cpu
from Noxus import memory

import sys

params = sys.argv

if len(params) > 1:
    if params[1] == "os" or params[1] == "system":
        print("Sistema operacional: ", computer.os())
        print("Versao: ", computer.osVersion())
    elif params[1] == "name":
        print("Node de rede:", computer.name())
    elif params[1] == "distro":
        print("Distribuicao: ", computer.distro())
    elif params[1] == "processor" or params[1] == "-p":
        if len(params) == 4 and params[2] == "percentage" and int(params[3]) >= 1:
            for x in range(int(params[3])):
                consume = cpu.percentage()
                print("Consumindo: ", consume.user + consume.system, "%")
                print("Livre: ", consume.idle,"%")
                print("_________________________")
        elif len(params) == 4 and params[2] == "benchmarking" and int(params[3]) >= 1:
            print("Analisando uso da CPU...")
            media = 0
            for x in range (int(params[3])):
                consume = cpu.percentage()
                media += consume.user + consume.system
            media = media/int(params[3])
            print("Média de consumo da CPU durante", params[3],"segundos:", media, " % ")
        else:
            print("Processador: ", computer.cpu())
            print("Velocidade: ", cpu.freq(),"GHz")
            print("Cores: ", cpu.cores())
            print("Cores Fisicos: ", cpu.phyCores())
    elif params[1] == "memory" or params[1] == "-m":
        if str(params).find("size") > 0:
            print("Tamanho da memoria: ", memory.size(), "GBs")
        if str (params).find("Ppercentage") > 0:
            print("Consumo atual da memoria: ", memory.percentage(), "%")
        if str(params).find("free") > 0:
            print("Memoria livre: ", memory.free(), "GBs")    
    elif params[1] == "arc":
        print("Arquitetura da maquina:", computer.arc())
    else:
        print("Parametro desconhecido!")
else:
    print("Sistema operacional: ", computer.os())