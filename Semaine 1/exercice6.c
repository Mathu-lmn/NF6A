#include <stdio.h>
#include <math.h>

int i;
int a;

int main()
{
    printf("Enter one number :");
    scanf("%d", &i);
    float p = 3;
    int n = 2;
    float j = pow(2, p) - 1;
    int u = (int)j;
    a = u << (n - 1);
    i = i ^ a;
    printf("j = %d", i);
    return 0;
}