#include <stdio.h>

int main()
{
    int arr[6] = {'2', '5', '1', '6', '3', '9'};
    int temp, n = 6, i;
    temp = arr[5];
    arr[5] = arr[3];
    arr[3] = temp;
    printf("\nArray elements after swapping elements:\n");
    for (i = 0; i < n; i++)
    {
        printf("%c\n", arr[i]);
    }
}