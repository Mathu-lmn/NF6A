#include <stdio.h>
#include <string.h>

void main() {
    char *text = "France is a European country.$ It is part of the European Union.$ It is a member of the United Nations.$";
    char text2[500] = {};
    char final[50][50] = {};
    char $[3];
    char temp[500];
    int i,j,l,t,r = 0;
    l = strlen(text);
    for (i = 0; i < l; i++) {
        if (text[i] == '$') {
            $[r] = i;
            r++;
        }
    }
    j = $[0];
    strncpy(final[0],text,j);
    strncpy(final[1],text + j + 2, $[1] - j - 2);
    strncpy(final[2],text + $[1] + 2, l - $[1]- 3);
    for (i = 0; i < 3; i++)
        printf("%s\n",final[i]);

    //Sorting
    for(int j = 0; j < 2; j++){
    if(strcmp(final[j], final[j+1]) > 0){
        strcpy(temp, final[j]);
        strcpy(final[j], final[j+1]);
        strcpy(final[j+1], temp);
    }
    }
}