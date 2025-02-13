import angr

p = angr.Project('xorsssssssss')
state = p.factory.entry_state()
simgr = p.factory.simgr(state)
simgr.explore(find=0x101f83-0x100000+0x400000, avoid=0x101f94-0x100000+0x400000)
print(simgr.found[0].posix.dumps(0).decode())