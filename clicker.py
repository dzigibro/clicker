from pynput.mouse import Controller, Button
from pynput import keyboard
import threading
import time

clicking = True
mouse = Controller()

def auto_click():
    while clicking:
        mouse.click(Button.left)
        time.sleep(0.001)  # Adjust for faster/slower clicking

def on_key_press(key):
    global clicking
    if key == keyboard.KeyCode.from_char('a'):
        clicking = False
        print("\n[!] Clicker stopped.")
        return False  # Stop the key listener

def main():
    print("[+] Clicker started. Press 'A' to stop.")

    thread = threading.Thread(target=auto_click, daemon=True)
    thread.start()

    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
