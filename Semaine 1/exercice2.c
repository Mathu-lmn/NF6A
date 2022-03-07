#include <stdio.h>

int main()
{
    int i = 5; // does not works as you're trying to divide a number by 0
    int j = 5;
    // Division de j par i
    printf(" Division de j par i = % d ", j / i);
    return 0;
}