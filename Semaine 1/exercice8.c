#include <stdio.h>
#define PI 3.1416

int R = 5;
int H = 10;

int main()
{
    float V = (PI * R * R * H) / 3;
    printf("PI = %0.4f", V);
}