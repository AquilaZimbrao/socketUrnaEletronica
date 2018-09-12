#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 

void error(const char *msg)
{
    perror(msg);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, size_msg;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char msg[256];


    if (argc < 3) {
       fprintf(stderr,"usage %s hostname port\n", argv[0]);
       exit(0);
    }
    
    while (1 == 1) {
        portno = atoi(argv[2]);
        sockfd = socket(AF_INET, SOCK_STREAM, 0);

        if (sockfd < 0) 
            error("ERROR opening socket");
        
        server = gethostbyname(argv[1]);
        
        if (server == NULL) {
            fprintf(stderr,"ERROR, no such host\n");
            exit(0);
        }


        bzero((char *) &serv_addr, sizeof(serv_addr));
        serv_addr.sin_family = AF_INET;
        bcopy((char *)server->h_addr, 
            (char *)&serv_addr.sin_addr.s_addr,
            server->h_length);
        serv_addr.sin_port = htons(portno);
        if (connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0) 
            error("ERROR connecting");

        
        //Interface do cliente
        printf("Digite o seu voto: ");
        bzero(msg,256);
        fgets(msg,255,stdin);
        
        
        //Grava msg no Socket (enviar para server)
        size_msg = write(sockfd, msg, strlen(msg));
        if (size_msg < 0) 
            error("ERROR ao escrever no socket");
    
        //Lendo responsta do server
        bzero(msg,256);
        size_msg = read(sockfd, msg,255);
        if (size_msg < 0) 
            error("ERROR ao ler resposta");

        //Inteface do usuario: print resposta do server
        printf("%s\n",msg);
        //system("clear");
        close(sockfd);
    }
    return 0;
}