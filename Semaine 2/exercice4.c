#include <stdio.h>
#include <stdbool.h>

int num, digit, res;

bool iszero(int num)
{
    if (num > 0)
    {
        digit = num % 10;
        if (digit == 0)
            return 1;
        else
            return iszero(num / 10);
    }
    else
        return 0;
}
int main()
{
    printf("Enter a number :");
    scanf("%d", &num);
    if (iszero(num) == 1)
        printf("The number have at least 1 zero in its decimal form");
    else
        printf("There is no zero in this number");
}