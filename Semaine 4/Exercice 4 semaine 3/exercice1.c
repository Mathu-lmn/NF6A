#include <stdio.h>
#include <stdlib.h>


void enterVector(int n, double *vecteur[]) {
    int i;

    *vecteur = malloc(n * sizeof(double));
    if (*vecteur == NULL) {
        printf("Can't allocate memory");
        exit(0);
    }

    for (i = 0; i < n; i++) {
        printf("Enter element n%d\n", (i + 1));
        scanf("%lf", &(*vecteur)[i]);
    }
}


void printVector(int n, double vecteur[]) {
    int i;
    for (i = 0; i < n; i++) {
        printf("%lf\n", vecteur[i]);
    }
}


double *sumVector(int n, double *A, double *B) {
    int i;
    double *vecteur;

    vecteur = malloc(n * sizeof(double));
    if (vecteur == NULL) {
        printf("Can't allocate memory");
        exit(0);
    }

    for (i = 0; i < n; i++) {
        vecteur[i] = A[i] + B[i];
    }
    return vecteur;
}


double *substractVector(int n, double *A, double *B) {
    int i;
    double *vecteur;

    vecteur = malloc(n * sizeof(double));
    if (vecteur == NULL) {
        printf("Can't allocate memory");
        exit(0);
    }

    for (i = 0; i < n; i++) {
        vecteur[i] = A[i] - B[i];
    }
    return vecteur;
}

double prodscalVector(int n, double *A, double *B) {
    int i;
    double prod;

    prod = 0;
    for (i = 0; i < n; i++) {
        prod += A[i] * B[i];
    }
    return prod;
}

int main(int argc, char const *argv[]) {
    int n;
    double *A = NULL;
    double *B = NULL;
    double *C = NULL;

    printf("Enter the number of elements of the vectors\n");
    scanf("%d", &n);
    printf("Enter vector A\n");
    enterVector(n, &A);
    printf("Enter vector B\n");
    enterVector(n, &B);
    printf("_______________________\n\n");

    printf("\nA=\n");
    printVector(n, A);
    printf("\nB=\n");
    printVector(n, B);

    printf("\nA+B=\n");
    C = sumVector(n, A, B);
    printVector(n, C);
    free(C);

    printf("\nA-B=\n");
    C = substractVector(n, A, B);
    printVector(n, C);
    free(C);

    printf("\nA.B=%lf\n", prodscalVector(n, A, B));

    free(A);
    free(B);
    return 0;
}