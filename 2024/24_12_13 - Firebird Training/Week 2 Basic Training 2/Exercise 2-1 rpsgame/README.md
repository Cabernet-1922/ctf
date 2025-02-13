# Exercise 2-1 rpsgame [100 points] (51 solves)
```python
from pwn import *
context.log_level = 'CRITICAL'
guess_pool = ["R", "P", "S"]
memory_pool = []

def rps(opponent_):
    if opponent_ == "Scissor":
        return "R"
    elif opponent_ == "Rock":
        return "P"
    else:
        return "S"


start = time.time()
for i in range(40):
    p = remote('chal.firebird.sh', 35005)
    p.recvuntil(b'> ')
    if not memory_pool:
        p.sendline(random.choice(guess_pool).encode())
    else:
        for j in range(i):
            p.sendline(memory_pool[j].encode())
            p.recvuntil(b'> ')
        p.sendline(random.choice(guess_pool).encode())
    opponent = p.recvline_startswith(b"Computer chosen: ").strip(b"Computer chosen: ").strip().decode()
    memory_pool.append(rps(opponent))
    p.close()

p = remote('chal.firebird.sh', 35005)
for i in range(40):
    p.recvuntil(b'> ')
    p.sendline(memory_pool[i].encode())
print(p.recvline_startswith(b"Congrats!"))
print("Time Spend: ",time.time() - start)
```