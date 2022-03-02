#include <stdio.h>

int main() { 
    float i = 44.56;
    float j = 64.34;

    float temp = j;
    j = i;
    i = temp;
    printf("i = %g and j = %g", i, j);
}