package main

import (
	"fmt"
	"unsafe"
)

type secretStruct struct {
	hiddenValue string
	Visible     string
}

func main() {
	secret := &secretStruct{
		hiddenValue: "CTF{flag_secret_interne}",
		Visible:     "Vous ne verrez que moi en normal",
	}

	basePtr := unsafe.Pointer(secret)
	offset := unsafe.Offsetof(secret.hiddenValue)
	ptrToHidden := (*string)(unsafe.Pointer(uintptr(basePtr) + offset))

	fmt.Println("Le champ caché est :", *ptrToHidden)
}
