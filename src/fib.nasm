%include "macros.nasm"

;    vset 5, r0
;    vset 0, r1
;
;    vset 1, r7
;    vset 0, r6
;
;l:
;    vset zero, r3
;    vld r3, r4
;    vadd r6, r7
;    vadd r7, r4
;    voutb r4
;
;    vset enter, r3
;    vld r3, r4
;    voutb r4
;
;    vset zero, r3
;    vld r3, r4
;    vadd r7, r6
;    vadd r6, r4
;    voutb r4
;
;    vset enter, r3
;    vld r3, r4
;    voutb r4
;
;
;e:
;    voff
;
;enter:
;    db 10
;
;zero:
;    db '0'




    ;vset 120, r0
    ;vset 10, r2
    ;vset '0', r3


    ;vmov r0, r1
    ;vmod r2, r1
    ;vpush r1
    ;vdiv r2, r0

    ;vmov r0, r1
    ;vmod r2, r1
    ;vpush r1
    ;vdiv r2, r0

    ;vmov r0, r1
    ;vmod r2, r1
    ;vpush r1

    ;vpop r1
    ;vadd r3, r1
    ;voutb r1
    ;vpop r1
    ;vadd r3, r1
    ;voutb r1
    ;vpop r1
    ;vadd r3, r1
    ;voutb r1


    SET 4, r1
    OFF

