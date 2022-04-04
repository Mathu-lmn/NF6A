#include <stdio.h>

int main() {
    int i,j,M,N;
    FILE *ptr;
    char name[20];
    printf("Input a file name : ");
    scanf("%s",name);
    printf("Enter the number of vectors : ");
    scanf("%d",&M);
    printf("Input the size of the vectors : ");
    scanf("%d",&N);
    int a[M][N];
    for(i = 0; i < M; i++) {
        for(j = 0; j < N; j++) {
            printf("Enter value for a[%d][%d] : ", i, j);
            scanf("%d", &a[i][j]);
        }
    }
    //File Creation
    ptr = fopen(name,"w");
    fprintf(ptr, "%s", "I write in the file ! \n");
    fprintf(ptr, "%s","\nInput Vectors a : ");
    //Printing the Matrix in the file
    for (i = 0; i < M; i++)
    {  
        fprintf(ptr,"\n\t");
        for (j = 0; j < N; j++)
        {
            fprintf(ptr,"\t%d", a[i][j]);
        }
        fprintf(ptr,"\n");
    }
    //Calculate a new Vector as sum of first 2
    fprintf(ptr, "%s","\nSum of the first 2 vectors :\n");
    int sum[N];
    for (i = 0; i < N; i++) {
        sum[i] = a[0][i] + a[1][i];
        fprintf(ptr,"%d\t",sum[i]);
    }
    
    fclose(ptr);
}