#!/usr/bin/python
#
# quick installer for SET
#
#
import subprocess
import os
print("[*] Installing requirements.txt...")
subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
print("[*] Finished.")
