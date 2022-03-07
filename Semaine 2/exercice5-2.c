#include <stdio.h>
int n;

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

int main()
{
   printf("Please give an input upto you want to print series : ");
   scanf("%d", &n);
   printf("Fibonacci Series is:\n");
   int i;
   for (i = 0; i < n; i++)
   {
      printf("%d ", fibbonacci(i));
   }
}