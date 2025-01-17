package main

import (
	"fmt"
)

func main() {
	secretToken := "CTF{SuperSecretToken}"

	// Faute volontaire : on affiche directement l'adresse mémoire
	fmt.Printf("L'adresse mémoire du secretToken est: %p\n", &secretToken)

	// Exécution bloquée pour laisser le temps d'inspecter (si besoin)
	var input string
	fmt.Scanln(&input)
}
