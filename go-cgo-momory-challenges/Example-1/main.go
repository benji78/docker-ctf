package main

import (
	"fmt"
)

func main() {
	secretToken := "CTF{SuperSecretToken}"
	fmt.Printf("L'adresse mémoire du secretToken est: %p\n", &secretToken)

	var input string
	fmt.Scanln(&input)
}
