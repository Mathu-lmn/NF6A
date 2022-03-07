#include <stdio.h>

int B = 7; // it's the base of the triangle
int H = 9; // it's the height of the triangle

int main()
{
    int A = (B * H) / 2;
    printf("The area of a triangle with a base of %d and a height of %d is approximately %d", B, H, A);
}