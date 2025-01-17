package main

import (
	"fmt"
	_ "unsafe"
)

type secretStruct struct {
	hiddenValue string
	Visible     string
}

func main() {
	_ = &secretStruct{
		hiddenValue: "CTF{flag_secret_interne}",
		Visible:     "Vous ne verrez que moi en normal",
	}

	fmt.Println("Défi : réussir à lire le champ caché (hiddenValue) sans y avoir accès directement.")

	// use unsafe ou reflect
}
