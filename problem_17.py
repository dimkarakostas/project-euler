digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dg = [len(i) for i in digits]

teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
te = [len(i) for i in teen]

decs = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
dc = [len(i) for i in decs]

thou = len('thousand')
hun = len('hundred')
an = len('and')

total = 0
for num in range(1, 1001):
    t = num/1000
    num -= t*1000
    h = num/100
    num -= h*100
    d = num/10
    num -= d*10
    if t:
        total += dg[t] + thou
    if h:
        total += dg[h] + hun
        if d or num:
            total += an
    if d != 1:
        total += dc[d] + dg[num]
    else:
        total += te[num]
print total
