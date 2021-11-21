from connection import *
import time

def operacoes(operacao):
    if operacao == 1:
        musica = input("Digite o nome da música: ")
        
        selectArtistas()
        listaArtista = []
        boolArtista = True
        while boolArtista:
            artista = input("Digite o Id do artista dessa música: ")
            listaArtista.append(artista)
            operacao2 = int(input("\nMais artistas estavam envolvidos na música?\n\t1 - Sim\n\t(Qualquer outro número) - Não\n"))
            if operacao2 != 1:
                boolArtista = False
        insert_bd(musica, operacao)
        associarArtMusica(listaArtista, selectLastMusic())
        
    elif operacao == 2:
        artista = input("Digite o nome do artista: ")
        insert_bd(artista, operacao)
    elif operacao == 3:
        print("\nAté a próxima :)")
        exit()
    else:
        print("Escolha um número válido")

print(f"----------========== BEM VINDO ==========----------\n\n")

while True:
    print("OPERAÇÕES:\n\t1 - Adicionar uma Música\n\t2 - adicionar Artista\n\t3 - Sair\n")

    operacao = int(input("Operação: "))
    operacoes(operacao);


