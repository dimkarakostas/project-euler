inp_nums = []
with open('input_13', 'r') as f:
    for num in f.readlines():
        inp_nums.append(int(num.strip()))

i = 0
for n in inp_nums:
    i += n

print str(i)[0:10]
