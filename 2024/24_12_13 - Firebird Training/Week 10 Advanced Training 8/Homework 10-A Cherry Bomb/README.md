# Homework 10-A Cherry Bomb [100 points] (3 solves)
```python
from pwn import *
from z3 import *
import re

def get_server_output():
    r = remote('chal.firebird.sh', 35055, level='error')
    data = r.recvuntil(b"encouragement!").decode()
    recipe_data = data.split('\n')
    stamina = int(re.search(r"(\d+)%", recipe_data[0]).group(1))
    steps = []
    for line in recipe_data:
        if ": Add " in line or "Knead" in line:
            num = re.findall(r'\d+', line)
            if len(num) > 1:
                steps.append(int(num[1]))
    r.close()
    return stamina, steps[:128]

def collect_recipes(num_samples=25):
    recipes = {}
    while len(recipes) < num_samples:
        stamina, steps = get_server_output()
        if stamina and steps and len(steps) == 128:
            if stamina not in recipes:
                recipes[stamina] = steps
                print(f"[+] Recipe {len(recipes)}/{num_samples} (stamina: {stamina})")
        time.sleep(0.5)
    return recipes

def solve_equations(recipes):
    s = Solver()
    chars = [BitVec(f'x{i}', 8) for i in range(228)]
    xored = [BitVec(f'xor{i}', 8) for i in range(227)]

    for i in range(227):
        s.add(xored[i] == chars[i] ^ chars[i + 1])

    for stamina, steps in recipes.items():
        offset = stamina - 100
        for i, step in enumerate(steps):
            if offset + i + 1 < 227:
                s.add(xored[offset + i] + xored[offset + i + 1] == step - stamina)

    for char in chars:
        s.add(And(char >= 32, char <= 126))

    if s.check() == sat:
        return [s.model().eval(char).as_long() for char in chars]
    return None

def main():
    recipes = collect_recipes()
    solution = solve_equations(recipes)
    if solution:
        message = ''.join(chr(x) for x in solution)
        r = remote('chal.firebird.sh', 35055, level='error')
        r.recvuntil(b"encouragement!")
        r.sendline(message.encode())
        print("\n[+] Server response:", r.recvall().decode())
        r.close()

if __name__ == "__main__":
    main()
```