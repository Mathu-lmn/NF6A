#include <stdio.h>

int main()
{
    unsigned short A = 104;
    unsigned short B = 6.5;
    float C = 5;
    A += (int)C;         // A becomes A + the integer part of C
    A = ~A;              // A becomes it's bitwise complement
    B = A ^ (A + 2);     // B becomes the bitwise exclusive or between A and A+2
    C = (float)(A << B); // C becomes the leftshift of A by B
    A = A & (int)C;      // A becomes the bitwise AND between A and the integer of C
}