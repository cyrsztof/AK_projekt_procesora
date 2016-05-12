%define R0 0
%define R1 1
%define R2 2
%define R3 3
%define R4 4
%define R5 5
%define R6 6
%define R7 7

%macro MOV 2
db 0x00, %1, %2
%endmacro

%macro SET 2
db 0x01, %1, %2
%endmacro

%macro LD 2
db 0x02, %1, %2
%endmacro

%macro ST 2
db 0x03, %1, %2
%endmacro


%macro ADD 2
db 0x10, %1, %2
%endmacro

%macro SUB 2
db 0x11, %1, %2
%endmacro

%macro MUL 2
db 0x12, %1, %2
%endmacro

%macro DIV 2
db 0x13, %1, %2
%endmacro

%macro MOD 2
db 0x14, %1, %2
%endmacro

%macro INC 1
db 0x15, %1
%endmacro

%macro DEC 1
db 0x16, %1
%endmacro


%macro OR 2
db 0x20, %1, %2
%endmacro

%macro AND 2
db 0x21, %1, %2
%endmacro

%macro XOR 2
db 0x22, %1, %2
%endmacro

%macro NOT 1
db 0x23, %1
%endmacro

%macro SHL 2
db 0x24, %1, %2
%endmacro

%macro SHR 2
db 0x25, %1, %2
%endmacro


%macro CMP 2
db 0x30, %1, %2
%endmacro

%macro JC 1
db 0x31, %1
%endmacro

%macro JNC 1
db 0x32, %1
%endmacro

%macro JZ 1
db 0x33, %1
%endmacro

%macro JNZ 1
db 0x34, %1
%endmacro

%macro JA 1
db 0x35, %1
%endmacro

%macro JNA 1
db 0x36, %1
%endmacro

%macro JB 1
db 0x37, %1
%endmacro

%macro JNB 1
db 0x38, %1
%endmacro

%macro JE 1
db 0x39, %1
%endmacro

%macro JNE 1
db 0x3a, %1
%endmacro

%macro JMP 1
db 0x3b, %1
%endmacro

%macro JMPR 1
db 0x3c, %1
%endmacro


%macro PUSH 1
db 0x40, %1
%endmacro

%macro POP 1
db 0x41, %1
%endmacro


%macro CALL 1
db 0x50, %1
%endmacro

%macro CALLR 1
db 0x51, %1
%endmacro

%macro RET 0
db 0x52
%endmacro


%macro OUT 1
db 0xf0, %1
%endmacro

%macro IN 2
db 0xf1, %2, %1
%endmacro

%macro END 0
db 0xff
%endmacro
