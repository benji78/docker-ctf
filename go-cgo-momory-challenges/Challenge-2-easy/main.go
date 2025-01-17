package main

import (
	"fmt"
	"os"
	"strconv"
	"unsafe"
)

var secret = "FLAG{Bravo_tu_as_lu_le_secret_en_memoire}"
var sensitiveData = []byte{
	0x42, 0x65, 0x65, 0x70, 0x20, 0x42, 0x6F, 0x6F, // "Beep Boo"
	0x70, 0x21, 0x20, 0x53, 0x65, 0x63, 0x72, 0x65, // "p! Secre"
	0x74, 0x20, 0x64, 0x61, 0x74, 0x61, 0x20, 0x2E, // "t data ."
	0x2E, 0x2E, 0x00, // "...\0"
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: ./vuln <offset>")
		fmt.Println("Ex: ./vuln 0   -> lit sensitiveData[0]")
		os.Exit(1)
	}

	offsetStr := os.Args[1]
	offset, err := strconv.Atoi(offsetStr)
	if err != nil || offset < 0 {
		fmt.Println("Offset invalide")
		os.Exit(1)
	}

	ptr := unsafe.Pointer(&sensitiveData[0])

	vulnPtr := unsafe.Pointer(uintptr(ptr) + uintptr(offset))

	value := *(*byte)(vulnPtr)

	fmt.Printf("[*] Lecture à l'offset %d : 0x%02X ('%c')\n", offset, value, value)
}
