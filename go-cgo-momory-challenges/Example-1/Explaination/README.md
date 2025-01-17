# README – Exemple n°1 : Fuite d’adresse mémoire (Leak)

Cet exemple illustre à quel point il est facile de **faire fuiter une adresse mémoire** ou un secret dans un programme Go lorsque l’on utilise des logs ou des impressions directes (ex: `fmt.Printf`).

---

## 1. Structure du projet

- **main.go**  
  Contient un code très simple qui :
    1. Stocke un secret `secretToken` dans une variable locale.
    2. Imprime l’adresse mémoire de cette variable (exemple : `fmt.Printf("L'adresse du token : %p\n", &secretToken)`).
    3. Invite l’utilisateur à appuyer sur Entrée, permettant de garder le programme en vie pour analyser le fonctionnement.

---

## 2. Exemple de code

<details>
<summary>Cliquez pour afficher <code>main.go</code></summary>

```go
package main

import (
    "fmt"
)

func main() {
    secretToken := "CTF{SuperSecretToken}"

    fmt.Printf("L'adresse mémoire du secretToken est: %p\n", &secretToken)
    fmt.Println("Quelqu'un a laissé traîner une info sensible...")

    // On attend que l'utilisateur tape Entrée
    var input string
    fmt.Scanln(&input)
}
