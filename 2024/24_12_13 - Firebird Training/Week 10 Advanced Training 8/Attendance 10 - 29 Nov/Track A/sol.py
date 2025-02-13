import z3

f = open('enc_10a.txt', 'r').readlines()
for i in range(len(f)):
    f[i] = int(f[i])

n = z3.Int('n')
c = [] # symbolic representation of flag
for i in range(len(f)):
    c.append(z3.Int(f'c{i}'))

s = z3.Solver()
for c1, c2, k in zip(c, c[1:], range(len(f))):
    s.add((c1 * 2 - c2 * 4 + n + k) * (n + k) == f[k])

for i in c:
    s.add(i >= 0, i <= 127)

s.add(c[0] == ord('f'))
s.add(c[1] == ord('l'))

if s.check() == z3.sat:
    m = s.model()
    for i in c:
        print(chr(int(str(m[i]))), end='')