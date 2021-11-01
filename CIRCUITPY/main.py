import sys
import os
import supervisor
import gc
from Menu import Menu

# Turn off RTL8720 to save energy
#
import wio_terminal_rtl

files = [ name[:-3] for name in os.listdir()
          if name.endswith('.py') and name not in ('main.py', 'boot.py') ]
files.sort()

idx = Menu("Python Launcher", files)
print("\x1b[2J")
if idx is None : sys.exit()

module = files[idx]
del files
gc.collect()
__import__(module)
supervisor.reload()
