#include <stdio.h>

int num, oct, dec, base = 1, rem;

int main()
{
    printf(" Enter a decimal number : ");
    scanf(" %d", &num);

    dec = num;

    while (num > 0)
    {
        rem = num % 8;
        oct = oct + rem * base;
        num = num / 8;
        base = base * 10;
    }

    printf("\n The decimal number is %d \t", dec);
    printf(" \n The octal number is %d \t", oct);
    return 0;
}