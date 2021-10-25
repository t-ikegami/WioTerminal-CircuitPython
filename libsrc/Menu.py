#
# Choose menu for Wio Terminal console
# Display is 50x18 with top line outside of the screen.
#
import time
from ButtonEvents import ButtonEvents

def Menu(title, lst, idx = 0) :
    """Show choose menu on the text console.  50x18 screen is assumed.

    """
    n = len(lst)
    
    if n <= 30 :
        res = menu(title, lst, idx)
        return res

    idx = max(min(idx, n-1), 0)
    lst = [ lst[i:i+30] for i in range(0, n, 30) ]
    np = len(lst)
    
    while True :
        page = idx // 30
        res = menu(f"{title} ({page+1}/{np})", lst[page], idx % 30, paging = True)
        if res is None : return None
        idx = max(min(page * 30 + res, n-1), 0)
        if res < 0 or res >= 30 : continue
        break

    return idx
    
def menu(title, lst, idx = 0, paging = False) :
    """Show choose menu on the text console.  50x18 screen is assumed.  Up
    to 30 str items are allowed in lst.  When paging is True, BUTTON_1
    returns idx + 30 and BUTTON_2 returns idx - 30.  BUTTON_3 returns
    None.

    """
    n = len(lst)
    if n > 30 : raise ValueError("Menu list is too long. (<=30)")
    idx = max(min(idx, n-1), 0)

    x = 25 - len(title) // 2
    print(f"\x1b[2J\x1b[2;{x}H{title}", end = "")

    def calc_pos(i) :
        x = 1 if i < 15 else 26
        y = 4 + (i % 15)
        return (x, y)
    
    for i, s in enumerate(lst) :
        x, y = calc_pos(i)
        s = s[:23]
        print(f"\x1b[{y};{x+1}H{s}", end = "")
        
    be = ButtonEvents()
    be.wait_released()			# wait until all keys are released

    (x, y) = calc_pos(idx)
    print(f"\x1b[{y};{x}H>", end = "")
    while True :
        time.sleep(0.05)
        buttons = be.keys()
        if buttons == 0 : continue
        
        if paging :
            if   buttons & be.K_O :
                idx += 30
                break
            elif buttons & be.K_START :
                idx -= 30
                break
            elif buttons & be.K_RIGHT and idx >= 15 :
                idx += 15
                break
            elif buttons & be.K_LEFT and idx < 15 :
                idx -= 15
                break
            
        if buttons & be.K_UP    and idx > 0   : idx -= 1
        if buttons & be.K_DOWN  and idx < n-1 : idx += 1
        if buttons & be.K_RIGHT and idx < 15 and (idx + 15) < n : idx += 15
        if buttons & be.K_LEFT  and idx >= 15 : idx -= 15
        if buttons & be.K_X : break
        if buttons & be.K_SELECT :
            idx = None
            break

        print(f"\x1b[{y};{x}H ", end = "")
        (x, y) = calc_pos(idx)
        print(f"\x1b[{y};{x}H>", end = "")

    be.deinit()
    return idx
