# Straight Up Circular [271 points] (172 solves)
```python
enc = "dvlby_otspnr{cobrnot450i1nm_e03}"

left_pointer = 15
right_pointer = 16
res = ""
while (left_pointer >= 0 and right_pointer <= len(enc)):
    res += enc[left_pointer] + enc[right_pointer]
    left_pointer -= 1
    right_pointer += 1
print(res)
```

flag: `bronco{tr4n5p0sit1on_my_bel0v3d}`