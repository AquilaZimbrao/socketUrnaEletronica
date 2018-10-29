import os
import socket

votacao = [0]*8
pre = 'Fernando Haddad (13) / Jair Bolsonaro (17) / Branco (B)'
gov = 'Eduardo Paes (25) / Wilson Witzel (20) / Branco (B)'
HOST = '127.0.0.1'
PORT = 5000

def pegar_dados_conexao():
    print 'Informe o host do TRE'
    HOST = raw_input()
    print 'Informe a porta do TRE'
    PORT = input()
    limparTela()

def limparTela():
    if (os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")


def menu():
    print '1 - Iniciar Votacao\n2 - Modo Adminstrativo\n3 - Sair'
    asw = input()

    if (asw == 1):
        iniciarVotacao()
    elif (asw == 2):
        limparTela()
        menuAdmin()
    elif (asw == 3):
        limparTela()
        exit(1)
    else:
        limparTela()
        menu()



def menuAdmin():
    print '1 - Conferir Votos\n2 - Enviar relatorio de teste para o TRE\n3 - Sincronizar com o TRE\n4 - Voltar'
    asw = input()

    if (asw == 1):
        print map(str, votacao)
        print '\n Presione qualquer tecla para sair'
        t = raw_input()
        limparTela()
        menuAdmin()
    elif (asw == 2):
        enviarTRE('10 10 10 10 10 10 10 10')
        limparTela()
        menuAdmin()
    elif (asw == 3):
        votoSTR = map(str, votacao)
        enviarTRE(' '.join(votoSTR))
        votacao = [0]*8
        limparTela()
        menuAdmin()
    elif (asw == 4):
        limparTela()
        menu()
    else:
        limparTela()
        menuAdmin()


def iniciarVotacao():
    limparTela()
    print 'Iniciar Sessao de Voto (S/N): '
    asw = raw_input()

    if (asw != "s"):
        if (asw != "S"):
            limparTela()
            menu()

    limparTela()
    print 'Voto para Governador'
    print gov
    g = raw_input()
    limparTela()
    print 'Voto para Governador'
    print pre
    p = raw_input()

    if g == '25':
        votacao[0] += 1
    elif g == '20':
        votacao[1] += 1
    elif g == 'B' or g == 'b':
        votacao[2] += 1
    else:
        votacao[3] += 1

    if p == '13':
        votacao[4] += 1
    elif p == '17':
        votacao[5] += 1
    elif p == 'B' or p == 'b':
        votacao[6] += 1
    else:
        votacao[7] += 1

    limparTela()
    iniciarVotacao()

def enviarTRE(vot):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    tcp.send(vot)
    tcp.close()

limparTela()
pegar_dados_conexao()
menu()