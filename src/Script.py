import os
import pyautogui
import time
import clipboard
import keyboard
import configparser
from loguru import logger
# Function to get text from clipboard and type it out
def type_clipboard_text(kpdelay):
    # Get text from clipboard
    text = clipboard.paste()

    # Type out the text
    pyautogui.typewrite(text, interval=kpdelay)

# Function to release keys from any sort of script interruption
def release_held_keys():
    keyboard.release('ctrl')
    keyboard.release('shift')

def on_termination_hotkey():
    logger.debug('Exit hotkey pressed. Terminating script..')
    release_held_keys()
    quit()

def main():
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))

    logger.info("Welcome to paste-by-keyboard 3.0")
    logger.debug("Reading settings.ini")
    
    config = configparser.ConfigParser()

    try:
        # Read from INI file
        config.read(os.path.join(FILE_DIR,'settings.ini'))

        # Set values
        PASTE_HOTKEY = config['Hotkeys'].get('paste', '')
        key_press_delay = config.get('Misc', 'delay')
        if PASTE_HOTKEY == '' or key_press_delay == '':
             raise ValueError('Values in config file can\'t be blank')
        
        logger.debug("Finished reading settings.ini successfully")
    except Exception as e:
        logger.debug("Error trying to read settings.ini")
        logger.debug('Resulting to default values. (Paste=home, delay=0)')
        PASTE_HOTKEY = 'home'
        key_press_delay = 0

    logger.debug(f"Listening for hotkeys. Paste Hotkey={PASTE_HOTKEY}")

    logger.info("Press ctrl + shift + Q to quit anytime")

    hotkey_was_pressed = False
    # Loop to listen for hotkey
    while True:
        hotkey_is_pressed = keyboard.is_pressed(PASTE_HOTKEY)
        # If hotkey is pressed and was not pressed in previous iteration of loop
        if hotkey_is_pressed and not hotkey_was_pressed:
            release_held_keys()
            # Type out the clipboard text
            type_clipboard_text(key_press_delay)

        hotkey_was_pressed = hotkey_is_pressed

        # Quit the script, has to be hard-coded so users can't possibly mess it up
        if keyboard.is_pressed('ctrl+shift+q'):
            on_termination_hotkey()

        # Small delay to avoid using too much CPU
        time.sleep(0.01)

if __name__ == '__main__':
    main()