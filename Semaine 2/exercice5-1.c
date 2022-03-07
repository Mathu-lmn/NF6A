#include <stdio.h>
int n, first = 0, second = 1, res, i;

int main() {
  printf("Please give an input upto you want to print series : ");
  scanf("%d", &n);
  printf("Fibonacci Series is:\n");
  for (i = 0; i < n; i++) {
    if (i <= 1)
      res = i;
    else {
      res = first + second;
      first = second;
      second = res;
    }
    printf("%d\n", res);
  } 
  return 0;
} 