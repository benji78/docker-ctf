package main

import (
	"encoding/hex"
	"fmt"
	"os"
	"reflect"
	"strconv"
	"unsafe"
)

var secretData = "3058357e412f48696464656e5f52657375745f3f"

var secretFuncPtr uintptr

func init() {
	secretFuncPtr = reflect.ValueOf(secretAdminAccess).Pointer()
}

var xorKey byte = 0x3A
var encodedPass = []byte{0x54, 0x52, 0x49, 0x4F, 0x0D, 0x5F} // "SECRET" ^ 0x3A

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: ./challenge <password> [optional_memory_address]")
		return
	}

	userInput := os.Args[1]

	decodedPass := make([]byte, len(encodedPass))
	for i, b := range encodedPass {
		decodedPass[i] = b ^ xorKey
	}

	if userInput == string(decodedPass) {
		fmt.Println("Bravo, mot de passe correct !")
		fmt.Println("Mais ce n'est pas la fin du défi...")
	} else {
		fmt.Println("Mot de passe incorrect.")
		return
	}

	if len(os.Args) == 3 {
		addrStr := os.Args[2]

		addr, err := strconv.ParseUint(addrStr, 0, 64)
		if err != nil {
			fmt.Println("Adresse invalide. Utilisez un format hexadécimal, ex: 0x1053530")
			return
		}

		callSecret(addr)
	}
}

func secretAdminAccess() {
	dec, _ := hex.DecodeString(secretData)
	fmt.Println("Félicitations, vous avez contourné la protection !")
	fmt.Println("Voici le secret final :", string(dec))
}

func callSecret(addrUint uint64) {
	f := *(*func())(unsafe.Pointer(&addrUint))
	f()
}
