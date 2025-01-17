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
	fmt.Printf("Nom : %s, Age : %d\n", u.Name, u.Age)
}

func main() {
	fmt.Println("Bienvenue dans le défi Null pointer / Panic!")

	if len(os.Args) > 1 && os.Args[1] == "panic" {
		riskyFunction(nil)
	} else {
		u := &User{Name: "Alice", Age: 42}
		riskyFunction(u)
	}
}
