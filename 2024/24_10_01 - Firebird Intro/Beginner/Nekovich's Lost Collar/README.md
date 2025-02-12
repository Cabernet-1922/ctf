# Nekovich's Lost Collar [150 points] (13 solves)

```python
def verify(number):
    # Convert number to list of digits
    digits = [int(d) for d in str(number)]
    if len(digits) != 6 or 0 in digits:
        return False

    w = x = y = z = 0

    # First digit
    w = digits[0]
    x = (z % 26) - 13
    z //= 26
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25 * x + 1
    z *= y
    y = (w + 15) * x
    z += y

    # Second digit
    w = digits[1]
    x = (z % 26) + 10
    z //= 1
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25 * x + 1
    z *= y
    y = (w + 7) * x
    z += y

    # Third digit
    w = digits[2]
    x = (z % 26) + 0
    z //= 26
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25 * x + 1
    z *= y
    y = (w + 2) * x
    z += y

    # Fourth digit
    w = digits[3]
    x = (z % 26) - 11
    z //= 26
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25 * x + 1
    z *= y
    y = (w + 13) * x
    z += y

    # Fifth digit
    w = digits[4]
    x = (z % 26) - 11
    z //= 26
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25 * x + 1
    z *= y
    y = (w + 9) * x
    z += y

    # Sixth digit
    w = digits[5]
    x = (z % 26) - 13
    z //= 26
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25 * x + 1
    z *= y
    y = (w + 14) * x
    z += y

    return z == 0


# Test all valid 6-digit numbers
min_code = float('inf')
max_code = 0

for i in range(100000, 999999):
    if '0' not in str(i) and verify(i):
        min_code = min(min_code, i)
        max_code = max(max_code, i)

print(min_code, max_code)
Frequency = (min_code * max_code) ** 2
print(Frequency)
```