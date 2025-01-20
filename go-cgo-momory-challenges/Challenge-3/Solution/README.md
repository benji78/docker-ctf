# Challenge Go - Exploitation Mémoire & Reverse Engineering

Ce dépôt contient un défi pédagogique en Go (Golang) conçu pour un exercice de **reverse engineering** et d’**exploitation mémoire** de type CTF / Root-Me.

## Sommaire
1. [Présentation](#présentation)
2. [Architecture du Code](#architecture-du-code)
3. [Compilation](#compilation)
4. [Utilisation](#utilisation)
5. [Principe du XOR pour le Mot de Passe](#principe-du-xor-pour-le-mot-de-passe)
6. [Fonction Cachée & Appel par Adresse](#fonction-cachée--appel-par-adresse)
7. [Désassemblage & Découverte](#désassemblage--découverte)
8. [Notes sur l'ASLR](#notes-sur-laslr)
9. [Conclusion](#conclusion)

---

## Présentation

Ce challenge illustre :
- L’utilisation d’un mot de passe XORé pour un premier niveau de protection.
- La présence d’une fonction secrète non appelée directement, qu’il faut invoquer via son **adresse en mémoire**.
- Le besoin de faire du *reverse engineering* sur un binaire Go afin de retrouver le mot de passe caché et l’adresse de la fonction secrète.

**Objectif :**
1. Découvrir le mot de passe XORé.
2. Appeler la fonction cachée pour afficher un message secret (flag).

---

## Architecture du Code

Le fichier principal est **`challenge.go`**. Il contient :

- **`var xorKey byte`** : clé XOR pour encoder/décoder le mot de passe.
- **`var encodedPass []byte`** : tableau d’octets représentant le mot de passe XORé.
- **`var secretData string`** : chaîne hexadécimale du message final.
- **`func secretAdminAccess()`** : la fonction “cachée” qui révèle le flag.
- **`func main()`** : la fonction principale qui gère :
    1. La lecture du mot de passe via `os.Args`.
    2. La comparaison avec la version décodée de `encodedPass`.
    3. L’appel optionnel de la fonction à une adresse spécifiée (si le mot de passe est correct).

---

## Compilation

Assurez-vous d’avoir Go (version ≥ 1.18 recommandée).

```bash
go build -o challenge challenge.go
