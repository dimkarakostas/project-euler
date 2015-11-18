ADJ = 13

with open('input_8', 'r') as f:
    inp = f.read()

i = 0
mx = 0
while i + ADJ < len(inp) - 1:
    tst = inp[i:i+ADJ]
    outp = 1
    for j in tst:
        outp *= int(j)
    if outp > mx:
        mx = outp
    i += 1
print mx
