# README – Démonstration d’un Buffer Overflow avec Go + CGO

Ce projet illustre comment un simple **buffer overflow** (débordement de mémoire) peut réintroduire une vulnérabilité dans un programme Go lorsque l’on utilise du code C non sécurisé via **CGO**.

Nous allons montrer qu’en **dépassant la capacité d’un buffer** de 16 octets, on peut **corrompre** une variable `isAdmin`, prouvant la faille de sécurité.

---

## 1. Structure du projet

- **main.go**  
  Contient le code Go et le code C intégré via CGO. On y déclare :
    1. Une structure globale `gData` avec un **buffer** de 16 octets (`buffer[16]`).
    2. Une variable `int isAdmin` placée **juste après** ce buffer.
    3. Une fonction vulnérable `insecureCopy` qui fait un simple `strcpy` (sans vérifier la taille) dans `gData.buffer`.
    4. Une fonction `getIsAdmin` pour récupérer la valeur de `gData.isAdmin`.

Ce positionnement en mémoire permet qu’un débordement au-delà des 16 octets de `buffer` **écrase la variable** `isAdmin`.

---

## 2. Code source (main.go)

```go
package main

/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// On définit une structure globale qui contient le buffer et la variable isAdmin
struct {
    char buffer[16];
    int isAdmin;
} gData;

// Fonction vulnérable
void insecureCopy(char *input) {
    // Copie sans vérification dans gData.buffer (16 octets)
    strcpy(gData.buffer, input);
    printf("buffer = %s\n", gData.buffer);
}

// Renvoie la valeur actuelle de gData.isAdmin
int getIsAdmin() {
    return gData.isAdmin;
}
*/
import "C"
import (
    "fmt"
    "os"
    "unsafe"
)

func main() {
    if len(os.Args) < 2 {
        fmt.Printf("Usage: %s <payload>\n", os.Args[0])
        return
    }

    // Récupère la chaîne d'entrée
    payload := os.Args[1]

    // Convertit la string Go en *C.char
    cPayload := C.CString(payload)
    defer C.free(unsafe.Pointer(cPayload))

    // Appel de la fonction vulnérable
    C.insecureCopy(cPayload)

    // Vérifie la valeur de isAdmin après la copie
    adminValue := int(C.getIsAdmin())
    if adminValue == 1 {
        fmt.Println("Félicitations, vous êtes devenu admin grâce à la corruption mémoire !")
    } else {
        fmt.Printf("isAdmin = %d\n", adminValue)
    }
}
