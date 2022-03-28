#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    char *nom;
    char *prenom;
    float median;
    float final;
    float moy;
};

void saisiePhrase(char *chaine[], int tailleMax) {

    char *chaineTmp = NULL;
    char c;
    int n = 0;

    chaineTmp = malloc(tailleMax * sizeof(char));
    if (chaineTmp == NULL) {
        printf("Impossible d'allouer de la mémoire");
        exit(0);
    }

    do {
        scanf("%c", &c);
        if (c != '\n' || n != 0) {
            chaineTmp[n] = c;
            n++;
        }
        else {
            c = 0;
        }
    } while (c != '\n' && n < tailleMax);

    n--;
    chaineTmp[n] = 0;

    *chaine = malloc(n * sizeof(char));
    if (*chaine == NULL) {
        printf("Can't allocate memory");
        exit(0);
    }

    strcpy(*chaine, chaineTmp);
    free(chaineTmp);
}

struct Student StudentAssign() {
    struct Student etu;

    printf("Student's Surname :\n");
    saisiePhrase(&etu.prenom, 255);

    printf("Student's Name :\n");
    saisiePhrase(&etu.nom, 255);

    printf("Medians Grade :\n");
    scanf("%f", &etu.median);

    printf("Finals Grade :\n");
    scanf("%f", &etu.final);

    etu.moy = 0.4 * etu.median + 0.6 * etu.final;
    printf("Average grade : %f\n", etu.moy);

    return etu;
}

int StudentListIput(struct Student *etu[]) {
    int i, nbrEtu;

    printf("Enter the number of students :\n");
    scanf("%d", &nbrEtu);

    *etu = malloc(nbrEtu * sizeof(struct Student));

    for (i = 0; i < nbrEtu; ++i) {
        printf("------ Students input %d/%d ------\n", i + 1, nbrEtu);
        (*etu)[i] = StudentAssign();
    }

    return nbrEtu;
}


void printStudentList(struct Student *etu[], int nbrEtu) {

    int i;
    printf("Name Surname | Median Final | Average\n\n");
    for (i = 0; i < nbrEtu; i++)
    {
        printf("%s %s | %f %f | %f\n", (*etu)[i].nom, (*etu)[i].prenom, (*etu)[i].median, (*etu)[i].final, (*etu)[i].moy);
    }
}

void sortByName(struct Student *etu[], int nbrEtu) {
    struct Student temp;
    int i, j, cmp;

    for (i = 0; i < nbrEtu - 1; i++) {
        for (j = i + 1; j < nbrEtu; j++) {
            /// Comparaison des noms
            cmp = strcmp((*etu)[i].nom, (*etu)[j].nom);
            // Si les noms sont identiques, comparaison des prénoms
            if (cmp == 0) {
                cmp = strcmp((*etu)[i].prenom, (*etu)[j].prenom);
            }

            if (cmp > 0) {
                temp = (*etu)[i];
                (*etu)[i] = (*etu)[j];
                (*etu)[j] = temp;
            }
        }
    }
}

void sortByAverage(struct Student *etu[], int nbrEtu) {
    struct Student temp;
    int i, j;

    for (i = 0; i < nbrEtu - 1; i++) {
        for (j = i + 1; j < nbrEtu; j++) {
            if ((*etu)[i].moy < (*etu)[j].moy) {
                temp = (*etu)[i];
                (*etu)[i] = (*etu)[j];
                (*etu)[j] = temp;
            }
        }
    }
}

int main() {
    struct Student *etu;
    int nbrEtu;
    
    nbrEtu = StudentListIput(&etu);
    printf("------------------------\n");
    printf("--------- Input --------\n");
    printStudentList(&etu, nbrEtu);

    printf("\n------------------------\n");
    printf("---- Sorted by name ----\n");
    sortByName(&etu, nbrEtu);
    printStudentList(&etu, nbrEtu);

    printf("\n------------------------\n");
    printf("Grade by descending order \n");
    sortByAverage(&etu, nbrEtu);
    printStudentList(&etu, nbrEtu);
}