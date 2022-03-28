#include <stdio.h>
#include <stdlib.h> 

void enterVector(int n, int *vecteur[]) {
    int i;
    *vecteur = malloc(n * sizeof(int));
    
    for (i = 0; i < n; i++) {
        printf("Enter element n%d\n", (i + 1));
        scanf("%d", &(*vecteur)[i]);
    }
}

void printVector(int n, int vecteur[]) {
    int i;
    for (i = 0; i < n; i++) {
        printf("%d\n", vecteur[i]);
    }
}

int *sumVector(int n, int *A, int *B){
    int i;
    int *vector;
    vector = malloc(n * sizeof(int));
    
    for (i = 0; i < n; i++) {
        vector[i] = A[i] + B[i];
    }
    return vector;
}

int *subVector(int n, int *A, int *B){
    int i;
    int *vector;
    vector = malloc(n * sizeof(int));

    for (i = 0; i < n; i++){
        vector[i] = A[i] - B[i];
    }
    return vector;
}

int prodscal(int n, int *A, int *B) {
    int i;
    int scal;

    scal = 0;
    for (i = 0; i < n; i++) {
        scal += A[i] * B[i];
    }
    return scal;
}


int main() {
    int n;
    int *A = NULL;
    int *B = NULL;
    int *C = NULL;
    printf("Enter the number of elements in the vectors : ");
    scanf("%d", &n);
    printf("Vector A :\n");
    enterVector(n, &A);
    printf("\nVector B :\n");
    enterVector(n, &B);   
    printf("_______________________\n");
    
    printf("\nA=\n");
    printVector(n, A);
    printf("\nB=\n");
    printVector(n, B);
    
    printf("\nA+B=\n");
    C = sumVector(n, A, B);
    printVector(n, C);
    free(C);

    printf("\nA-B=\n");
    C = subVector(n, A, B);
    printVector(n, C);
    free(C);
    
    printf("\nA.B=%d\n", prodscal(n, A, B));

    free(A);
    free(B);
}