import time
import microcontroller as mc
import aesio
from binascii import hexlify
from ButtonEvents import ButtonEvents
from Menu import Menu
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

be = ButtonEvents()
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

def get_key() :
    """Read button sequence (end with Button_3) and return 16-bytes
    key.

    """
    pw = []
    while True :
        time.sleep(0.05)
        buttons = be.buttons()
        if buttons == 0 : continue
        if buttons & be.K_UP     : pw.append("U")
        if buttons & be.K_DOWN   : pw.append("D")
        if buttons & be.K_LEFT   : pw.append("L")
        if buttons & be.K_RIGHT  : pw.append("R")
        if buttons & be.K_X      : pw.append("X")
        if buttons & be.K_O      : pw.append("A")
        if buttons & be.K_START  : pw.append("B")
        if buttons & be.K_SELECT : break
        print(".", end = "")

    pw = ("".join(pw) + " " * 16)[:16]

    cipher = aesio.AES(mc.cpu.uid, aesio.MODE_ECB)
    key = bytearray(16)
    cipher.encrypt_into(pw, key)

    return key

def gen_key() :
    """Generate key & iv to encrypt password db."""
    
    while be.buttons() : pass		# consume all buttons
    print("\x1b[2J")
    
    while True :
        print("\nEnter your KONAMI command:")
        key0 = get_key()
        print("\nEnter again:")
        key1 = get_key()
        print()
        if key0 == key1 : break
        print("Commands don't match.  Try again.")

    print("\n\n")
    print("key:", hexlify(key0).decode())
    print(" iv:", hexlify(mc.cpu.uid).decode())
    print("""
Prepare password file "vault.py" like
    [ [ "siteA", "passA" ], ...  ]
Encrypt valut.py as 
    openssl enc -aes-128-ctr -e \\ 
      -K <key> -iv <iv> \\
      -in vault.py -out vault.enc
Put valut.enc at "/".

Press any key.
""")
    while be.buttons() == 0 :
        time.sleep(0.1)
    
#------------------------------------------------------------------------

print("\x1b[2J\nEnter your KONAMI command:")
key = get_key()

with open("vault.enc", "rb") as f :
    buf = f.read()

cipher = aesio.AES(key, aesio.MODE_CTR, mc.cpu.uid)
dec = bytearray(len(buf))
cipher.decrypt_into(buf, dec)

try :
    vault = eval(dec)
except SyntaxError :
    print("\nOops! wrong KONAMI command, maybe.")
    time.sleep(1)
    vault = []

title  = [ x[0] for x in vault ]
passwd = [ x[1] for x in vault ]

title.append("")
title.append("Generate key")

idx = 0
while True :
    idx = Menu("Password Vault", title, idx)
    if idx is None: break
    if idx < len(passwd) : layout.write(passwd[idx])
    if idx == len(passwd) + 1 : gen_key()

be.deinit()
