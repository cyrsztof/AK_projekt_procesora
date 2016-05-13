%include "macros.nasm"

%define zero '0'
%define newline 10

    JMP start

print_num:
    POP R1              ; pobranie agrumentu funkcji
    POP R0
    PUSH R1

    PUSH R2
    PUSH R3
    PUSH R4
    PUSH R5

    SET 10, R1          ; podstawa = 10
    SET zero, R2
    SET 0, R3
    SET 3, R4
pl:
    MOV R0, R5
    MOD R1, R5
    ADD R2, R5
    PUSH R5
    DIV R1, R0

    DEC R4
    CMP R3, R4
    JNZ pl

    POP R5
    OUT R5
    POP R5
    OUT R5
    POP R5
    OUT R5

    POP R5
    POP R4
    POP R3
    POP R2

    RET

fib:
    PUSH R2
    PUSH R3
    PUSH R4
    PUSH R5
    PUSH R6

    SET 0, R2
    SET 1, R3
    SET 13, R4
    SET 0, R5
fl:
    MOV R2, R6
    ADD R3, R2
    MOV R6, R3

    PUSH R2
    CALL print_num

    SET newline, R6
    OUT R6

    DEC R4
    CMP R5, R4
    JNZ fl
fr:
    POP R6
    POP R5
    POP R4
    POP R3
    POP R2

    RET

start:
    CALL fib

    END

