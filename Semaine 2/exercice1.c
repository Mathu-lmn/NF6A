#include <stdio.h>
#include <math.h>

int a,b,c,disc,root1,root2;

int main() {
    printf("Enter the coefficient for x^2 :");
    scanf("%d",&a);
    printf("Enter the coefficient for x :");
    scanf("%d",&b);
    printf("Enter the integer :");
    scanf("%d",&c);

    disc = b*b-4*a*c;
    if (disc>0) {
        root1 = (float)(-b - sqrt(disc)) / 2*a; 
        root2 = (float)(-b + sqrt(disc)) / 2*a;
        printf("The solution for the equation %d*x^2 + %d*x + %d = 0 are : \nx = %d \nx = %d",a,b,c,root1,root2);
    }
    else if (disc == 0) {
        root1 = -b/(float)(2*a);
    printf("The solution for the equation %d*x^2 + %d*x + %d = 0 is : \nx = %d",a,b,c,root1);
    }
    else
        printf("There is no real solution for the equation %d*x^2 + %d*x + %d = 0",a,b,c);
    return 0;
}