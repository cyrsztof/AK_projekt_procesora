#AK projekt procesora stałoprzecinkowego
## Dokumentacja
### Sładnia
`etykieta: INSTRUKCJE   ; komentarze`
### Liczby
```
Szesnaskowo: 0xAF
Dziesiętnie: 123
Ósemkowo: 0o76
Binarnie: 0b101
```
### Stałe znakowe
```
Znak: 'X'
String: "I'm string"
```
### Rejestry
```
Użycie: Rx
Ogólnego przeznaczenia: R0, R1, R2, R3, R4, R5, R6, R7
Stosu: SP
Instrukcji: IP
```
### Adresy
```
Adres z etykiety: label
```
### Rozkazy procesora
#### Ładowanie stałych
```
DB stała
```
#### Kopiowanie wartości
##### Rejestr -> rejestr
```
MOV rejestr, rejestr
```
##### Stała -> rejestr
```
SET stala, rejestr
```
##### Pamięć -> rejestr
```
LD rejestr, rejestr
```
##### Rejestr -> pamięć
```
ST rejestr, rejestr
```
#### Instrukcje arytmetyczne
##### Suma
```
ADD rejestr, rejestr
```
##### Różnica
```
SUB rejestr, rejestr
```
##### Iloczyn
```
MUL rejestr, rejestr
```
##### Iloraz
```
DIV rejestr, rejestr
```
##### Modulo
```
MOD rejestr, rejestr
```
##### Inkrementacja
```
INC rejestr
```
##### Dekrementacja
```
DEC rejestr
```

#### Instrukcje logiczne
##### Alternatywa
```
OR rejestr, rejestr
```
##### Koniunkcja
```
AND rejestr, rejestr
```
##### Alternatywa wykluczająca
```
XOR rejestr, rejestr
```
##### Zaprzeczenie
```
NOT rejestr
```
##### Przesunięcie bitowe w prawo
```
SHR rejestr, rejestr
```
##### Przesunięcie bitowe w lewo
```
SHL rejestr, rejestr
```
#### Porównanie
```
CMP rejestr, rejestr
```
#### Skoki
##### Warunkowe
```
JC adres
JNC adres
JZ adres
JNZ adres
JA adres
JNA adres
JB adres
JNB adres
JE adres
JNE adres
```
##### Bezwarunkowy
```
JMP adres
```
#### Funkcje
##### Wywołanie
```
CALL adres
```
##### Powrót
```
RET
```
#### Operacje na stosie
##### Wkładanie
```
PUSH rejestr
```
##### Zdejmowanie
```
POP rejestr
```
#### Kończenie pracy
```
END
```
