import socket
import threading
import time
import os

TIME = 5
TIMESYNC = 7
HOST = ''
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

votacao = [0]*4


def limparTela():
    if (os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")


def printRelatorio(args):
    while True:
        time.sleep(TIME)
        limparTela()
        print 'Eduardo Paes (DEM) - ' + str(votacao[0])
        print 'Wilson Witzel (?) - ' + str(votacao[1])
        print 'Brancos - ' + str(votacao[2])
        print 'Nulos - ' + str(votacao[3])
        print 'Fernando Haddad (PT) - ' + str(votacao[4])
        print 'Jair Bolsonaro (PSL) - ' + str(votacao[5])
        print 'Brancos - ' + str(votacao[6])
        print 'Nulos - ' + str(votacao[7])

def enviarTSE(args):
    HOSTTSE = '127.0.0.1'
    PORTTSE = 5010
    tcpTSE = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destTSE = (HOSTTSE, PORTTSE)
    tcpTSE.connect(destTSE)
    vot = map(str, votacao)
    tcpTSE.send(vot)
    tcpTSE.close()

t = threading.Thread(target=printRelatorio,args=("thread sendo executada",))
t.start()
ts = threading.Thread(target=enviarTSE,args=("thread sendo executada",))
ts.start()

while True:
    con, cliente = tcp.accept()
    msg = con.recv(1024)

    relatorioUrna = msg.split(' ')
    votacao[0] += int(relatorioUrna[0])
    votacao[1] += int(relatorioUrna[1])
    votacao[2] += int(relatorioUrna[2])
    votacao[3] += int(relatorioUrna[3])
    votacao[0] += int(relatorioUrna[4])
    votacao[1] += int(relatorioUrna[5])
    votacao[2] += int(relatorioUrna[6])
    votacao[3] += int(relatorioUrna[7])