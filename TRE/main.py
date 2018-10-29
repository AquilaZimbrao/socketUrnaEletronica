import socket
import thread
import threading
import time
import os

TIME = 1
TIMESYNC = 1
HOST = ''
PORT = 5000
HOSTTSE = '127.0.0.1'
PORTTSE = 5010

votacao = [0]*8
votacaoAcumulativa = [0]*8

def pegar_dados_conexao():
    global PORT, HOSTTSE, PORTTSE
    print 'Informe a porta na qual deseja trabalhar'
    PORT = input()
    print 'Informe o host do TSE'
    HOSTTSE = raw_input()
    print 'Informe a porta do TSE'
    PORTTSE = input()
    limparTela()

def limparTela():
    if (os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")


def printRelatorio(args):
    while True:
        time.sleep(TIME)
        limparTela()
        print 'Eduardo Paes (DEM) - ' + str(votacaoAcumulativa[0])
        print 'Wilson Witzel (PSC) - ' + str(votacaoAcumulativa[1])
        print 'Brancos - ' + str(votacaoAcumulativa[2])
        print 'Nulos - ' + str(votacaoAcumulativa[3])
        print 'Fernando Haddad (PT) - ' + str(votacaoAcumulativa[4])
        print 'Jair Bolsonaro (PSL) - ' + str(votacaoAcumulativa[5])
        print 'Brancos - ' + str(votacaoAcumulativa[6])
        print 'Nulos - ' + str(votacaoAcumulativa[7])

def enviarTSE(args):
    while True:
        time.sleep(TIMESYNC)
        global votacao
        tcpTSE = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destTSE = (HOSTTSE, PORTTSE)
        tcpTSE.connect(destTSE)
        vot = map(str, votacao)
        tcpTSE.send(' '.join(vot))
        votacao = [0]*8
        tcpTSE.close()


pegar_dados_conexao()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)


t = threading.Thread(target=printRelatorio,args=("thread sendo executada",))
t.start()
ts = threading.Thread(target=enviarTSE,args=("thread sendo executada",))
ts.start()

def conectado(con, cliente):

    while True:
        msg = con.recv(1024)
        msg = msg.replace('\n', '')

        if (len(msg)):
            relatorioUrna = msg.split(' ')
            votacao[0] += int(relatorioUrna[0])
            votacao[1] += int(relatorioUrna[1])
            votacao[2] += int(relatorioUrna[2])
            votacao[3] += int(relatorioUrna[3])
            votacao[4] += int(relatorioUrna[4])
            votacao[5] += int(relatorioUrna[5])
            votacao[6] += int(relatorioUrna[6])
            votacao[7] += int(relatorioUrna[7])

            votacaoAcumulativa[0] += int(relatorioUrna[0])
            votacaoAcumulativa[1] += int(relatorioUrna[1])
            votacaoAcumulativa[2] += int(relatorioUrna[2])
            votacaoAcumulativa[3] += int(relatorioUrna[3])
            votacaoAcumulativa[4] += int(relatorioUrna[4])
            votacaoAcumulativa[5] += int(relatorioUrna[5])
            votacaoAcumulativa[6] += int(relatorioUrna[6])
            votacaoAcumulativa[7] += int(relatorioUrna[7])


while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))
    