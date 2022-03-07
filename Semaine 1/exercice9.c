#include <stdio.h>

int main()
{
    int num, bin, dec = 0, base = 1, rem;
    printf(" Enter a binary number with the combination of 0s and 1s : ");
    scanf(" %d", &num);

    bin = num;

    while (num > 0)
    {
        rem = num % 10;
        dec = dec + rem * base;
        num = num / 10;
        base = base * 2;
    }

    printf("\n The binary number is %d \t", bin);
    printf(" \n The decimal number is %d \t", dec);
    return 0;
}