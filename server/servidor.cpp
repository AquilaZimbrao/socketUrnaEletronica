#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <bits/stdc++.h>

using namespace std;

int lula = 0, meireles = 0, marina = 0, bolsonaro = 0, alckmin = 0;

void error(const char *msg)
{
    perror(msg);
}

void printResult() {
    system("clear");
    printf("13 - Lula: %d\n", lula);
    printf("15 - Meireles: %d\n", meireles);
    printf("16 - Marina: %d\n", marina);
    printf("17 - Bolsonaro: %d\n", bolsonaro);
    printf("45 - Alckmin: %d\n", alckmin);
}

int main(int argc, char *argv[])
{
     int sockfd, newsockfd, portno;
     socklen_t clilen;
     char msg[256];
     struct sockaddr_in serv_addr, cli_addr;
     int size_msg;

     if (argc < 2) {
         fprintf(stderr,"ERROR: Falta informar a porta\n");
         exit(1);
     }
     sockfd = socket(AF_INET, SOCK_STREAM, 0);
     
     if (sockfd < 0) 
        error("ERROR ao abrir socket");
     bzero((char *) &serv_addr, sizeof(serv_addr));
     portno = atoi(argv[1]);
     
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);
     if (bind(sockfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0) 
              error("ERROR ao validar socket: ");
     
     listen(sockfd,5);
     clilen = sizeof(cli_addr);

    while(1 == 1) {
        newsockfd = accept(sockfd, 
                 (struct sockaddr *) &cli_addr, 
                 &clilen);
        if (newsockfd < 0) 
            error("ERROR on accept");
        
        size_msg = read(newsockfd, msg, 2);

        if (size_msg < 0) error("ERROR reading from socket");
        
        int voto = atoi(msg);
        int erro = 0;

        switch(voto) {
            case 13:
                lula += 1;
                break;
            case 15:
                meireles += 1;
                break;
            case 16:
                marina += 1;
                break;
            case 17:
                bolsonaro += 1;
                break;
            case 45:
                alckmin += 1;
                break;
            default:
                erro += 1;
        }

        if (erro == 1) {
            size_msg = write(newsockfd, "Voto Invalido", 13);
            if (size_msg < 0) error("ERROR ao escrever no socket");
        } else {
            printResult();
            size_msg = write(newsockfd, "Voto computado com sucesso", 26);
            if (size_msg < 0) error("ERROR ao escrever no socket");
        }
    
        close(newsockfd);
    }
    close(sockfd);
    return 0;
}