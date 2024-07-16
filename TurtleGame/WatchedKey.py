import turtle


class WatchedKey:
    def __init__(self, key):
        self.key = key
        self.down = False
        turtle.onkeypress(self.press, key)
        turtle.onkeyrelease(self.release, key)

    def press(self):
        self.down = True

    def release(self):
        self.down = False


# You can now create the watched keys you want to be able to check:
w_key = WatchedKey('w')


# and you can check their state by looking at their 'down' attribute
w_currently_pressed = w_key.down
