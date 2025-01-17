# README – Exemple n°2 : Null Pointer / Panic

Cet exemple montre à quel point il est facile de provoquer un **panic** en Go lorsque l’on manipule des **pointeurs `nil`** sans précaution.  
Vous allez voir qu’un simple appel de fonction avec un argument nul peut faire planter le programme si le code ne vérifie pas la validité du pointeur.

---

## 1. Description du programme

Dans le fichier `main.go`, nous avons :

1. Une structure `User` (avec des champs `Name` et `Age`).
2. Une fonction `riskyFunction(u *User)` qui accède directement aux champs de `u`.
3. Une logique dans `main()` qui, selon l’argument passé en ligne de commande, appelle `riskyFunction(nil)` ou crée un `User` valide.

Extrait de code :

```go
package main

import (
    "fmt"
    "os"
)

type User struct {
    Name string
    Age  int
}

func riskyFunction(u *User) {
    // Pas de vérification : si 'u' est nil, on provoque un panic
    fmt.Printf("Nom : %s, Age : %d\n", u.Name, u.Age)
}

func main() {
    fmt.Println("Bienvenue dans le défi Null pointer / Panic!")

    // Si l'argument est "panic", on passe nil à la fonction
    if len(os.Args) > 1 && os.Args[1] == "panic" {
        riskyFunction(nil)  // risque de panic
    } else {
        u := &User{Name: "Alice", Age: 42}
        riskyFunction(u)
    }
}
