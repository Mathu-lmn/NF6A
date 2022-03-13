#include <stdio.h>
void main()
{
    int r1 = 3, r2 = 3, c1 = 3, c2 = 3;
    int ab[r1][c2], i, j, k, c, r, temp, sum[3][3];

    int a[3][3] = {1, 4, 2, 3, 6, 5, 3, 9, 4};
    int b[3][3] = {3, 5, 6, 4, 1, 8, 6, 4, 6};

    printf("\nMatrix a : ");
    for (i = 0; i < r1; i++)
    {
        printf("\n\t");
        for (j = 0; j < c1; j++)
        {
            printf("\t%d", a[i][j]);
        }
        printf("\n");
    }

    printf("\nMatrix b : ");
    for (i = 0; i < r2; i++)
    {
        printf("\n\t");
        for (j = 0; j < c2; j++)
        {
            printf("\t%d", b[i][j]);
        }
        printf("\n");
    }

    // Defining a*b
    for (i = 0; i < r1; i++)
    {
        for (j = 0; j < c2; j++)
        {
            temp = 0;
            for (k = 0; k < r2; k++)
            {
                temp += a[i][k] * b[j][k];
            }
            ab[i][j] = temp;
        }
    }

    // adding two matrices
    for (i = 0; i < r1; ++i)
    {
        for (j = 0; j < c1; ++j)
        {
            sum[i][j] = a[i][j] + b[i][j];
        }
    }

    printf("\nMatrix multiplication of a*b : ");
    for (i = 0; i < r1; i++)
    {
        printf("\n\t");
        for (j = 0; j < c2; j++)
        {
            printf("\t%d", ab[i][j]);
        }
        printf("\n");
    }
    
    printf("\nSum of the Matrices: \n");
    for (i = 0; i < r1; ++i)
    {
        printf("\n\t");
        for (j = 0; j < c1; ++j)
        {
            printf("\t%d", sum[i][j]);
        }
        printf("\n");
    }
}