#!/usr/bin/python3

from pwn import *
import misc.coloredstatus as cs
from time import sleep
import os

def prep(search):
    return "DISPLAY=:0 && export DISPLAY && nohup firefox -new-tab https://www.google.com.sg/#q=" + search.replace(" ", "+") + " &"

def execute(session, configs, params):
    if params == None:
        print(cs.status, "Usage: search [string]")
        return 1 

    try:
        shell = session.shell("/bin/bash")
        shell.sendline(prep(params))
        output = str(shell.recvrepeat(0.2), "UTF-8")
        shell.close()
        return 0
    except:
        return 2
