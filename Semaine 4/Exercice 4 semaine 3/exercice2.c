#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Etudiant {
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

struct Etudiant saisieEtudiant() {
    struct Etudiant etu;

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

int saisieListeEtudiant(struct Etudiant *etu[]) {
    int i, nbrEtu;

    printf("Enter the number of students :\n");
    scanf("%d", &nbrEtu);

    *etu = malloc(nbrEtu * sizeof(struct Etudiant));
    if (*etu == NULL) {
        printf("Can't allocate memory");
        exit(0);
    }

    for (i = 0; i < nbrEtu; ++i) {
        printf("------ Students input %d/%d ------\n", i + 1, nbrEtu);
        (*etu)[i] = saisieEtudiant();
    }

    return nbrEtu;
}

void trierParNomListeEtudiant(struct Etudiant *etu[], int nbrEtu) {
    struct Etudiant temp;
    int i, j, cmp;

    for (i = 0; i < nbrEtu - 1; i++) {
        // Pour chaque element de la liste
        // parcours le reste de la liste pour trouver le plus petit restant
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

void trierParMoyListeEtudiant(struct Etudiant *etu[], int nbrEtu) {
    struct Etudiant temp;
    int i, j;

    for (i = 0; i < nbrEtu - 1; i++) {
        for (j = i + 1; j < nbrEtu; j++) {
            if ((*etu)[i].moy > (*etu)[j].moy) {
                temp = (*etu)[i];
                (*etu)[i] = (*etu)[j];
                (*etu)[j] = temp;
            }
        }
    }
}


void afficherListeEtudiant(struct Etudiant *etu[], int nbrEtu) {

    int i;
    printf("Name Surname | Median Final | Average\n");
    for (i = 0; i < nbrEtu; i++)
    {
        printf("%s %s | %f %f | %f\n", (*etu)[i].nom, (*etu)[i].prenom, (*etu)[i].median, (*etu)[i].final, (*etu)[i].moy);
    }
}

int main(int argc, char const *argv[]) {
    struct Etudiant *etu;
    int nbrEtu;

    nbrEtu = saisieListeEtudiant(&etu);
    printf("------------------------\n");
    printf("--------- Input --------\n");
    afficherListeEtudiant(&etu, nbrEtu);

    printf("----- List by Name -----\n");
    trierParNomListeEtudiant(&etu, nbrEtu);
    afficherListeEtudiant(&etu, nbrEtu);

    printf("----- Liste by average (ascending) -----\n");
    trierParMoyListeEtudiant(&etu, nbrEtu);
    afficherListeEtudiant(&etu, nbrEtu);

    return 0;
}