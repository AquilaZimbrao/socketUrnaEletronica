import socket
import threading
import time
import os

TIME = 5
HOST = ''
PORT = 5010
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
        print 'Fernando Haddad (PT) - ' + str(votacao[0])
        print 'Jair Bolsonaro (PSL) - ' + str(votacao[1])
        print 'Brancos - ' + str(votacao[2])
        print 'Nulos - ' + str(votacao[3])


t = threading.Thread(target=printRelatorio,args=("thread sendo executada",))
t.start()

while True:
    con, cliente = tcp.accept()
    msg = con.recv(1024)
    msg = msg.replace('\n', '')

    relatorioUrna = msg.split(' ')
    votacao[0] += int(relatorioUrna[0])
    votacao[1] += int(relatorioUrna[1])
    votacao[2] += int(relatorioUrna[2])
    votacao[3] += int(relatorioUrna[4])