#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int num, digit, res, n;
char a[20];
int r, len, temp;

bool iszero(int num)
{
    if (num > 1)
    {
        digit = num % 10;
        if (digit == 0)
            res = 1;
        else
            return iszero(num / 10);
    }
    else
        return 0;
    return res;
}

int prime(int n)
{
    if (n == 2)
        return 1;
    else
    {
        int k = 2;
        int z = 1;
        while (k < n)
        {
            while ((prime(k) == 0) && (k < n - 1))
            {
                k++;
            };
            if (n % k == 0)
            {
                z = 0;
                k++;
            }
            else
                k++;
        };
        return z;
    };
}

int fibbonacci(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        return (fibbonacci(n - 1) + fibbonacci(n - 2));
    }
}

bool isPalindrome(char a[], int r, int len)
{
    if (a[r] != a[len - r - 1])
    {
        return false;
    }
    else if (r < (len / 2))
    {
        r++;
        return isPalindrome(a, r, len);
    }
    return true;
}

int i;
int main()
{
    printf("Choose the exercise you want to do : ");
    scanf("%d", &i);
    switch (i)
    {
    case 1:
        int z, b, c, disc, root1, root2;
        printf("Enter the coefficient for x^2 :");
        scanf("%d", &z);
        printf("Enter the coefficient for x :");
        scanf("%d", &b);
        printf("Enter the integer :");
        scanf("%d", &c);

        disc = b * b - 4 * z * c;
        if (disc > 0)
        {
            root1 = (float)(-b - sqrt(disc)) / 2 * z;
            root2 = (float)(-b + sqrt(disc)) / 2 * z;
            printf("The solution for the equation %d*x^2 + %d*x + %d = 0 are : \nx = %d \nx = %d", z, b, c, root1, root2);
        }
        else if (disc == 0)
        {
            root1 = -b / (float)(2 * z);
            printf("The solution for the equation %d*x^2 + %d*x + %d = 0 is : \nx = %d", z, b, c, root1);
        }
        else
            printf("There is no real solution for the equation %d*x^2 + %d*x + %d = 0", z, b, c);
        return 0;
        ;
        break;
    case 2:
        int i;
        for (i = 2; i < 30; i++)
            if (prime(i) == 1)
                printf("%d\n", i);
            else
                continue;
        ;
        break;
    case 3:
        int arr[] = {45, 5, -5, 8, 66};

        int length = sizeof(arr) / sizeof(arr[0]);

        int max = arr[0];

        for (int i = 0; i < length; i++)
        {
            if (arr[i] > max)
                max = arr[i];
        }
        printf("Largest element in the array: %d\n", max);
        return 0;
        ;
        break;
    case 4:
        printf("Enter a number :");
        scanf("%d", &num);
        if (iszero(num) == 1)
            printf("The number have at least 1 zero in its decimal form");
        else
            printf("There is no zero in this number");
        ;
        break;
    case 5:
        printf("Please give an input upto you want to print series : ");
        scanf("%d", &n);
        printf("Fibonacci Series is:\n");
        int k;
        for (k = 0; k < n; k++)
        {
            printf("%d ", fibbonacci(k));
        };
        break;
    case 6:
        getchar();
        gets(a);
        len = strlen(a);
        if (isPalindrome(a, r, len) == 1)
        {
            printf("This word is a palindrome");
        }
        else
        {
            printf("This word is not a palindrome");
        };
        break;
    }
}