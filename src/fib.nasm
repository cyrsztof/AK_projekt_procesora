%include "macros.nasm"

%define zero '0'
%define newline 10

    JMP start

print_num:
    POP R1              ; pobranie agrumentu funkcji
    POP R0
    PUSH R1

    SET 10, R1          ; podstawa = 10
    SET zero, R2
    SET 0, R3
    SET 3, R4
l:
    MOV R0, R7
    MOD R1, R7
    ADD R2, R7
    PUSH R7
    DIV R1, R0

    DEC R4
    CMP R3, R4
    JNZ l

    POP R7
    OUT R7
    POP R7
    OUT R7
    POP R7
    OUT R7

    RET

fib:
    RET

start:
    ;SET 12, R0
    ;PUSH R0
    ;CALL print_num
    CALL fib

    END

