%include "macros.nasm"

    SET zero, R0

    MOV R0, R1
    LD R1, R1
    OUT R1

    INC R0

    MOV R0, R1
    LD R1, R1
    OUT R1

    END

zero:
    DB "01"

