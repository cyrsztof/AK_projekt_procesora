fname = 'hello'
fname2 = fname + '2'

with open(fname, 'rb') as f:
    nasm = f.read()

with open(fname, 'rb') as f:
    asm = f.read()

for i, v in enumerate(zip(nasm, asm)):
    if v[0] != v[1]:
        print(i, v, [hex(i) for i in v])
