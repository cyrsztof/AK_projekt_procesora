%include "macros.nasm"

    JMP start

foo:
    POP R3
    POP R2
    PUSH R3

    SET 0, R0
    SET 1, R1
l:
    MOV R2, R3
    LD R3, R3

    CMP R3, R0
    JZ r

    OUT R3

    INC R2
    JMP l
r:
    RET

start:
    SET hello, R2
    PUSH R2
    CALL foo

    SET world, R2
    PUSH R2
    CALL foo

    END

hello:
    DB "Hello!"
    DB 0

world:
    DB " World!"
    DB 0
