#include <stdio.h>
#include <stdlib.h>

// STRUCT NÓ (NODE)
struct Node {
    int data;
    struct Node* next;
};

int main() {
    //VARIÁVEIS INTEIRAS
    
    int vetor[5];
    int cont = 0;
    int modf = 0;
    int pos = 0;
    int rem = 0;
    
    //HEAD APONTANDO PARA O PRIMEIRO NÓ DA LISTA
    struct Node* head = NULL;

    //VERIFICANDO SE A LISTA ESTÁ VAZIA
    if (head == NULL) {
        printf("A lista estah vazia.\n");
    } else {
        printf("A lista não está vazia.\n");
    }

    //USUÁRIO ADICIONA 5 ELEMENTOS NA LISTA
    printf("Digite 5 numeros para acrescentar na lista: \n");
    for (cont = 0; cont < 5; cont++){
        printf("Digite o '%d' numero para acrescentar na lista: ", cont+1);
        scanf("%d", &vetor[cont]);
    }

     //IMPRIMINDO O VETOR EM UM LAÇO DE REPETIÇÃO
    for(cont = 0; cont < 5; cont++){
        printf("\nPosicao %d : %d", cont+1, vetor[cont] );
    }

   
    //INSERINDO OS DADOS PARA CADA UM DOS NÓS
    struct Node* node1 = malloc(sizeof(struct Node));
    node1->data = vetor[0];
    node1->next = NULL;
    head = node1;

    struct Node* node2 = malloc(sizeof(struct Node));
    node2->data = vetor[1];
    node2->next = NULL;
    node1->next = node2;

    struct Node* node3 = malloc(sizeof(struct Node));
    node3->data = vetor[2];
    node3->next = NULL;
    node2->next = node3;

    struct Node* node4 = malloc(sizeof(struct Node));
    node4->data = vetor[3];
    node4->next = NULL;
    node3->next = node4;

    struct Node* node5 = malloc(sizeof(struct Node));
    node5->data = vetor[4];
    node5->next = NULL;
    node4->next = node5;

    //CÁLCULO DO TAMANHO DA LISTA
    int size = 0;
    struct Node* current = head;
    while (current != NULL) {
        size++;
        current = current->next;
    }
    printf("\n");
    printf("O tamanho da lista eh %d.\n", size);

    //MODIFICANDO UM ITEM DA LISTA 
   
    printf("Seleciona a posicao entre 1 e 5 para substituir o valor: \n");
    scanf("%d", &pos);
    printf("Digite o novo valor para a posicao: \n");
    scanf("%d", &modf);

    //REALOCANDO O NOVO VALOR PARA A POSIÇÃO REQUERIDA
    switch (pos)
    {
    case 1:
        vetor[0] = modf;
        break;
    case 2:
        vetor[1] = modf;
        break;
    case 3:
        vetor[2] = modf;
        break;
    case 4:
        vetor[3] = modf;
        break;
     case 5:
        vetor[4] = modf;
        break;
    }

    //IMPRIMINDO O VETOR NOVO LINEARMENTE
    printf("\n---------------------------------\n");
    printf("NOVO VETOR: [ %d, %d, %d, %d, %d]\n",  vetor[0], vetor[1], vetor[2], vetor[3], vetor[4]);
    printf("----------------------------------\n");
    
    //IMPRIMINDO O VETOR EM UM LAÇO DE REPETIÇÃO COM A POSIÇÃO
    for(cont = 0; cont < 5; cont++){
        printf("\nPosicao %d : %d", cont+1, vetor[cont]);
    }
    printf("\n");
  
    printf("Seleciona a posicao entre 1 e 5 para remover o valor: \n");
    scanf("%d", &rem);

    for (int i = rem-1; i < 4; i++) {
      vetor[i] = vetor[i + 1];
   }

    //IMPRIMINDO O VETOR NOVO LINEARMENTE
    printf("\n----------------------------------\n");
    printf("NOVO VETOR: [ %d, %d, %d, %d]\n",  vetor[0], vetor[1], vetor[2], vetor[3]);
    printf("----------------------------------\n");
    

    return 0;
}