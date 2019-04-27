from pynput import keyboard


class KeyboardListener:
    def __init__(self):
        self.key_pressed = 'l'

        self.listening_process = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release)

    def start(self):
        self.listening_process.start()

    def on_press(self, key):
        try:
            self.key_pressed = key.char
        except AttributeError:
            # print(f'special key {key} pressed')
            self.key_pressed = key

    def on_release(self, key):
        pass
        if key == keyboard.Key.esc:
            pass
