#include <stdio.h>

int main()
{
    char sentence[100], i;
    int upper = 0, lower = 0, number = 0, whitesp = 0;
    printf("Write the sentence : ");
    gets(sentence);
    for (i = 0; i < sentence[i] != '\0'; i++)
    {
        if (sentence[i] >= 'A' && sentence[i] <= 'Z')
            upper++;
        else if (sentence[i] >= 'a' && sentence[i] <= 'z')
            lower++;
        else if (sentence[i] == ' ')
            whitesp++;
        else
            continue;
    }
    printf("Upper case letters: %d\n", upper);
    printf("lower case letters: %d\n", lower);
    printf("whitespace: %d\n", whitesp);
    return 0;
}