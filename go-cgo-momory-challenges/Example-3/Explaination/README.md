# README – Exemple n°3 : Exploitation de la mémoire Go avec `unsafe` et `reflect`

Dans ce défi, vous allez apprendre à **contourner l’encapsulation** en Go et à **manipuler directement la mémoire** à l’aide du package [**`unsafe`**](https://pkg.go.dev/unsafe).  
L’objectif : **lire un champ privé** (non exporté) d’une structure, qui devrait normalement être inaccessible si l’on respecte les règles du langage Go.

---

## 1. Structure du projet

- **main.go**  
  Contient une structure `secretStruct` avec un champ privé `hiddenValue` (en minuscule) et un champ exporté `Visible`.
    - La variable `secret` de type `*secretStruct` stocke une donnée sensible dans `hiddenValue`.
    - Aucune fonction « officielle » ne permet d’y accéder.
    - **But du défi** : réussir à lire `hiddenValue` sans passer par un getter, **grâce** à la manipulation de la mémoire via `unsafe.Pointer`.

---

## 2. Code source (exemple)

<details>
<summary>Cliquez pour afficher <code>main.go</code></summary>

```go
package main

import (
    "fmt"
    "unsafe"
)

// Structure avec un champ privé
type secretStruct struct {
    hiddenValue string
    Visible     string
}

func main() {
    // Création d'un objet qui contient la donnée sensible
    secret := &secretStruct{
        hiddenValue: "CTF{Flag_Tres_Secret}",
        Visible:     "Je suis public",
    }

    // Indication pour le joueur
    fmt.Println("Défi : réussir à lire le champ caché (hiddenValue) sans y avoir accès directement.")
    fmt.Println("Indice : regardez du côté de `unsafe` ou `reflect` pour contourner l'encapsulation.")

    // On bloque l'exécution pour permettre l'analyse
    var pause string
    fmt.Scanln(&pause)
}
