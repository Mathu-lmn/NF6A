#include <stdio.h>

int main()
{
    int i = 23;
    int j = 455;
    int max = i > j ? i : j;
    int min = max == i ? j : i;
    printf("Max = %d \nMin = %d", max, min);
    return 0;
}