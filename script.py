from keyboard import write, add_hotkey, wait
from clipboard import paste


def clipboardToKeyboard():
    write(paste())


print("Paste by Keyboard script v1.0.0")
print("<ctrl> + <shift> + V to paste")
print("esc to exit.")

add_hotkey('ctrl+shift+v', clipboardToKeyboard)

wait('esc')
