import time
import board
import displayio as dpio
from KanjiTerminal import KanjiTerminal, han2zen
from ButtonEvents import ButtonEvents
from wifi_connect import wifi_connect
from wio_terminal_rtl.WiFiClientSecure import WiFiClientSecure

def get_weather() :
    c = WiFiClientSecure()
    c.rootCA = b"""-----BEGIN CERTIFICATE-----
MIIEcjCCA1qgAwIBAgIJErmw+nLg2EjGMA0GCSqGSIb3DQEBCwUAMFAxCzAJBgNV
BAYTAkpQMRgwFgYDVQQKEw9TRUNPTSBUcnVzdC5uZXQxJzAlBgNVBAsTHlNlY3Vy
aXR5IENvbW11bmljYXRpb24gUm9vdENBMTAeFw0xNTAzMjQwMjIyMzVaFw0yMzA5
MjkwMjIyMzVaMF0xCzAJBgNVBAYTAkpQMSUwIwYDVQQKExxTRUNPTSBUcnVzdCBT
eXN0ZW1zIENPLixMVEQuMScwJQYDVQQLEx5TZWN1cml0eSBDb21tdW5pY2F0aW9u
IFJvb3RDQTIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDQFTlSsVKz
usVZgsRdUq46Q2WAS8fylrzbNpfWpmSMqF7w4woc99+XPUuu9l3sIbVBq825fnaf
vvk+NjSgO8H2MRFFdJM9V4DF+YmZyuWratS12kGQEMHW1kKJwr/0OBKVTFQF9zbk
RYN7FGXW3AxN0d5+DKs7xBW+OlamWm92aVKpernI62qaXVLQLQprNRYJEITQaso6
BgA3R+R+V08/i+tnuIiqxb5TVbKRxH25sIUZBngu22Ea+oX1SpGh5xbVjqI535S4
cB8oP4v8QF5jgzyDKhqZa8/eWWo7/G8W1x/9ShDrToIWOqwnDFPxrdUksGsDUMEt
PBbdRDQnGnX7AgMBAAGjggFAMIIBPDAdBgNVHQ4EFgQUCoWpd2UFmHxAgfgPlyw4
8QrsPM8wHwYDVR0jBBgwFoAUoHNJmWjchVtl45soL1efvTO8B0gwDwYDVR0TAQH/
BAUwAwEB/zAOBgNVHQ8BAf8EBAMCAQYwSQYDVR0fBEIwQDA+oDygOoY4aHR0cDov
L3JlcG9zaXRvcnkuc2Vjb210cnVzdC5uZXQvU0MtUm9vdDEvU0NSb290MUNSTC5j
cmwwTAYDVR0gBEUwQzBBBgRVHSAAMDkwNwYIKwYBBQUHAgEWK2h0dHBzOi8vcmVw
b3NpdG9yeS5zZWNvbXRydXN0Lm5ldC9TQy1Sb290MS8wQAYIKwYBBQUHAQEENDAy
MDAGCCsGAQUFBzABhiRodHRwOi8vc2Nyb290Y2ExLm9jc3Auc2Vjb210cnVzdC5u
ZXQwDQYJKoZIhvcNAQELBQADggEBAA34p8Of912y2te2PGmyl5bSupbH4F1YLIph
OvTSG3tL6kbndcWWBVM27b7dFD0pTIunUSzBhflsWOiBJQ8aEcmGHUg7V6k52kG7
vSoD6gow2aXUHwgVxbWt65vpli5BjiF+WOhUNAtKGc0F6k+wQfHSuNjMD4NdaPxa
rkF28wfSg+S+0rL9bbr33V5Mzee9aDHT9TpxmCsmYLmfWc+5KV3wL1Tp85uSyaA7
u5ZuCjxerxj3qS1rM46bcEfjopnaD7hnJXSYiL1d0yw5zSW2PEe+LHdoIAb2I6D8
8UFJH0Cli6sY5l8jhjkOOs1yeu1C/RcY0+NBHKZkFEeEb6ez0sg=
-----END CERTIFICATE-----
"""
    c.connect("rss-weather.yahoo.co.jp", 443)
    c.write(b"GET /rss/days/4410.xml HTTP/1.1\r\nHost: rss-weather.yahoo.co.jp\r\n\r\n")
    ret = process_output(c)
    c.stop()

    return ret

def process_output(c) :
    while True :
        a = c.read_until(b">")
        if len(a) == 0 : return None
        if a.endswith(b"</lastBuildDate>") : break
    skip = 1 if int(a.split()[-2].split(b":")[0]) > 3 else 0

    while True :
        a = c.read_until(b">")
        if len(a) == 0 : return None
        if a.endswith(b"</title>") :
            skip -= 1
            if skip < 0 : break

    ( _, date, place, _, weather, _, temp, _, _ ) = a.decode().split()
    return (date, place, weather, temp)

def show_weather() :
    disp = board.DISPLAY
    kt = KanjiTerminal(11, 9)
    kt.x = 72
    kt.y = 48
    disp.show(kt)
    be = ButtonEvents()

    def printc(y, txt) :
        kt.locate(5 - (len(txt) >> 1), y)
        kt.print(txt)
    
    def update(res) :
        kt.cls()
        if res is None : printc(4, "調整中")
        else :
            (date, place, weather, temp) = res
            date = han2zen(date)
            temp = han2zen(temp)
            printc(0, "明日の天気")
            printc(2, place)
            printc(4, date)
            printc(6, weather)
            printc(8, temp)
    
    res = get_weather()
    update(res)

    while True :
        time.sleep(1)
        buttons = be.buttons()
        if buttons == 0 : continue
        elif buttons & be.K_SELECT : break
        elif buttons & be.K_O :
            res = get_weather()
            update(res)

    be.deinit()
    disp.show(None)

status = wifi_connect()		# if None, return simply
if status is False :
    print("\nCannot connect to wifi.")
    time.sleep(3)
elif status is not None :
    show_weather()
