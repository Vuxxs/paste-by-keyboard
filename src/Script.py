from keyboard import write, add_hotkey, wait
from clipboard import paste

# Hotkeys
paste_hotkey = 'ctrl+shift+v'
exit_hotkey = 'esc'


def main():
    print("Paste by Keyboard Script 2.0")
    print(f"{paste_hotkey} to paste")
    print(f"{exit_hotkey} to exit.")

    add_hotkey(paste_hotkey, write(paste()))

    wait(exit_hotkey)


if __name__ == '__main__':
    main()
